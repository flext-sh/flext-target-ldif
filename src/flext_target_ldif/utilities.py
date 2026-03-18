"""Singer target utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
import re
from collections.abc import Mapping
from datetime import UTC, datetime
from pathlib import Path
from typing import ClassVar, override

from flext_core import r
from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities
from flext_target_ldap.utilities import FlextTargetLdapUtilities

from .constants import c
from .typings import t


class FlextTargetLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Single unified utilities class for Singer target LDIF operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer target functionality with LDIF file operations.
    Extends urget-specific operations.
    """

    DEFAULT_BATCH_SIZE: ClassVar[int] = c.DEFAULT_BATCH_SIZE
    DEFAULT_TIMEOUT: ClassVar[int] = c.DEFAULT_TIMEOUT_SECONDS
    MAX_RETRIES: ClassVar[int] = c.MAX_RETRIES
    LDIF_LINE_WRAP_LENGTH: ClassVar[int] = c.LDIF_LINE_WRAP_LENGTH
    ASCII_SPACE: ClassVar[int] = c.ASCII_SPACE
    ASCII_TILDE: ClassVar[int] = c.ASCII_TILDE

    @override
    def __init__(self) -> None:
        """Initialize LDIF target utilities."""
        super().__init__()

    class TargetLdif:
        """Singer protocol utilities for target operations."""

        @staticmethod
        def parse_singer_message(
            line: str,
        ) -> r[Mapping[str, t.ContainerValue]]:
            """Parse Singer message from input line.

            Args:
            line: JSON line from Singer tap

            Returns:
            r[dict[str, t.ContainerValue]]: Parsed message or error

            """
            return FlextTargetLdapUtilities.TargetLdap.parse_singer_message(line)

        @staticmethod
        def validate_record_message(
            message: Mapping[str, t.ContainerValue],
        ) -> r[Mapping[str, t.ContainerValue]]:
            """Validate Singer RECORD message structure.

            Args:
            message: Singer message to validate

            Returns:
            r[dict[str, t.ContainerValue]]: Validated record or error

            """
            return FlextTargetLdapUtilities.TargetLdap.validate_record_message(message)

        @staticmethod
        def validate_schema_message(
            message: Mapping[str, t.ContainerValue],
        ) -> r[Mapping[str, t.ContainerValue]]:
            """Validate Singer SCHEMA message structure.

            Args:
            message: Singer message to validate

            Returns:
            r[dict[str, t.ContainerValue]]: Validated schema or error

            """
            return FlextTargetLdapUtilities.TargetLdap.validate_schema_message(message)

        @staticmethod
        def write_state_message(state: Mapping[str, t.ContainerValue]) -> None:
            """Write Singer state message to stdout.

            Args:
            state: State data to write

            """
            _ = state

    class LdifDataProcessing:
        """LDIF-specific data processing utilities."""

        @staticmethod
        def build_ldif_dn(
            record: Mapping[str, t.ContainerValue],
            dn_template: str,
            base_dn: str | None = None,
        ) -> r[str]:
            """Build LDIF Distinguished Name from record data.

            Args:
            record: Record data
            dn_template: DN template with placeholders
            base_dn: Optional base DN to append

            Returns:
            r[str]: Built DN or error

            """
            if not record or not dn_template:
                return r[str].fail("Record and DN template are required")
            try:
                dn_rdn = dn_template
                for key, value in record.items():
                    placeholder = f"{{{key}}}"
                    if placeholder in dn_rdn:
                        if value is None:
                            return r[str].fail(f"Cannot build DN: {key} is null")
                        dn_rdn = dn_rdn.replace(placeholder, str(value))
                if "{" in dn_rdn and "}" in dn_rdn:
                    return r[str].fail(f"Unresolved placeholders in DN: {dn_rdn}")
                full_dn = f"{dn_rdn},{base_dn}" if base_dn else dn_rdn
                if not FlextTargetLdifUtilities.LdifDataProcessing.split(full_dn):
                    return r[str].fail(f"Invalid DN format: {full_dn}")
                return r[str].ok(full_dn)
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[str].fail(f"Error building DN: {e}")

        @staticmethod
        def convert_record_to_ldif_entry(
            record: Mapping[str, t.ContainerValue],
            dn: str,
            object_classes: list[str] | None = None,
            attribute_mapping: Mapping[str, str] | None = None,
        ) -> r[str]:
            """Convert Singer record to LDIF entry format.

            Args:
            record: Singer record data
            dn: Distinguished Name for the entry
            object_classes: Object classes for the entry
            attribute_mapping: Optional mapping from record keys to LDIF attributes

            Returns:
            r[str]: LDIF entry or error

            """
            if not record or not dn:
                return r[str].fail("Record and DN are required")
            try:
                ldif_lines: list[str] = []
                mapping = attribute_mapping or {}
                ldif_lines.append(f"dn: {dn}")
                if object_classes:
                    ldif_lines.extend(f"objectClass: {oc}" for oc in object_classes)
                for key, value in record.items():
                    if value is None:
                        continue
                    ldif_attr = mapping.get(key, key)
                    if isinstance(value, list):
                        for item in value:
                            if item is not None:
                                ldif_value = FlextTargetLdifUtilities.LdifDataProcessing.format_ldif_value(
                                    str(item)
                                )
                                ldif_lines.append(f"{ldif_attr}: {ldif_value}")
                    else:
                        ldif_value = FlextTargetLdifUtilities.LdifDataProcessing.format_ldif_value(
                            str(value)
                        )
                        ldif_lines.append(f"{ldif_attr}: {ldif_value}")
                ldif_lines.append("")
                return r[str].ok("\n".join(ldif_lines))
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[str].fail(f"Error converting to LDIF entry: {e}")

        @staticmethod
        def format_ldif_value(value: str) -> str:
            """Format value for LDIF attribute.

            Args:
            value: Value to format

            Returns:
            str: Formatted LDIF value

            """
            if not value:
                return ""
            if value.startswith((" ", ":", "<")) or any(
                ord(c) < FlextTargetLdifUtilities.ASCII_SPACE
                or ord(c) > FlextTargetLdifUtilities.ASCII_TILDE
                for c in value
            ):
                encoded = base64.b64encode(value.encode("utf-8")).decode("ascii")
                return f":: {encoded}"
            if len(value) > FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                return FlextTargetLdifUtilities.LdifDataProcessing.wrap_ldif_line(value)
            return value

        @staticmethod
        def split(dn: str) -> bool:
            """Validate LDIF Distinguished Name format.

            Args:
            dn: Distinguished Name to validate

            Returns:
            bool: True if valid, False otherwise

            """
            if not dn:
                return False
            dn_pattern = "^[a-zA-Z][\\w\\-]*\\s*=\\s*[^,]+(?:\\s*,\\s*[a-zA-Z][\\w\\-]*\\s*=\\s*[^,]+)*$"
            return bool(re.match(dn_pattern, dn.strip()))

        @staticmethod
        def validate_ldif_entry(entry: str) -> r[bool]:
            """Validate LDIF entry format.

            Args:
            entry: LDIF entry to validate

            Returns:
            r[bool]: Validation result

            """
            if not entry or not entry.strip():
                return r[bool].fail("LDIF entry cannot be empty")
            lines = entry.strip().split("\n")
            if not lines:
                return r[bool].fail("LDIF entry must have at least one line")
            first_line = lines[0].strip()
            if not first_line.startswith("dn:"):
                return r[bool].fail("LDIF entry must start with DN")
            dn_value = first_line[3:].strip()
            if not dn_value:
                return r[bool].fail("DN cannot be empty")
            if not FlextTargetLdifUtilities.LdifDataProcessing.split(dn_value):
                return r[bool].fail(f"Invalid DN format: {dn_value}")
            return r[bool].ok(value=True)

        @staticmethod
        def wrap_ldif_line(value: str) -> str:
            """Wrap long LDIF lines according to RFC 2849.

            Args:
            value: Value to wrap

            Returns:
            str: Wrapped value

            """
            if len(value) <= FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                return value
            lines: list[str] = []
            remaining = value
            while remaining:
                if len(remaining) <= FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                    lines.append(remaining)
                    break
                break_point = FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH
                if " " in remaining[:break_point]:
                    break_point = remaining[:break_point].rfind(" ")
                lines.append(remaining[:break_point])
                remaining = " " + remaining[break_point:].lstrip()
            return "\n".join(lines)

    class FileUtilities:
        """File handling utilities for LDIF operations."""

        @staticmethod
        def append_to_ldif_file(file_path: str, entries: list[str]) -> r[str]:
            """Append entries to existing LDIF file.

            Args:
            file_path: Path to LDIF file
            entries: List of LDIF entries to append

            Returns:
            r[str]: Success message or error

            """
            if not file_path or not entries:
                return r[str].fail("File path and entries are required")
            try:
                path = Path(file_path)
                if not path.exists():
                    path.parent.mkdir(parents=True, exist_ok=True)
                with Path(path).open("a", encoding="utf-8") as f:
                    for entry in entries:
                        f.write(entry)
                        if not entry.endswith("\n"):
                            f.write("\n")
                return r[str].ok(f"Entries appended to LDIF file: {file_path}")
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[str].fail(f"Error appending to LDIF file: {e}")

        @staticmethod
        def create_ldif_file(
            file_path: str, entries: list[str], *, overwrite: bool = False
        ) -> r[str]:
            """Create LDIF file with entries.

            Args:
            file_path: Path to LDIF file
            entries: List of LDIF entries
            overwrite: Whether to overwrite existing file

            Returns:
            r[str]: Success message or error

            """
            if not file_path or not entries:
                return r[str].fail("File path and entries are required")
            try:
                path = Path(file_path)
                if path.exists() and (not overwrite):
                    return r[str].fail(f"File already exists: {file_path}")
                path.parent.mkdir(parents=True, exist_ok=True)
                with Path(path).open("w", encoding="utf-8") as f:
                    for entry in entries:
                        f.write(entry)
                        if not entry.endswith("\n"):
                            f.write("\n")
                return r[str].ok(f"LDIF file created: {file_path}")
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[str].fail(f"Error creating LDIF file: {e}")

        @staticmethod
        def validate_ldif_file_path(file_path: str) -> r[str]:
            """Validate LDIF file path.

            Args:
            file_path: Path to validate

            Returns:
            r[str]: Validated path or error

            """
            if not file_path or not file_path.strip():
                return r[str].fail("File path cannot be empty")
            try:
                path = Path(file_path)
                if not path.name:
                    return r[str].fail("Invalid file path")
                if path.suffix.lower() != ".ldif":
                    return r[str].fail("File must have .ldif extension")
                if path.parent.exists() and (not path.parent.is_dir()):
                    return r[str].fail("Parent path is not a directory")
                return r[str].ok(str(path.resolve()))
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[str].fail(f"Invalid file path: {e}")

    class StreamUtilities:
        """Stream processing utilities for Singer targets."""

        @staticmethod
        def calculate_ldif_batch_size(
            record_count: int, target_batches: int = 10
        ) -> int:
            """Calculate optimal batch size for LDIF operations.

            Args:
            record_count: Total number of records
            target_batches: Target number of batches

            Returns:
            int: Optimal batch size

            """
            if record_count <= 0:
                return FlextTargetLdifUtilities.DEFAULT_BATCH_SIZE
            calculated_size = max(1, record_count // target_batches)
            return min(calculated_size, FlextTargetLdifUtilities.DEFAULT_BATCH_SIZE)

        @staticmethod
        def generate_ldif_stream_metadata(
            stream_name: str,
            record_count: int,
            file_size_bytes: int,
            processing_time: float,
        ) -> Mapping[str, t.ContainerValue]:
            """Generate metadata for LDIF stream processing.

            Args:
            stream_name: Name of the stream
            record_count: Number of records processed
            file_size_bytes: Size of generated LDIF file
            processing_time: Time taken for processing

            Returns:
            dict[str, t.ContainerValue]: Stream metadata

            """
            return {
                "stream_name": stream_name,
                "records_processed": record_count,
                "file_size_bytes": file_size_bytes,
                "file_size_mb": round(file_size_bytes / (1024 * 1024), 2),
                "processing_time_seconds": processing_time,
                "records_per_second": record_count / max(processing_time, 0.001),
                "processing_timestamp": datetime.now(UTC).isoformat(),
                "target_type": "ldif",
            }

        @staticmethod
        def validate_stream_compatibility(
            stream_name: str, schema: Mapping[str, t.ContainerValue]
        ) -> r[bool]:
            """Validate stream compatibility with LDIF operations.

            Args:
            stream_name: Name of the stream
            schema: Stream schema

            Returns:
            r[bool]: Validation result

            """
            if not stream_name or not schema:
                return r[bool].fail("Stream name and schema are required")
            properties_raw = schema.get("properties", {})
            if not isinstance(properties_raw, Mapping) or not properties_raw:
                return r[bool].fail("Schema must have properties")
            properties_map = properties_raw
            properties: dict[str, t.ContainerValue] = {
                str(key): value for key, value in properties_map.items()
            }
            has_dn_field = "dn" in properties
            has_id_fields = any(
                key in properties for key in ["id", "uid", "cn", "username", "email"]
            )
            if not has_dn_field and (not has_id_fields):
                return r[bool].fail(
                    "Schema must have either 'dn' field or identifier fields (id, uid, cn, username, email)"
                )
            return r[bool].ok(value=True)

    class ConfigValidation:
        """Configuration validation utilities."""

        @staticmethod
        def validate_ldif_entry_config(
            config: Mapping[str, t.ContainerValue],
        ) -> r[Mapping[str, t.ContainerValue]]:
            """Validate LDIF entry configuration.

            Args:
            config: Entry configuration

            Returns:
            r[dict[str, t.ContainerValue]]: Validated config or error

            """
            if "object_classes" in config:
                object_classes = config["object_classes"]
                if not isinstance(object_classes, list) or not object_classes:
                    return r[Mapping[str, t.ContainerValue]].fail(
                        "Object classes must be a non-empty list"
                    )
                for oc in object_classes:
                    match oc:
                        case str() as object_class if object_class.strip():
                            pass
                        case _:
                            return r[Mapping[str, t.ContainerValue]].fail(
                                "All object classes must be non-empty strings"
                            )
            if "attribute_mapping" in config:
                attribute_mapping = config["attribute_mapping"]
                if not isinstance(attribute_mapping, Mapping):
                    return r[Mapping[str, t.ContainerValue]].fail(
                        "Attribute mapping must be a dictionary"
                    )
                attribute_mapping_map = attribute_mapping
                for key, value in attribute_mapping_map.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return r[Mapping[str, t.ContainerValue]].fail(
                            "Attribute mapping keys and values must be strings"
                        )
            return r[Mapping[str, t.ContainerValue]].ok(config)

        @staticmethod
        def validate_ldif_target_config(
            config: Mapping[str, t.ContainerValue],
        ) -> r[Mapping[str, t.ContainerValue]]:
            """Validate LDIF target configuration.

            Args:
            config: Configuration dictionary

            Returns:
            r[dict[str, t.ContainerValue]]: Validated config or error

            """
            required_fields = ["output_file"]
            missing_fields = [field for field in required_fields if field not in config]
            if missing_fields:
                return r[Mapping[str, t.ContainerValue]].fail(
                    f"Missing required LDIF target fields: {', '.join(missing_fields)}"
                )
            output_file_raw = config["output_file"]
            if not isinstance(output_file_raw, str):
                return r[Mapping[str, t.ContainerValue]].fail(
                    "Invalid output file: output_file must be a string"
                )
            output_file = output_file_raw
            file_validation = (
                FlextTargetLdifUtilities.FileUtilities.validate_ldif_file_path(
                    output_file
                )
            )
            if file_validation.is_failure:
                return r[Mapping[str, t.ContainerValue]].fail(
                    f"Invalid output file: {file_validation.error}"
                )
            operation_mode = config.get("operation_mode", "append")
            valid_modes = ["append", "overwrite", "create"]
            if operation_mode not in valid_modes:
                return r[Mapping[str, t.ContainerValue]].fail(
                    f"Invalid operation mode: {operation_mode}. Valid modes: {', '.join(valid_modes)}"
                )
            if "dn_template" in config:
                dn_template = config["dn_template"]
                match dn_template:
                    case str() as template if template.strip():
                        pass
                    case _:
                        return r[Mapping[str, t.ContainerValue]].fail(
                            "DN template must be a non-empty string"
                        )
            batch_size_raw = config.get(
                "batch_size", FlextTargetLdifUtilities.DEFAULT_BATCH_SIZE
            )
            if not isinstance(batch_size_raw, int):
                return r[Mapping[str, t.ContainerValue]].fail(
                    "Batch size must be a positive integer"
                )
            if batch_size_raw <= 0:
                return r[Mapping[str, t.ContainerValue]].fail(
                    "Batch size must be a positive integer"
                )
            return r[Mapping[str, t.ContainerValue]].ok(config)

    class StateManagement:
        """State management utilities for target operations."""

        @staticmethod
        def create_processing_state(
            stream_name: str,
            records_processed: int,
            file_path: str,
            file_size_bytes: int,
            last_processed_record: Mapping[str, t.ContainerValue] | None = None,
        ) -> Mapping[str, t.ContainerValue]:
            """Create processing state for target stream.

            Args:
            stream_name: Name of the stream
            records_processed: Number of records processed
            file_path: Path to LDIF file
            file_size_bytes: Size of LDIF file
            last_processed_record: Last processed record for checkpointing

            Returns:
            dict[str, t.ContainerValue]: Processing state

            """
            state: dict[str, t.ContainerValue] = {
                "stream_name": stream_name,
                "records_processed": records_processed,
                "output_file": file_path,
                "file_size_bytes": file_size_bytes,
                "last_updated": datetime.now(UTC).isoformat(),
                "target_type": "ldif",
            }
            if last_processed_record:
                checkpoint_data: dict[str, t.ContainerValue | None] = {
                    "id": last_processed_record.get("id"),
                    "dn": last_processed_record.get("dn"),
                    "timestamp": last_processed_record.get("_timestamp"),
                }
                state["checkpoint"] = {
                    k: v for k, v in checkpoint_data.items() if v is not None
                }
            return state

        @staticmethod
        def get_target_state(
            state: Mapping[str, t.ContainerValue], stream_name: str
        ) -> Mapping[str, t.ContainerValue]:
            """Get state for a specific target stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream

            Returns:
            dict[str, t.ContainerValue]: Stream state

            """
            bookmarks = state.get("bookmarks", {})
            if not isinstance(bookmarks, Mapping):
                return {}
            bookmarks_map = bookmarks
            stream_state = bookmarks_map.get(stream_name, {})
            if not isinstance(stream_state, Mapping):
                return {}
            stream_state_map = stream_state
            return {str(key): value for key, value in stream_state_map.items()}

        @staticmethod
        def set_target_state(
            state: Mapping[str, t.ContainerValue],
            stream_name: str,
            stream_state: Mapping[str, t.ContainerValue],
        ) -> Mapping[str, t.ContainerValue]:
            """Set state for a specific target stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            stream_state: State data for the stream

            Returns:
            dict[str, t.ContainerValue]: Updated state

            """
            updated_state = dict(state)
            bookmarks_raw = updated_state.get("bookmarks")
            bookmarks: dict[str, t.ContainerValue] = {}
            if isinstance(bookmarks_raw, Mapping):
                bookmarks = {str(key): value for key, value in bookmarks_raw.items()}
            bookmarks[stream_name] = dict(stream_state)
            updated_state["bookmarks"] = bookmarks
            return updated_state

        @staticmethod
        def update_processing_progress(
            state: Mapping[str, t.ContainerValue],
            stream_name: str,
            records_count: int,
            file_size_bytes: int,
        ) -> Mapping[str, t.ContainerValue]:
            """Update processing progress in state.

            Args:
            state: Current state
            stream_name: Name of the stream
            records_count: Number of records processed in this batch
            file_size_bytes: Current file size

            Returns:
            dict[str, t.ContainerValue]: Updated state

            """
            stream_state = FlextTargetLdifUtilities.StateManagement.get_target_state(
                state, stream_name
            )
            current_count_raw = stream_state.get("records_processed", 0)
            current_count = (
                current_count_raw if isinstance(current_count_raw, int) else 0
            )
            new_count = current_count + records_count
            batch_count_raw = stream_state.get("batch_count", 0)
            batch_count = batch_count_raw if isinstance(batch_count_raw, int) else 0
            updated_stream_state: dict[str, t.ContainerValue] = {
                **stream_state,
                "records_processed": new_count,
                "file_size_bytes": file_size_bytes,
                "last_updated": datetime.now(UTC).isoformat(),
                "batch_count": batch_count + 1,
            }
            return FlextTargetLdifUtilities.StateManagement.set_target_state(
                state, stream_name, updated_stream_state
            )


u = FlextTargetLdifUtilities
__all__ = ["FlextTargetLdifUtilities", "u"]
