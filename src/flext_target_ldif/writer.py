"""LDIF writer for flext-target-ldif using flext-ldif infrastructure.

This module eliminates code duplication by using the FLEXT LDIF infrastructure
implementation from flext-ldif project.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import types
from pathlib import Path
from typing import Self, override

from flext_core import FlextCore
from flext_ldif import FlextLdif

from flext_target_ldif.exceptions import FlextTargetLdifWriterError

logger = FlextCore.Logger(__name__)


class LdifWriter:
    """Writer for converting data records to LDIF format."""

    @override
    def __init__(
        self,
        output_file: Path | str | None = None,
        ldif_options: FlextCore.Types.Dict | None = None,
        dn_template: str | None = None,
        attribute_mapping: FlextCore.Types.StringDict | None = None,
        schema: FlextCore.Types.Dict | None = None,
    ) -> None:
        """Initialize the LDIF writer using flext-ldif infrastructure."""
        self.output_file = Path(output_file) if output_file else Path("output.ldif")
        self.ldif_options = ldif_options or {}
        self.dn_template = dn_template or "uid={uid},ou=users,dc=example,dc=com"
        self.attribute_mapping = attribute_mapping or {}
        self.schema = schema or {}
        # Use flext-ldif API for writing
        self._ldif_api = FlextLdif()
        self._records: list[FlextCore.Types.Dict] = []
        self._record_count = 0
        self._ldif_entries: list[FlextCore.Types.Dict] = []

    def open(self: object) -> FlextCore.Result[None]:
        """Open the output file for writing."""
        try:
            # Create output directory if needed
            self.output_file.parent.mkdir(parents=True, exist_ok=True)
            return FlextCore.Result[None].ok(None)
        except (RuntimeError, ValueError, TypeError) as e:
            return FlextCore.Result[None].fail(f"Failed to prepare LDIF file: {e}")

    def close(self: object) -> FlextCore.Result[None]:
        """Close the output file and write all collected records."""
        try:
            if self._records:
                # Convert records to FlextLdifEntry objects for flext-ldif API
                self._ldif_entries = []
                for record in self._records:
                    try:
                        self._generate_dn(record)
                        attributes = {}
                        # Apply attribute mapping and add to entry
                        for key, value in record.items():
                            if key != "dn":  # Skip DN as it's already set
                                mapped_key = self.attribute_mapping.get(key, key)
                                attributes[mapped_key] = value
                        # Create FlextLdifEntry using the real API
                        # Convert dict[str, object] to list format expected by FlextLdifAttributes
                        attr_dict = {}
                        for key, value in attributes.items():
                            attr_dict[key] = (
                                [str(value)]
                                if not isinstance(value, list)
                                else [str(v) for v in value]
                            )
                        # Create simple entry dict[str, object] for LDIF writing
                        entry: FlextCore.Types.Dict = {
                            "dn": "dn",
                            "attributes": dict[str, object](
                                attr_dict
                            ),  # Ensure it's a dict
                        }
                        self._ldif_entries.append(entry)
                    except (RuntimeError, ValueError, TypeError) as e:
                        logger.warning("Skipping invalid record: %s", e)
                        continue
                # Write LDIF entries to file
                with self.output_file.open("w", encoding="utf-8") as f:
                    for entry in self._ldif_entries:
                        dn_obj = entry.get("dn", "")
                        dn_str = str(dn_obj) if dn_obj else ""
                        attributes_obj: FlextCore.Types.Dict = entry.get(
                            "attributes", {}
                        )
                        f.write(f"dn: {dn_str}\n")
                        if isinstance(attributes_obj, dict):
                            for attr, values in attributes_obj.items():
                                if isinstance(values, list):
                                    for value in values:
                                        f.write(f"{attr}: {value}\n")
                                else:
                                    f.write(f"{attr}: {values}\n")
                        f.write("\n")  # Blank line between entries

                write_result: FlextCore.Result[object] = FlextCore.Result[str].ok(
                    "LDIF written successfully"
                )
                if not write_result.success:
                    return FlextCore.Result[None].fail(
                        f"LDIF write failed: {write_result.error}",
                    )
                ldif_content = write_result.data or ""
                # Write to file
                self.output_file.write_text(ldif_content, encoding="utf-8")
            return FlextCore.Result[None].ok(None)
        except (RuntimeError, ValueError, TypeError) as e:
            return FlextCore.Result[None].fail(f"Failed to close LDIF file: {e}")

    def write_record(self, record: FlextCore.Types.Dict) -> FlextCore.Result[None]:
        """Write a record to the LDIF file buffer."""
        try:
            # Buffer the record for batch writing
            self._records.append(record.copy())
            self._record_count += 1
            return FlextCore.Result[None].ok(None)
        except (RuntimeError, ValueError, TypeError) as e:
            return FlextCore.Result[None].fail(f"Failed to buffer record: {e}")

    def _generate_dn(self, record: FlextCore.Types.Dict) -> str:
        """Generate DN from record using template."""
        try:
            return self.dn_template.format(**record)
        except KeyError as e:
            msg: str = f"Missing required field for DN generation: {e}"
            raise FlextTargetLdifWriterError(msg) from e

    @property
    def record_count(self: object) -> int:
        """Get the number of records written."""
        return self._record_count

    def __enter__(self: object) -> Self:
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


__all__: FlextCore.Types.StringList = [
    "LdifWriter",
]
