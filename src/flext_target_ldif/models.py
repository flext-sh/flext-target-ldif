"""Models for LDIF target operations.

This module provides data models for LDIF target operations.
"""

from __future__ import annotations

from datetime import UTC, datetime

from flext_core import FlextCore
from pydantic import ConfigDict, Field

# LDIF target constants
FORMAT_VALIDATION = "FORMAT_VALIDATION"
FILE_IO = "FILE_IO"
TRANSFORMATION = "TRANSFORMATION"
SINGER_PROTOCOL = "SINGER_PROTOCOL"
CONFIGURATION = "CONFIGURATION"
DISK_SPACE = "DISK_SPACE"
PERMISSION = "PERMISSION"
ENCODING = "ENCODING"

"""LDIF target models extending flext-core FlextCore.Models.

Provides comprehensive models for LDIF file export, Singer protocol
compliance, format validation, and target operations following standardized patterns.
"""


class LdifFormatOptions(FlextCore.Config):
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


class LdifExportConfig(FlextCore.Config):
    """LDIF export configuration with file management."""

    output_path: str = Field(..., description="Output directory for LDIF files")
    file_naming_pattern: str = Field(
        default="{stream_name}.ldif", description="File naming pattern template"
    )
    dn_template: str = Field(
        ..., description="DN template for generating LDIF entry DNs"
    )
    attribute_mappings: FlextCore.Types.StringDict = Field(
        default_factory=dict, description="Singer field to LDIF attribute mappings"
    )
    object_classes: FlextCore.Types.StringList = Field(
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


class LdifEntry(FlextCore.Models.Entity):
    """LDIF entry representation with format validation."""

    distinguished_name: str = Field(
        ..., description="LDIF Distinguished Name (DN)", min_length=1, max_length=1000
    )
    attributes: dict[str, FlextCore.Types.StringList] = Field(
        default_factory=dict, description="LDIF attributes with values"
    )
    object_classes: FlextCore.Types.StringList = Field(
        default_factory=list, description="LDAP object classes"
    )
    change_type: str | None = Field(
        None, description="LDIF change type (add, modify, delete, modrdn)"
    )
    controls: FlextCore.Types.StringList = Field(
        default_factory=list, description="LDAP controls for the entry"
    )

    def validate_business_rules(self) -> FlextCore.Result[None]:
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
                return FlextCore.Result[None].fail("; ".join(errors))
            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"LDIF entry validation failed: {e}")


class LdifFile(FlextCore.Models.Entity):
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

    def validate_business_rules(self) -> FlextCore.Result[None]:
        """Validate LDIF file business rules."""
        try:
            # Validate file path
            if not self.file_path.strip():
                return FlextCore.Result[None].fail("File path cannot be empty")

            # Validate entry count matches actual entries
            if len(self.entries) != self.entry_count:
                return FlextCore.Result[None].fail(
                    f"Entry count mismatch: {len(self.entries)} vs {self.entry_count}"
                )

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"LDIF file validation failed: {e}")


class LdifTransformationResult(FlextCore.Models.Entity):
    """Result of Singer to LDIF transformation."""

    original_record: FlextCore.Types.Dict = Field(
        ..., description="Original Singer record"
    )
    transformed_entry: FlextTargetLdifModels.LdifEntry = Field(
        ..., description="Resulting LDIF entry"
    )
    transformation_errors: FlextCore.Types.StringList = Field(
        default_factory=list, description="Transformation errors"
    )
    processing_time_ms: float = Field(
        default=0.0, ge=0.0, description="Processing time in milliseconds"
    )
    transformation_timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Transformation timestamp",
    )

    def validate_business_rules(self) -> FlextCore.Result[None]:
        """Validate transformation result business rules."""
        try:
            if not self.original_record:
                return FlextCore.Result[None].fail("Original record cannot be empty")

            # Validate transformed entry
            entry_validation = self.transformed_entry.validate_business_rules()
            if entry_validation.is_failure:
                return FlextCore.Result[None].fail(
                    f"Transformed entry is invalid: {entry_validation.error}"
                )

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(
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


class LdifBatchProcessing(FlextCore.Models.Entity):
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

    def validate_business_rules(self) -> FlextCore.Result[None]:
        """Validate batch processing business rules."""
        try:
            if len(self.current_batch) > self.batch_size:
                return FlextCore.Result[None].fail(
                    f"Current batch size exceeds maximum: {len(self.current_batch)} > {self.batch_size}"
                )

            if self.successful_exports + self.failed_exports > self.total_processed:
                return FlextCore.Result[None].fail(
                    "Export counts exceed total processed"
                )

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(
                f"Batch processing validation failed: {e}"
            )

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


class SingerStreamConfig(FlextCore.Config):
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


class LdifTargetResult(FlextCore.Models.Entity):
    """Result of LDIF target operation processing."""

    stream_name: str = Field(..., description="Singer stream name")
    output_files: FlextCore.Types.StringList = Field(
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
    error_messages: FlextCore.Types.StringList = Field(
        default_factory=list, description="Error messages encountered"
    )
    warnings: FlextCore.Types.StringList = Field(
        default_factory=list, description="Warning messages"
    )

    def validate_business_rules(self) -> FlextCore.Result[None]:
        """Validate LDIF target result business rules."""
        try:
            # Validate entry counts
            total_entries = self.entries_exported + self.entries_failed
            if total_entries > self.records_processed:
                return FlextCore.Result[None].fail(
                    "Total entries cannot exceed records processed"
                )

            # Validate file count
            if len(self.output_files) == 0 and self.entries_exported > 0:
                return FlextCore.Result[None].fail(
                    "No output files but entries were exported"
                )

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Target result validation failed: {e}")

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


class LdifErrorContext(FlextCore.Models.StrictArbitraryTypesModel):
    """Error context for LDIF target error handling."""

    error_type: Literal[
        FORMAT_VALIDATION,
        FILE_IO,
        TRANSFORMATION,
        SINGER_PROTOCOL,
        CONFIGURATION,
        DISK_SPACE,
        PERMISSION,
        ENCODING,
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
LdifRecord = FlextCore.Types.Dict
LdifRecords = list[LdifRecord]


class FlextTargetLdifModels(FlextCore.Models):
    """Unified models collection for FLEXT Target LDIF following [Project]Models standard.

    This class extends FlextCore.Models and provides a centralized access point for all
    LDIF target-related model classes, ensuring consistency with the FLEXT ecosystem
    patterns and enabling reusable model composition across the project.

    Model Categories:
    - Configuration: LDIF format and export configuration models
    - Entities: Core LDIF data structures and business entities
    - Processing: Batch processing and transformation models
    - Results: Operation results and error context models
    """

    model_config = ConfigDict(
        validate_assignment=True,
        validate_return=True,
        validate_default=True,
        use_enum_values=True,
        arbitrary_types_allowed=True,
        extra="forbid",
        frozen=False,
        strict=True,
        str_strip_whitespace=True,
        ser_json_timedelta="iso8601",
        ser_json_bytes="base64",
        hide_input_in_errors=True,
    )

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


# ZERO TOLERANCE CONSOLIDATION - FlextTargetLdifUtilities moved to utilities.py
#
# CRITICAL: FlextTargetLdifUtilities was DUPLICATED between models.py and utilities.py.
# This was a ZERO TOLERANCE violation of the user's explicit requirements.
#
# RESOLUTION: Import from utilities.py to eliminate duplication completely.

from typing import Literal

from flext_target_ldif.utilities import FlextTargetLdifUtilities

# Note: This import ensures backward compatibility while eliminating duplication


# Export the unified models class
__all__ = [
    "FlextTargetLdifModels",  # Unified models class
    "FlextTargetLdifUtilities",  # Standardized [Project]Utilities pattern
]
