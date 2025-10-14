"""Singer target utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
import json
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import ClassVar, override

from flext_core import FlextCore


class FlextTargetLdifUtilities(FlextCore.Utilities):
    """Single unified utilities class for Singer target LDIF operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer target functionality with LDIF file operations.
    Extends FlextCore.Utilities with LDIF target-specific operations.
    """

    # Configuration constants
    DEFAULT_BATCH_SIZE: ClassVar[int] = 1000
    DEFAULT_TIMEOUT: ClassVar[int] = 30
    MAX_RETRIES: ClassVar[int] = 3
    LDIF_LINE_WRAP_LENGTH: ClassVar[int] = 76

    # ASCII character constants for LDIF encoding
    ASCII_SPACE: ClassVar[int] = 32
    ASCII_TILDE: ClassVar[int] = 126

    @override
    def __init__(self) -> None:
        """Initialize LDIF target utilities."""
        super().__init__()

    class SingerUtilities:
        """Singer protocol utilities for target operations."""

        @staticmethod
        def parse_singer_message(line: str) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Parse Singer message from input line.

            Args:
                line: JSON line from Singer tap

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Parsed message or error

            """
            if not line or not line.strip():
                return FlextCore.Result[FlextCore.Types.Dict].fail("Empty input line")

            try:
                message = json.loads(line.strip())
                if not isinstance(message, dict):
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "Message must be a JSON object"
                    )

                if "type" not in message:
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "Message missing required 'type' field"
                    )

                return FlextCore.Result[FlextCore.Types.Dict].ok(message)

            except json.JSONDecodeError as e:
                return FlextCore.Result[FlextCore.Types.Dict].fail(f"Invalid JSON: {e}")

        @staticmethod
        def validate_record_message(
            message: FlextCore.Types.Dict,
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Validate Singer RECORD message structure.

            Args:
                message: Singer message to validate

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Validated record or error

            """
            if message.get("type") != "RECORD":
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    "Message type must be RECORD"
                )

            required_fields = ["stream", "record"]
            for field in required_fields:
                if field not in message:
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        f"RECORD message missing '{field}' field"
                    )

            record = message["record"]
            if not isinstance(record, dict):
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    "Record data must be a dictionary"
                )

            return FlextCore.Result[FlextCore.Types.Dict].ok(message)

        @staticmethod
        def validate_schema_message(
            message: FlextCore.Types.Dict,
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Validate Singer SCHEMA message structure.

            Args:
                message: Singer message to validate

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Validated schema or error

            """
            if message.get("type") != "SCHEMA":
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    "Message type must be SCHEMA"
                )

            required_fields = ["stream", "schema"]
            for field in required_fields:
                if field not in message:
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        f"SCHEMA message missing '{field}' field"
                    )

            schema = message["schema"]
            if not isinstance(schema, dict):
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    "Schema data must be a dictionary"
                )

            return FlextCore.Result[FlextCore.Types.Dict].ok(message)

        @staticmethod
        def write_state_message(state: FlextCore.Types.Dict) -> None:
            """Write Singer state message to stdout.

            Args:
                state: State data to write

            """

    class LdifDataProcessing:
        """LDIF-specific data processing utilities."""

        @staticmethod
        def build_ldif_dn(
            record: FlextCore.Types.Dict,
            dn_template: str,
            base_dn: str | None = None,
        ) -> FlextCore.Result[str]:
            """Build LDIF Distinguished Name from record data.

            Args:
                record: Record data
                dn_template: DN template with placeholders
                base_dn: Optional base DN to append

            Returns:
                FlextCore.Result[str]: Built DN or error

            """
            if not record or not dn_template:
                return FlextCore.Result[str].fail("Record and DN template are required")

            try:
                # Replace placeholders in DN template
                dn_rdn = dn_template
                for key, value in record.items():
                    placeholder = f"{{{key}}}"
                    if placeholder in dn_rdn:
                        if value is None:
                            return FlextCore.Result[str].fail(
                                f"Cannot build DN: {key} is null"
                            )
                        dn_rdn = dn_rdn.replace(placeholder, str(value))

                # Check if all placeholders were replaced
                if "{" in dn_rdn and "}" in dn_rdn:
                    return FlextCore.Result[str].fail(
                        f"Unresolved placeholders in DN: {dn_rdn}"
                    )

                # Combine with base DN if provided
                full_dn = f"{dn_rdn},{base_dn}" if base_dn else dn_rdn

                # Validate DN format
                if not FlextTargetLdifUtilities.LdifDataProcessing.validate_dn_format(
                    full_dn
                ):
                    return FlextCore.Result[str].fail(f"Invalid DN format: {full_dn}")

                return FlextCore.Result[str].ok(full_dn)

            except Exception as e:
                return FlextCore.Result[str].fail(f"Error building DN: {e}")

        @staticmethod
        def validate_dn_format(dn: str) -> bool:
            """Validate LDIF Distinguished Name format.

            Args:
                dn: Distinguished Name to validate

            Returns:
                bool: True if valid, False otherwise

            """
            if not dn:
                return False

            # Basic DN format validation
            # Should contain at least one RDN component (attr=value)
            dn_pattern = (
                r"^[a-zA-Z][\w\-]*\s*=\s*[^,]+(?:\s*,\s*[a-zA-Z][\w\-]*\s*=\s*[^,]+)*$"
            )
            return bool(re.match(dn_pattern, dn.strip()))

        @staticmethod
        def convert_record_to_ldif_entry(
            record: FlextCore.Types.Dict,
            dn: str,
            object_classes: FlextCore.Types.StringList | None = None,
            attribute_mapping: FlextCore.Types.StringDict | None = None,
        ) -> FlextCore.Result[str]:
            """Convert Singer record to LDIF entry format.

            Args:
                record: Singer record data
                dn: Distinguished Name for the entry
                object_classes: Object classes for the entry
                attribute_mapping: Optional mapping from record keys to LDIF attributes

            Returns:
                FlextCore.Result[str]: LDIF entry or error

            """
            if not record or not dn:
                return FlextCore.Result[str].fail("Record and DN are required")

            try:
                ldif_lines = []
                mapping = attribute_mapping or {}

                # Add DN
                ldif_lines.append(f"dn: {dn}")

                # Add object classes
                if object_classes:
                    ldif_lines.extend(f"objectClass: {oc}" for oc in object_classes)

                # Add attributes
                for key, value in record.items():
                    if value is None:
                        continue  # Skip null values

                    # Get LDIF attribute name (use mapping or original key)
                    ldif_attr = mapping.get(key, key)

                    # Convert value to LDIF format
                    if isinstance(value, list):
                        # Multi-value attribute
                        for item in value:
                            if item is not None:
                                ldif_value = FlextTargetLdifUtilities.LdifDataProcessing.format_ldif_value(
                                    str(item)
                                )
                                ldif_lines.append(f"{ldif_attr}: {ldif_value}")
                    else:
                        # Single-value attribute
                        ldif_value = FlextTargetLdifUtilities.LdifDataProcessing.format_ldif_value(
                            str(value)
                        )
                        ldif_lines.append(f"{ldif_attr}: {ldif_value}")

                # Add empty line to separate entries
                ldif_lines.append("")

                return FlextCore.Result[str].ok("\n".join(ldif_lines))

            except Exception as e:
                return FlextCore.Result[str].fail(
                    f"Error converting to LDIF entry: {e}"
                )

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

            # Check if value needs base64 encoding
            # LDIF requires base64 for values that start with space, colon, or less-than
            # or contain non-printable characters
            if value.startswith((" ", ":", "<")) or any(
                ord(c) < FlextTargetLdifUtilities.ASCII_SPACE
                or ord(c) > FlextTargetLdifUtilities.ASCII_TILDE
                for c in value
            ):
                encoded = base64.b64encode(value.encode("utf-8")).decode("ascii")
                return f":: {encoded}"

            # Handle line wrapping for long values
            if len(value) > FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                return FlextTargetLdifUtilities.LdifDataProcessing.wrap_ldif_line(value)

            return value

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

            lines = []
            remaining = value

            while remaining:
                if len(remaining) <= FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                    lines.append(remaining)
                    break
                # Find a good break point (prefer space)
                break_point = FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH
                if " " in remaining[:break_point]:
                    break_point = remaining[:break_point].rfind(" ")

                lines.append(remaining[:break_point])
                remaining = (
                    " " + remaining[break_point:].lstrip()
                )  # Continuation with space

            return "\n".join(lines)

        @staticmethod
        def validate_ldif_entry(entry: str) -> FlextCore.Result[bool]:
            """Validate LDIF entry format.

            Args:
                entry: LDIF entry to validate

            Returns:
                FlextCore.Result[bool]: Validation result

            """
            if not entry or not entry.strip():
                return FlextCore.Result[bool].fail("LDIF entry cannot be empty")

            lines = entry.strip().split("\n")
            if not lines:
                return FlextCore.Result[bool].fail(
                    "LDIF entry must have at least one line"
                )

            # First line must be DN
            first_line = lines[0].strip()
            if not first_line.startswith("dn:"):
                return FlextCore.Result[bool].fail("LDIF entry must start with DN")

            # Extract DN value
            dn_value = first_line[3:].strip()
            if not dn_value:
                return FlextCore.Result[bool].fail("DN cannot be empty")

            # Validate DN format
            if not FlextTargetLdifUtilities.LdifDataProcessing.validate_dn_format(
                dn_value
            ):
                return FlextCore.Result[bool].fail(f"Invalid DN format: {dn_value}")

            return FlextCore.Result[bool].ok(True)

    class FileUtilities:
        """File handling utilities for LDIF operations."""

        @staticmethod
        def create_ldif_file(
            file_path: str,
            entries: FlextCore.Types.StringList,
            *,
            overwrite: bool = False,
        ) -> FlextCore.Result[str]:
            """Create LDIF file with entries.

            Args:
                file_path: Path to LDIF file
                entries: List of LDIF entries
                overwrite: Whether to overwrite existing file

            Returns:
                FlextCore.Result[str]: Success message or error

            """
            if not file_path or not entries:
                return FlextCore.Result[str].fail("File path and entries are required")

            try:
                path = Path(file_path)

                # Check if file exists and overwrite flag
                if path.exists() and not overwrite:
                    return FlextCore.Result[str].fail(
                        f"File already exists: {file_path}"
                    )

                # Create parent directories if needed
                path.parent.mkdir(parents=True, exist_ok=True)

                # Write LDIF content
                with Path(path).open("w", encoding="utf-8") as f:
                    for entry in entries:
                        f.write(entry)
                        if not entry.endswith("\n"):
                            f.write("\n")

                return FlextCore.Result[str].ok(f"LDIF file created: {file_path}")

            except Exception as e:
                return FlextCore.Result[str].fail(f"Error creating LDIF file: {e}")

        @staticmethod
        def append_to_ldif_file(
            file_path: str,
            entries: FlextCore.Types.StringList,
        ) -> FlextCore.Result[str]:
            """Append entries to existing LDIF file.

            Args:
                file_path: Path to LDIF file
                entries: List of LDIF entries to append

            Returns:
                FlextCore.Result[str]: Success message or error

            """
            if not file_path or not entries:
                return FlextCore.Result[str].fail("File path and entries are required")

            try:
                path = Path(file_path)

                # Create file if it doesn't exist
                if not path.exists():
                    path.parent.mkdir(parents=True, exist_ok=True)

                # Append LDIF content
                with Path(path).open("a", encoding="utf-8") as f:
                    for entry in entries:
                        f.write(entry)
                        if not entry.endswith("\n"):
                            f.write("\n")

                return FlextCore.Result[str].ok(
                    f"Entries appended to LDIF file: {file_path}"
                )

            except Exception as e:
                return FlextCore.Result[str].fail(f"Error appending to LDIF file: {e}")

        @staticmethod
        def validate_ldif_file_path(file_path: str) -> FlextCore.Result[str]:
            """Validate LDIF file path.

            Args:
                file_path: Path to validate

            Returns:
                FlextCore.Result[str]: Validated path or error

            """
            if not file_path or not file_path.strip():
                return FlextCore.Result[str].fail("File path cannot be empty")

            try:
                path = Path(file_path)

                # Check if path is valid
                if not path.name:
                    return FlextCore.Result[str].fail("Invalid file path")

                # Check file extension
                if path.suffix.lower() != ".ldif":
                    return FlextCore.Result[str].fail("File must have .ldif extension")

                # Check if parent directory is writable (if it exists)
                if path.parent.exists() and not path.parent.is_dir():
                    return FlextCore.Result[str].fail("Parent path is not a directory")

                return FlextCore.Result[str].ok(str(path.resolve()))

            except Exception as e:
                return FlextCore.Result[str].fail(f"Invalid file path: {e}")

    class StreamUtilities:
        """Stream processing utilities for Singer targets."""

        @staticmethod
        def calculate_ldif_batch_size(
            record_count: int,
            target_batches: int = 10,
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
        def validate_stream_compatibility(
            stream_name: str,
            schema: FlextCore.Types.Dict,
        ) -> FlextCore.Result[bool]:
            """Validate stream compatibility with LDIF operations.

            Args:
                stream_name: Name of the stream
                schema: Stream schema

            Returns:
                FlextCore.Result[bool]: Validation result

            """
            if not stream_name or not schema:
                return FlextCore.Result[bool].fail(
                    "Stream name and schema are required"
                )

            # Check if schema has required properties
            properties = schema.get("properties", {})
            if not properties:
                return FlextCore.Result[bool].fail("Schema must have properties")

            # Check for DN building capability
            has_dn_field = "dn" in properties
            has_id_fields = any(
                key in properties for key in ["id", "uid", "cn", "username", "email"]
            )

            if not has_dn_field and not has_id_fields:
                return FlextCore.Result[bool].fail(
                    "Schema must have either 'dn' field or identifier fields (id, uid, cn, username, email)"
                )

            return FlextCore.Result[bool].ok(True)

        @staticmethod
        def generate_ldif_stream_metadata(
            stream_name: str,
            record_count: int,
            file_size_bytes: int,
            processing_time: float,
        ) -> FlextCore.Types.Dict:
            """Generate metadata for LDIF stream processing.

            Args:
                stream_name: Name of the stream
                record_count: Number of records processed
                file_size_bytes: Size of generated LDIF file
                processing_time: Time taken for processing

            Returns:
                FlextCore.Types.Dict: Stream metadata

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

    class ConfigValidation:
        """Configuration validation utilities."""

        @staticmethod
        def validate_ldif_target_config(
            config: FlextCore.Types.Dict,
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Validate LDIF target configuration.

            Args:
                config: Configuration dictionary

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Validated config or error

            """
            required_fields = ["output_file"]
            missing_fields = [field for field in required_fields if field not in config]

            if missing_fields:
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    f"Missing required LDIF target fields: {', '.join(missing_fields)}"
                )

            # Validate output file path
            output_file = config["output_file"]
            file_validation = (
                FlextTargetLdifUtilities.FileUtilities.validate_ldif_file_path(
                    output_file
                )
            )
            if file_validation.is_failure:
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    f"Invalid output file: {file_validation.error}"
                )

            # Validate operation mode
            operation_mode = config.get("operation_mode", "append")
            valid_modes = ["append", "overwrite", "create"]
            if operation_mode not in valid_modes:
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    f"Invalid operation mode: {operation_mode}. Valid modes: {', '.join(valid_modes)}"
                )

            # Validate DN template if provided
            if "dn_template" in config:
                dn_template = config["dn_template"]
                if not isinstance(dn_template, str) or not dn_template.strip():
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "DN template must be a non-empty string"
                    )

            # Validate batch size
            batch_size = config.get(
                "batch_size", FlextTargetLdifUtilities.DEFAULT_BATCH_SIZE
            )
            if not isinstance(batch_size, int) or batch_size <= 0:
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    "Batch size must be a positive integer"
                )

            return FlextCore.Result[FlextCore.Types.Dict].ok(config)

        @staticmethod
        def validate_ldif_entry_config(
            config: FlextCore.Types.Dict,
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Validate LDIF entry configuration.

            Args:
                config: Entry configuration

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Validated config or error

            """
            # Validate object classes if provided
            if "object_classes" in config:
                object_classes = config["object_classes"]
                if not isinstance(object_classes, list) or not object_classes:
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "Object classes must be a non-empty list"
                    )

                for oc in object_classes:
                    if not isinstance(oc, str) or not oc.strip():
                        return FlextCore.Result[FlextCore.Types.Dict].fail(
                            "All object classes must be non-empty strings"
                        )

            # Validate attribute mapping if provided
            if "attribute_mapping" in config:
                attribute_mapping = config["attribute_mapping"]
                if not isinstance(attribute_mapping, dict):
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        "Attribute mapping must be a dictionary"
                    )

                for key, value in attribute_mapping.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return FlextCore.Result[FlextCore.Types.Dict].fail(
                            "Attribute mapping keys and values must be strings"
                        )

            return FlextCore.Result[FlextCore.Types.Dict].ok(config)

    class StateManagement:
        """State management utilities for target operations."""

        @staticmethod
        def get_target_state(
            state: FlextCore.Types.Dict, stream_name: str
        ) -> FlextCore.Types.Dict:
            """Get state for a specific target stream.

            Args:
                state: Complete state dictionary
                stream_name: Name of the stream

            Returns:
                FlextCore.Types.Dict: Stream state

            """
            return state.get("bookmarks", {}).get(stream_name, {})

        @staticmethod
        def set_target_state(
            state: FlextCore.Types.Dict,
            stream_name: str,
            stream_state: FlextCore.Types.Dict,
        ) -> FlextCore.Types.Dict:
            """Set state for a specific target stream.

            Args:
                state: Complete state dictionary
                stream_name: Name of the stream
                stream_state: State data for the stream

            Returns:
                FlextCore.Types.Dict: Updated state

            """
            if "bookmarks" not in state:
                state["bookmarks"] = {}

            state["bookmarks"][stream_name] = stream_state
            return state

        @staticmethod
        def create_processing_state(
            stream_name: str,
            records_processed: int,
            file_path: str,
            file_size_bytes: int,
            last_processed_record: FlextCore.Types.Dict | None = None,
        ) -> FlextCore.Types.Dict:
            """Create processing state for target stream.

            Args:
                stream_name: Name of the stream
                records_processed: Number of records processed
                file_path: Path to LDIF file
                file_size_bytes: Size of LDIF file
                last_processed_record: Last processed record for checkpointing

            Returns:
                FlextCore.Types.Dict: Processing state

            """
            state = {
                "stream_name": stream_name,
                "records_processed": records_processed,
                "output_file": file_path,
                "file_size_bytes": file_size_bytes,
                "last_updated": datetime.now(UTC).isoformat(),
                "target_type": "ldif",
            }

            if last_processed_record:
                # Store minimal checkpoint information
                checkpoint_data = {
                    "id": last_processed_record.get("id"),
                    "dn": last_processed_record.get("dn"),
                    "timestamp": last_processed_record.get("_timestamp"),
                }
                state["checkpoint"] = {
                    k: v for k, v in checkpoint_data.items() if v is not None
                }

            return state

        @staticmethod
        def update_processing_progress(
            state: FlextCore.Types.Dict,
            stream_name: str,
            records_count: int,
            file_size_bytes: int,
        ) -> FlextCore.Types.Dict:
            """Update processing progress in state.

            Args:
                state: Current state
                stream_name: Name of the stream
                records_count: Number of records processed in this batch
                file_size_bytes: Current file size

            Returns:
                FlextCore.Types.Dict: Updated state

            """
            stream_state = FlextTargetLdifUtilities.StateManagement.get_target_state(
                state, stream_name
            )

            current_count = stream_state.get("records_processed", 0)
            new_count = current_count + records_count

            updated_stream_state = {
                **stream_state,
                "records_processed": new_count,
                "file_size_bytes": file_size_bytes,
                "last_updated": datetime.now(UTC).isoformat(),
                "batch_count": stream_state.get("batch_count", 0) + 1,
            }

            return FlextTargetLdifUtilities.StateManagement.set_target_state(
                state, stream_name, updated_stream_state
            )

    # Proxy methods for backward compatibility
    @classmethod
    def parse_singer_message(cls, line: str) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Proxy method for SingerUtilities.parse_singer_message()."""
        return cls.SingerUtilities.parse_singer_message(line)

    @classmethod
    def build_ldif_dn(
        cls,
        record: FlextCore.Types.Dict,
        dn_template: str,
        base_dn: str | None = None,
    ) -> FlextCore.Result[str]:
        """Proxy method for LdifDataProcessing.build_ldif_dn()."""
        return cls.LdifDataProcessing.build_ldif_dn(record, dn_template, base_dn)

    @classmethod
    def convert_record_to_ldif_entry(
        cls,
        record: FlextCore.Types.Dict,
        dn: str,
        object_classes: FlextCore.Types.StringList | None = None,
        attribute_mapping: FlextCore.Types.StringDict | None = None,
    ) -> FlextCore.Result[str]:
        """Proxy method for LdifDataProcessing.convert_record_to_ldif_entry()."""
        return cls.LdifDataProcessing.convert_record_to_ldif_entry(
            record, dn, object_classes, attribute_mapping
        )

    @classmethod
    def create_ldif_file(
        cls,
        file_path: str,
        entries: FlextCore.Types.StringList,
        *,
        overwrite: bool = False,
    ) -> FlextCore.Result[str]:
        """Proxy method for FileUtilities.create_ldif_file()."""
        return cls.FileUtilities.create_ldif_file(file_path, entries, overwrite)

    @classmethod
    def validate_ldif_target_config(
        cls, config: FlextCore.Types.Dict
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Proxy method for ConfigValidation.validate_ldif_target_config()."""
        return cls.ConfigValidation.validate_ldif_target_config(config)

    @classmethod
    def get_target_state(
        cls, state: FlextCore.Types.Dict, stream_name: str
    ) -> FlextCore.Types.Dict:
        """Proxy method for StateManagement.get_target_state()."""
        return cls.StateManagement.get_target_state(state, stream_name)

    @classmethod
    def create_processing_state(
        cls,
        stream_name: str,
        records_processed: int,
        file_path: str,
        file_size_bytes: int,
        last_processed_record: FlextCore.Types.Dict | None = None,
    ) -> FlextCore.Types.Dict:
        """Proxy method for StateManagement.create_processing_state()."""
        return cls.StateManagement.create_processing_state(
            stream_name,
            records_processed,
            file_path,
            file_size_bytes,
            last_processed_record,
        )


__all__ = [
    "FlextTargetLdifUtilities",
]
