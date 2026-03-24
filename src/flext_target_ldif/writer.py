"""LDIF writer for flext-target-ldif using flext-ldif infrastructure.

This module eliminates code duplication by using the FLEXT LDIF infrastructure
implementation from flext-ldif project.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
import types
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Self, TextIO, override

from flext_core import FlextLogger, r, t
from flext_ldif import FlextLdif

from flext_target_ldif import FlextTargetLdifWriterError

logger = FlextLogger(__name__)


class FlextTargetLdifWriter:
    """Writer for converting data records to LDIF format."""

    @override
    def __init__(
        self,
        output_file: Path | str | None = None,
        ldif_options: Mapping[str, t.ContainerValue] | None = None,
        dn_template: str | None = None,
        attribute_mapping: t.StrMapping | None = None,
        schema: Mapping[str, t.ContainerValue | t.StrSequence] | None = None,
    ) -> None:
        """Initialize the LDIF writer using flext-ldif infrastructure."""
        self.output_file = Path(output_file) if output_file else Path("output.ldif")
        self.ldif_options = ldif_options or {}
        self.dn_template = dn_template or "uid={uid},ou=users,dc=example,dc=com"
        self.attribute_mapping = attribute_mapping or {}
        self.schema = schema or {}
        line_length_val = self.ldif_options.get("line_length", 78)
        if isinstance(line_length_val, int):
            self.line_length: int = line_length_val
        elif isinstance(line_length_val, (str, float)):
            self.line_length = int(line_length_val)
        else:
            self.line_length = 78
        base64_val = self.ldif_options.get("base64_encode", False)
        self.base64_encode: bool = bool(base64_val) if base64_val is not None else False
        timestamps_val = self.ldif_options.get("include_timestamps", True)
        self.include_timestamps: bool = (
            bool(timestamps_val) if timestamps_val is not None else True
        )
        self._ldif_api = FlextLdif()
        self._records: list[Mapping[str, t.ContainerValue]] = []
        self._record_count = 0
        self._ldif_entries: Sequence[
            Mapping[str, str | Mapping[str, t.StrSequence]]
        ] = []
        self._file_handle: TextIO | None = None

    def __enter__(self) -> Self:
        """Context manager entry."""
        self.open()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        """Context manager exit."""
        self.close()

    @property
    def record_count(self) -> int:
        """Get the number of records written."""
        return self._record_count

    def close(self) -> r[bool]:
        """Close the output file and write all collected records."""
        try:
            self._ldif_entries = []
            for record in self._records:
                entry = self._convert_record_to_entry(record)
                if entry is not None:
                    self._ldif_entries.append(entry)
            self._write_entries_to_file()
            if self._file_handle is not None:
                self._file_handle.close()
                self._file_handle = None
            return r[bool].ok(value=True)
        except (RuntimeError, ValueError, TypeError, OSError, Exception) as e:
            self._file_handle = None
            return r[bool].fail(f"Failed to close LDIF file: {e}")

    def open(self) -> r[bool]:
        """Open the output file for writing."""
        try:
            self.output_file.parent.mkdir(parents=True, exist_ok=True)
            self._file_handle = self.output_file.open("w", encoding="utf-8")
            return r[bool].ok(value=True)
        except (RuntimeError, ValueError, TypeError, OSError) as e:
            return r[bool].fail(f"Failed to open LDIF file: {e}")

    def write_record(self, record: Mapping[str, t.ContainerValue]) -> r[bool]:
        """Write a record to the LDIF file buffer."""
        try:
            if self._file_handle is None:
                open_result = self.open()
                if not open_result.is_success:
                    return r[bool].fail(f"Failed to write record: {open_result.error}")
            self._generate_dn(record)
            self._records.append(dict(record))
            self._record_count += 1
            return r[bool].ok(value=True)
        except (
            RuntimeError,
            ValueError,
            TypeError,
            FlextTargetLdifWriterError,
        ) as e:
            return r[bool].fail(f"Failed to write record: {e}")

    def _convert_record_to_entry(
        self, record: Mapping[str, t.ContainerValue]
    ) -> Mapping[str, str | Mapping[str, t.StrSequence]] | None:
        """Convert a single record to LDIF entry format."""
        try:
            dn = self._generate_dn(record)
            attributes: dict[str, t.ContainerValue] = {}
            for key, value in record.items():
                if key != "dn":
                    mapped_key = self.attribute_mapping.get(key, key)
                    attributes[mapped_key] = value
            attr_dict: dict[str, t.StrSequence] = {}
            for key, value in attributes.items():
                if isinstance(value, list):
                    attr_dict[key] = [str(v) for v in value]
                else:
                    attr_dict[key] = [str(value)]
            result: Mapping[str, str | Mapping[str, t.StrSequence]] = {
                "dn": dn,
                "attributes": attr_dict,
            }
            return result
        except (RuntimeError, ValueError, TypeError, FlextTargetLdifWriterError) as e:
            logger.warning(f"Skipping invalid record: {e}")
            return None

    def _generate_dn(self, record: Mapping[str, t.ContainerValue]) -> str:
        """Generate DN from record using template."""
        try:
            return self.dn_template.format(**record)
        except KeyError as e:
            msg: str = f"Missing required field for DN generation: {e}"
            raise FlextTargetLdifWriterError(msg) from e

    def _needs_base64_encoding(self, value: str) -> bool:
        """Check if a value needs base64 encoding."""
        if value and value[0] in {" ", ":"}:
            return True
        try:
            value.encode("ascii")
        except UnicodeEncodeError:
            return True
        return "\n" in value or "\r" in value

    def _write_attribute(self, attr_name: str, value: str) -> None:
        """Write an attribute to the file handle."""
        if self._file_handle is None:
            msg = "File handle is not open"
            raise ValueError(msg)
        if self._needs_base64_encoding(value):
            encoded = base64.b64encode(value.encode("utf-8")).decode("ascii")
            self._file_handle.write(f"{attr_name}:: {encoded}\n")
        else:
            self._file_handle.write(f"{attr_name}: {value}\n")

    def _write_entries_to_file(self) -> None:
        """Write LDIF entries to file."""
        with self.output_file.open("w", encoding="utf-8") as f:
            f.write("version: 1\n")
            if self.include_timestamps:
                f.write(f"# Generated on: {datetime.now(UTC).isoformat()}\n")
            f.write("\n")
            for entry in self._ldif_entries:
                dn_obj = entry.get("dn", "")
                dn_str = str(dn_obj) if dn_obj else ""
                raw_attributes = entry.get("attributes", {})
                attributes_obj: Mapping[str, str | t.StrSequence] = {}
                if isinstance(raw_attributes, dict):
                    attributes_obj = {
                        str(key): value for key, value in raw_attributes.items()
                    }
                f.write(f"dn: {dn_str}\n")
                self._write_entry_attributes(f, attributes_obj)
                f.write("\n")

    def _write_entry_attributes(
        self, f: TextIO, attributes_obj: Mapping[str, str | t.StrSequence]
    ) -> None:
        """Write entry attributes to file."""
        for attr, values in attributes_obj.items():
            if isinstance(values, list):
                for value in values:
                    if self.base64_encode:
                        encoded = base64.b64encode(str(value).encode("utf-8")).decode(
                            "ascii"
                        )
                        f.write(f"{attr}:: {encoded}\n")
                    else:
                        f.write(f"{attr}: {value}\n")
            elif self.base64_encode:
                encoded = base64.b64encode(str(values).encode("utf-8")).decode("ascii")
                f.write(f"{attr}:: {encoded}\n")
            else:
                f.write(f"{attr}: {values}\n")

    def _write_line(self, line: str) -> None:
        """Write a line to the file handle, wrapping if necessary."""
        if self._file_handle is None:
            msg = "File handle is not open"
            raise ValueError(msg)
        if len(line) <= self.line_length:
            self._file_handle.write(line + "\n")
        else:
            self._file_handle.write(line[: self.line_length] + "\n")
            remaining = line[self.line_length :]
            while remaining:
                chunk = remaining[: self.line_length - 1]
                self._file_handle.write(" " + chunk + "\n")
                remaining = remaining[self.line_length - 1 :]


__all__: t.StrSequence = ["LdifWriter"]
