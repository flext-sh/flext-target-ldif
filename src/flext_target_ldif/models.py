"""Models for LDIF target operations.

This module provides data models for LDIF target operations.
"""

from __future__ import annotations

import pathlib
from datetime import UTC, datetime
from typing import Any, Literal

from pydantic import Field

from flext_core import FlextConfig, FlextModels, FlextResult

"""LDIF target models extending flext-core FlextModels.

Provides comprehensive models for LDIF file export, Singer protocol
compliance, format validation, and target operations following standardized patterns.
"""


class LdifFormatOptions(FlextConfig):
    """LDIF format configuration with specification compliance."""

    line_length: int = Field(
        default=78, ge=40, le=200, description="Maximum LDIF line length"
    )
    fold_lines: bool = Field(
        default=True, description="Enable line folding for long lines"
    )
    base64_encode: bool = Field(
        default=False, description="Force base64 encoding for all attributes"
    )
    include_version: bool = Field(
        default=True, description="Include LDIF version header"
    )
    encoding: str = Field(
        default="utf-8", description="Character encoding for LDIF files"
    )
    line_separator: str = Field(default="\n", description="Line separator character")


class LdifExportConfig(FlextConfig):
    """LDIF export configuration with file management."""

    output_path: str = Field(..., description="Output directory for LDIF files")
    file_naming_pattern: str = Field(
        default="{stream_name}.ldif", description="File naming pattern template"
    )
    dn_template: str = Field(
        ..., description="DN template for generating LDIF entry DNs"
    )
    attribute_mappings: dict[str, str] = Field(
        default_factory=dict, description="Singer field to LDIF attribute mappings"
    )
    object_classes: list[str] = Field(
        default_factory=list, description="Default LDAP object classes for entries"
    )

    # File management options
    overwrite_existing: bool = Field(
        default=False, description="Overwrite existing LDIF files"
    )
    create_directories: bool = Field(
        default=True, description="Create output directories if they don't exist"
    )
    compress_output: bool = Field(
        default=False, description="Compress LDIF files with gzip"
    )

    # Format configuration
    format_options: FlextTargetLdifModels.LdifFormatOptions = Field(
        default_factory=LdifFormatOptions, description="LDIF format options"
    )


class LdifEntry(FlextModels.Entity):
    """LDIF entry representation with format validation."""

    distinguished_name: str = Field(
        ..., description="LDIF Distinguished Name (DN)", min_length=1, max_length=1000
    )
    attributes: dict[str, list[str]] = Field(
        default_factory=dict, description="LDIF attributes with values"
    )
    object_classes: list[str] = Field(
        default_factory=list, description="LDAP object classes"
    )
    change_type: str | None = Field(
        None, description="LDIF change type (add, modify, delete, modrdn)"
    )
    controls: list[str] = Field(
        default_factory=list, description="LDAP controls for the entry"
    )

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate LDIF entry business rules."""
        try:
            errors = []

            # Validate DN format
            if "=" not in self.distinguished_name or "," not in self.distinguished_name:
                errors.append(
                    "DN must contain attribute=value pairs separated by commas"
                )

            # Validate object classes
            if not self.object_classes:
                errors.append("Entry must have at least one object class")

            # Validate attributes exist
            if not self.attributes:
                errors.append("Entry must have at least one attribute")

            if errors:
                return FlextResult[None].fail("; ".join(errors))
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"LDIF entry validation failed: {e}")

    def to_ldif_string(self) -> str:
        """Convert entry to LDIF string format."""
        lines = [f"dn: {self.distinguished_name}"]

        # Add object classes
        lines.extend(f"objectClass: {oc}" for oc in self.object_classes)

        # Add attributes
        for attr_name, attr_values in self.attributes.items():
            lines.extend(f"{attr_name}: {value}" for value in attr_values)

        # Add change type if specified
        if self.change_type:
            lines.append(f"changetype: {self.change_type}")

        lines.append("")  # Empty line after entry
        return "\n".join(lines)


class LdifFile(FlextModels.Entity):
    """LDIF file representation with metadata."""

    file_path: str = Field(..., description="Path to the LDIF file")
    stream_name: str = Field(..., description="Singer stream name")
    entries: list[FlextTargetLdifModels.LdifEntry] = Field(
        default_factory=list, description="LDIF entries in the file"
    )
    format_options: FlextTargetLdifModels.LdifFormatOptions = Field(
        ..., description="Format options used for the file"
    )

    # File metadata
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC), description="File creation timestamp"
    )
    file_size_bytes: int = Field(default=0, ge=0, description="File size in bytes")
    entry_count: int = Field(default=0, ge=0, description="Number of entries in file")
    is_compressed: bool = Field(default=False, description="Whether file is compressed")

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate LDIF file business rules."""
        try:
            # Validate file path
            if not self.file_path.strip():
                return FlextResult[None].fail("File path cannot be empty")

            # Validate entry count matches actual entries
            if len(self.entries) != self.entry_count:
                return FlextResult[None].fail(
                    f"Entry count mismatch: {len(self.entries)} vs {self.entry_count}"
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"LDIF file validation failed: {e}")


class LdifTransformationResult(FlextModels.Entity):
    """Result of Singer to LDIF transformation."""

    original_record: dict[str, Any] = Field(..., description="Original Singer record")
    transformed_entry: FlextTargetLdifModels.LdifEntry = Field(
        ..., description="Resulting LDIF entry"
    )
    transformation_errors: list[str] = Field(
        default_factory=list, description="Transformation errors"
    )
    processing_time_ms: float = Field(
        default=0.0, ge=0.0, description="Processing time in milliseconds"
    )
    transformation_timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Transformation timestamp",
    )

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate transformation result business rules."""
        try:
            if not self.original_record:
                return FlextResult[None].fail("Original record cannot be empty")

            # Validate transformed entry
            entry_validation = self.transformed_entry.validate_business_rules()
            if entry_validation.is_failure:
                return FlextResult[None].fail(
                    f"Transformed entry is invalid: {entry_validation.error}"
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(
                f"Transformation result validation failed: {e}"
            )

    @property
    def has_errors(self) -> bool:
        """Check if transformation has any errors."""
        return bool(self.transformation_errors)

    @property
    def success_rate(self) -> float:
        """Calculate transformation success rate."""
        return 0.0 if self.has_errors else 100.0


class LdifBatchProcessing(FlextModels.Entity):
    """LDIF batch processing configuration and state."""

    stream_name: str = Field(..., description="Singer stream name")
    batch_size: int = Field(
        default=1000, ge=1, le=10000, description="Records per batch"
    )
    current_batch: list[FlextTargetLdifModels.LdifEntry] = Field(
        default_factory=list, description="Current batch of entries"
    )
    total_processed: int = Field(default=0, ge=0, description="Total entries processed")
    successful_exports: int = Field(default=0, ge=0, description="Successful exports")
    failed_exports: int = Field(default=0, ge=0, description="Failed exports")
    last_processed_at: datetime | None = Field(
        None, description="Last processing timestamp"
    )

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate batch processing business rules."""
        try:
            if len(self.current_batch) > self.batch_size:
                return FlextResult[None].fail(
                    f"Current batch size exceeds maximum: {len(self.current_batch)} > {self.batch_size}"
                )

            if self.successful_exports + self.failed_exports > self.total_processed:
                return FlextResult[None].fail("Export counts exceed total processed")

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Batch processing validation failed: {e}")

    @property
    def is_batch_full(self) -> bool:
        """Check if current batch is full."""
        return len(self.current_batch) >= self.batch_size

    @property
    def success_rate(self) -> float:
        """Calculate success rate percentage."""
        total = self.successful_exports + self.failed_exports
        if total == 0:
            return 0.0
        return (self.successful_exports / total) * 100.0


class SingerStreamConfig(FlextConfig):
    """Singer stream configuration for LDIF export."""

    stream_name: str = Field(..., description="Singer stream name")
    ldif_config: FlextTargetLdifModels.LdifExportConfig = Field(
        ..., description="LDIF export configuration"
    )
    batch_size: int = Field(
        default=1000, ge=1, le=10000, description="Batch size for processing"
    )
    enable_validation: bool = Field(
        default=True, description="Enable LDIF format validation"
    )


class LdifTargetResult(FlextModels.Entity):
    """Result of LDIF target operation processing."""

    stream_name: str = Field(..., description="Singer stream name")
    output_files: list[str] = Field(
        default_factory=list, description="Generated LDIF file paths"
    )
    records_processed: int = Field(
        default=0, ge=0, description="Total records processed"
    )
    entries_exported: int = Field(default=0, ge=0, description="LDIF entries exported")
    entries_failed: int = Field(
        default=0, ge=0, description="Entries that failed export"
    )

    # File statistics
    total_file_size_bytes: int = Field(
        default=0, ge=0, description="Total size of generated files"
    )
    files_compressed: int = Field(
        default=0, ge=0, description="Number of compressed files"
    )

    # Performance metrics
    total_duration_ms: float = Field(
        default=0.0, ge=0.0, description="Total processing duration"
    )
    average_processing_time_ms: float = Field(
        default=0.0, ge=0.0, description="Average processing time per record"
    )

    # Error tracking
    error_messages: list[str] = Field(
        default_factory=list, description="Error messages encountered"
    )
    warnings: list[str] = Field(default_factory=list, description="Warning messages")

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate LDIF target result business rules."""
        try:
            # Validate entry counts
            total_entries = self.entries_exported + self.entries_failed
            if total_entries > self.records_processed:
                return FlextResult[None].fail(
                    "Total entries cannot exceed records processed"
                )

            # Validate file count
            if len(self.output_files) == 0 and self.entries_exported > 0:
                return FlextResult[None].fail(
                    "No output files but entries were exported"
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Target result validation failed: {e}")

    @property
    def success_rate(self) -> float:
        """Calculate success rate percentage."""
        if self.records_processed == 0:
            return 0.0
        return (self.entries_exported / self.records_processed) * 100.0

    @property
    def failure_rate(self) -> float:
        """Calculate failure rate percentage."""
        if self.records_processed == 0:
            return 0.0
        return (self.entries_failed / self.records_processed) * 100.0


class LdifErrorContext(FlextModels.BaseModel):
    """Error context for LDIF target error handling."""

    error_type: Literal[
        "FORMAT_VALIDATION",
        "FILE_IO",
        "TRANSFORMATION",
        "SINGER_PROTOCOL",
        "CONFIGURATION",
        "DISK_SPACE",
        "PERMISSION",
        "ENCODING",
    ] = Field(..., description="Error category")

    # Context information
    file_path: str | None = Field(None, description="File path that caused error")
    entry_dn: str | None = Field(None, description="DN of entry causing error")
    attribute_name: str | None = Field(None, description="Attribute causing error")
    stream_name: str | None = Field(None, description="Singer stream name")
    line_number: int | None = Field(None, description="Line number in LDIF file")

    # Recovery information
    is_retryable: bool = Field(default=False, description="Whether error is retryable")
    suggested_action: str | None = Field(None, description="Suggested recovery action")
    max_retry_attempts: int | None = Field(None, description="Maximum retry attempts")


# Type aliases for backward compatibility
LdifRecord = dict[str, Any]
LdifRecords = list[LdifRecord]


class FlextTargetLdifModels(FlextModels):
    """Unified models collection for FLEXT Target LDIF following [Project]Models standard.

    This class extends FlextModels and provides a centralized access point for all
    LDIF target-related model classes, ensuring consistency with the FLEXT ecosystem
    patterns and enabling reusable model composition across the project.

    Model Categories:
    - Configuration: LDIF format and export configuration models
    - Entities: Core LDIF data structures and business entities
    - Processing: Batch processing and transformation models
    - Results: Operation results and error context models
    """

    # Configuration models
    LdifFormatOptions = LdifFormatOptions
    LdifExportConfig = LdifExportConfig
    SingerStreamConfig = SingerStreamConfig

    # Entity models
    LdifEntry = LdifEntry
    LdifFile = LdifFile

    # Processing models
    LdifTransformationResult = LdifTransformationResult
    LdifBatchProcessing = LdifBatchProcessing

    # Result models
    LdifTargetResult = LdifTargetResult
    LdifErrorContext = LdifErrorContext


class FlextTargetLdifUtilities(FlextUtilities):
    """Standardized utilities for FLEXT Target LDIF operations.

    Provides comprehensive utility functions for LDIF target operations including
    Singer target configuration, LDIF file generation, data transformation,
    and validation helpers following FLEXT patterns.
    """

    class _LdifTargetHelper:
        """Helper for Singer target LDIF operations."""

        @staticmethod
        def validate_target_config(config: dict) -> FlextResult[dict]:
            """Validate Singer target configuration for LDIF operations."""
            if not config:
                return FlextResult[dict].fail("Target configuration cannot be empty")

            required_fields = ["output_path", "ldif_format"]
            for field in required_fields:
                if field not in config:
                    return FlextResult[dict].fail(f"Missing required field: {field}")

            return FlextResult[dict].ok(config)

        @staticmethod
        def create_ldif_sink_config(
            output_path: str, format_options: dict | None = None
        ) -> FlextResult[dict]:
            """Create LDIF sink configuration for Singer target."""
            if not output_path:
                return FlextResult[dict].fail("Output path is required")

            config = {
                "output_path": output_path,
                "ldif_format": format_options
                or {
                    "line_separator": "\\n",
                    "wrap_length": 78,
                    "include_version": True,
                },
                "batch_size": 1000,
                "create_directories": True,
            }

            return FlextResult[dict].ok(config)

    class _LdifFileGenerationHelper:
        """Helper for LDIF file generation and formatting."""

        @staticmethod
        def generate_ldif_entry(record: dict, dn_template: str) -> FlextResult[str]:
            """Generate LDIF entry from Singer record."""
            if not record:
                return FlextResult[str].fail("Record cannot be empty")
            if not dn_template:
                return FlextResult[str].fail("DN template is required")

            try:
                # Generate DN from template
                dn = dn_template.format(**record)

                # Build LDIF entry
                ldif_lines = [f"dn: {dn}"]

                # Add attributes
                for key, value in record.items():
                    if key.startswith("_") or value is None:
                        continue

                    if isinstance(value, list):
                        ldif_lines.extend(f"{key}: {item}" for item in value)
                    else:
                        ldif_lines.append(f"{key}: {value}")

                ldif_lines.append("")  # Empty line separator

                return FlextResult[str].ok("\\n".join(ldif_lines))

            except KeyError as e:
                return FlextResult[str].fail(f"Missing field in DN template: {e}")
            except Exception as e:
                return FlextResult[str].fail(f"LDIF entry generation failed: {e}")

        @staticmethod
        def validate_ldif_format(ldif_content: str) -> FlextResult[list[str]]:
            """Validate LDIF format and return list of entries."""
            if not ldif_content.strip():
                return FlextResult[list[str]].fail("LDIF content cannot be empty")

            try:
                entries = []
                current_entry = []

                for line in ldif_content.split("\\n"):
                    line = line.strip()

                    if not line:  # Empty line indicates end of entry
                        if current_entry:
                            entries.append("\\n".join(current_entry))
                            current_entry = []
                    else:
                        current_entry.append(line)

                # Add last entry if exists
                if current_entry:
                    entries.append("\\n".join(current_entry))

                if not entries:
                    return FlextResult[list[str]].fail("No valid LDIF entries found")

                return FlextResult[list[str]].ok(entries)

            except Exception as e:
                return FlextResult[list[str]].fail(
                    f"LDIF format validation failed: {e}"
                )

    class _SingerTargetIntegrationHelper:
        """Helper for Singer target integration with LDIF processing."""

        @staticmethod
        def process_singer_message(message: dict, config: dict) -> FlextResult[dict]:
            """Process Singer message for LDIF target output."""
            if not message:
                return FlextResult[dict].fail("Singer message cannot be empty")

            message_type = message.get("type")
            if not message_type:
                return FlextResult[dict].fail("Singer message must have type")

            if message_type == "RECORD":
                return FlextTargetLdifUtilities._SingerTargetIntegrationHelper._process_record_message(
                    message, config
                )
            if message_type == "SCHEMA":
                return FlextTargetLdifUtilities._SingerTargetIntegrationHelper._process_schema_message(
                    message, config
                )
            if message_type == "STATE":
                return FlextTargetLdifUtilities._SingerTargetIntegrationHelper._process_state_message(
                    message, config
                )
            return FlextResult[dict].fail(
                f"Unsupported Singer message type: {message_type}"
            )

        @staticmethod
        def _process_record_message(message: dict, config: dict) -> FlextResult[dict]:
            """Process Singer RECORD message for LDIF target."""
            record = message.get("record", {})
            stream = message.get("stream", "unknown")

            # Generate DN template based on stream
            dn_template = config.get("dn_templates", {}).get(
                stream, f"cn={{cn}},ou={stream},dc=example,dc=org"
            )

            # Generate LDIF entry
            ldif_result = (
                FlextTargetLdifUtilities._LdifFileGenerationHelper.generate_ldif_entry(
                    record, dn_template
                )
            )

            if ldif_result.is_failure:
                return FlextResult[dict].fail(
                    f"LDIF generation failed: {ldif_result.error}"
                )

            return FlextResult[dict].ok({
                "type": "ldif_entry",
                "stream": stream,
                "ldif": ldif_result.unwrap(),
                "record": record,
            })

        @staticmethod
        def _process_schema_message(message: dict, config: dict) -> FlextResult[dict]:
            """Process Singer SCHEMA message for LDIF target."""
            schema = message.get("schema", {})
            stream = message.get("stream", "unknown")

            return FlextResult[dict].ok({
                "type": "schema_processed",
                "stream": stream,
                "schema": schema,
            })

        @staticmethod
        def _process_state_message(message: dict, config: dict) -> FlextResult[dict]:
            """Process Singer STATE message for LDIF target."""
            state = message.get("value", {})

            return FlextResult[dict].ok({"type": "state_processed", "state": state})

    @classmethod
    def create_target_config(
        cls,
        output_path: str,
        dn_templates: dict | None = None,
        format_options: dict | None = None,
    ) -> FlextResult[dict]:
        """Create comprehensive LDIF target configuration."""
        config_result = cls._LdifTargetHelper.create_ldif_sink_config(
            output_path, format_options
        )

        if config_result.is_failure:
            return config_result

        config = config_result.unwrap()
        config["dn_templates"] = dn_templates or {}

        return FlextResult[dict].ok(config)

    @classmethod
    def validate_target_environment(cls, config: dict) -> FlextResult[dict]:
        """Validate LDIF target environment and dependencies."""
        validation_result = cls._LdifTargetHelper.validate_target_config(config)
        if validation_result.is_failure:
            return validation_result

        # Additional environment validation
        output_path = config.get("output_path", "")
        if not output_path:
            return FlextResult[dict].fail("Output path not specified")

        # Check if output directory is writable (simplified check)
        output_dir = pathlib.Path(output_path).parent
        if output_dir and not pathlib.Path(output_dir).exists():
            try:
                pathlib.Path(output_dir).mkdir(exist_ok=True, parents=True)
            except Exception as e:
                return FlextResult[dict].fail(f"Cannot create output directory: {e}")

        return FlextResult[dict].ok({
            "environment": "valid",
            "output_path": output_path,
            "writable": True,
        })

    @classmethod
    def process_singer_stream(
        cls, messages: list[dict], config: dict
    ) -> FlextResult[list[str]]:
        """Process complete Singer message stream for LDIF target output."""
        if not messages:
            return FlextResult[list[str]].fail("No Singer messages to process")

        ldif_entries = []

        for message in messages:
            result = cls._SingerTargetIntegrationHelper.process_singer_message(
                message, config
            )

            if result.is_failure:
                return FlextResult[list[str]].fail(
                    f"Message processing failed: {result.error}"
                )

            processed = result.unwrap()
            if processed.get("type") == "ldif_entry":
                ldif_entries.append(processed.get("ldif", ""))

        return FlextResult[list[str]].ok(ldif_entries)


# Export the unified models class
__all__ = [
    "FlextTargetLdifModels",  # Unified models class
    "FlextTargetLdifUtilities",  # Standardized [Project]Utilities pattern
]
