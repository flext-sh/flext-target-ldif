"""LDIF writer for flext-target-ldif using flext-ldif infrastructure.

This module eliminates code duplication by using the FLEXT LDIF infrastructure
implementation from flext-ldif project.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
import types
from collections.abc import Mapping
from pathlib import Path
from typing import Self, TextIO, override

from flext_core import FlextLogger, FlextResult, t, u
from flext_ldif import FlextLdif

from flext_target_ldif.exceptions import FlextTargetLdifWriterError

logger = FlextLogger(__name__)


class LdifWriter:
    """Writer for converting data records to LDIF format."""

    @override
    def __init__(
        self,
        output_file: Path | str | None = None,
        ldif_options: Mapping[str, t.GeneralValueType] | None = None,
        dn_template: str | None = None,
        attribute_mapping: Mapping[str, str] | None = None,
        schema: Mapping[str, t.GeneralValueType] | None = None,
    ) -> None:
        """Initialize the LDIF writer using flext-ldif infrastructure."""
        self.output_file = Path(output_file) if output_file else Path("output.ldif")
        self.ldif_options = ldif_options or {}
        self.dn_template = dn_template or "uid={uid},ou=users,dc=example,dc=com"
        self.attribute_mapping = attribute_mapping or {}
        self.schema = schema or {}
        # Extract LDIF options with defaults
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
        # Use flext-ldif API for writing
        self._ldif_api = FlextLdif()
        self._records: list[dict[str, t.GeneralValueType]] = []
        self._record_count = 0
        self._ldif_entries: list[Mapping[str, t.GeneralValueType]] = []
        self._file_handle: TextIO | None = None

    def open(self) -> FlextResult[bool]:
        """Open the output file for writing."""
        try:
            # Create output directory if needed
            self.output_file.parent.mkdir(parents=True, exist_ok=True)
            self._file_handle = self.output_file.open("w", encoding="utf-8")
            return FlextResult[bool].ok(value=True)
        except (RuntimeError, ValueError, TypeError, OSError) as e:
            return FlextResult[bool].fail(f"Failed to open LDIF file: {e}")

    def _convert_record_to_entry(
        self,
        record: Mapping[str, t.GeneralValueType],
    ) -> Mapping[str, t.GeneralValueType] | None:
        """Convert a single record to LDIF entry format."""
        try:
            self._generate_dn(record)
            attributes = {}
            # Apply attribute mapping and add to entry
            for key, value in record.items():
                if key != "dn":  # Skip DN as it's already set
                    mapped_key = self.attribute_mapping.get(key, key)
                    attributes[mapped_key] = value
            # Create FlextLdifEntry using the real API
            # Convert dict[str, t.GeneralValueType] to list format expected by FlextLdifAttributes
            attr_dict: dict[str, list[str]] = {}
            for key, value in attributes.items():
                attr_dict[key] = (
                    [str(value)]
                    if not u.Guards.is_list(value)
                    else [str(v) for v in value]
                )
            # Create simple entry dict[str, t.GeneralValueType] for LDIF writing
            return {
                "dn": "dn",
                "attributes": attr_dict,
            }
        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning("Skipping invalid record: %s", str(e))  # noqa: RUF065
            return None

    def _write_entry_attributes(
        self,
        f: TextIO,
        attributes_obj: Mapping[str, t.GeneralValueType],
    ) -> None:
        """Write entry attributes to file."""
        if u.is_dict_like(attributes_obj):
            for attr, values in attributes_obj.items():
                if u.Guards.is_list(values):
                    f.writelines(f"{attr}: {value}\n" for value in values)
                else:
                    f.write(f"{attr}: {values}\n")

    def _write_entries_to_file(self) -> None:
        """Write LDIF entries to file."""
        with self.output_file.open("w", encoding="utf-8") as f:
            for entry in self._ldif_entries:
                dn_obj = entry.get("dn", "")
                dn_str = str(dn_obj) if dn_obj else ""
                raw_attributes = entry.get("attributes", {})
                attributes_obj: dict[str, t.GeneralValueType] = {}
                if isinstance(raw_attributes, Mapping):
                    attributes_obj = {
                        str(key): value for key, value in raw_attributes.items()
                    }
                f.write(f"dn: {dn_str}\n")
                self._write_entry_attributes(f, attributes_obj)
                f.write("\n")

    def close(self) -> FlextResult[bool]:
        """Close the output file and write all collected records."""
        try:
            if self._records:
                # Convert records to FlextLdifEntry objects for flext-ldif API
                self._ldif_entries = []
                for record in self._records:
                    entry = self._convert_record_to_entry(record)
                    if entry is not None:
                        self._ldif_entries.append(entry)
                # Write LDIF entries to file
                self._write_entries_to_file()
            if self._file_handle is not None:
                self._file_handle.close()
                self._file_handle = None
            return FlextResult[bool].ok(value=True)
        except (RuntimeError, ValueError, TypeError, OSError) as e:
            return FlextResult[bool].fail(f"Failed to close LDIF file: {e}")

    def write_record(
        self,
        record: Mapping[str, t.GeneralValueType],
    ) -> FlextResult[bool]:
        """Write a record to the LDIF file buffer."""
        try:
            # Buffer the record for batch writing
            self._records.append(dict(record))
            self._record_count += 1
            return FlextResult[bool].ok(value=True)
        except (RuntimeError, ValueError, TypeError) as e:
            return FlextResult[bool].fail(f"Failed to buffer record: {e}")

    def _generate_dn(self, record: Mapping[str, t.GeneralValueType]) -> str:
        """Generate DN from record using template."""
        try:
            return self.dn_template.format(**record)
        except KeyError as e:
            msg: str = f"Missing required field for DN generation: {e}"
            raise FlextTargetLdifWriterError(msg) from e

    def _needs_base64_encoding(self, value: str) -> bool:
        """Check if a value needs base64 encoding."""
        # Check for leading space or colon
        if value and value[0] in {" ", ":"}:
            return True
        # Check for non-ASCII characters
        try:
            value.encode("ascii")
        except UnicodeEncodeError:
            return True
        # Check for newlines or carriage returns
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

    def _write_line(self, line: str) -> None:
        """Write a line to the file handle, wrapping if necessary."""
        if self._file_handle is None:
            msg = "File handle is not open"
            raise ValueError(msg)
        if len(line) <= self.line_length:
            self._file_handle.write(line + "\n")
        else:
            # Wrap long lines according to LDIF spec
            self._file_handle.write(line[: self.line_length] + "\n")
            remaining = line[self.line_length :]
            while remaining:
                chunk = remaining[: self.line_length - 1]
                self._file_handle.write(" " + chunk + "\n")
                remaining = remaining[self.line_length - 1 :]

    @property
    def record_count(self) -> int:
        """Get the number of records written."""
        return self._record_count

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


__all__: list[str] = [
    "LdifWriter",
]
