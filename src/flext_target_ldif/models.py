"""Models for LDIF target operations.

This module provides data models for LDIF target operations.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from typing import Annotated

from flext_core import (
    FlextSettings,
    r,
)
from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels
from pydantic import Field

from flext_target_ldif import c, t

"""LDIF target models extending flext-core FlextModels.

Provides complete models for LDIF file export, Singer protocol
compliance, format validation, and target operations following standardized patterns.
"""


class FlextTargetLdifModels(FlextMeltanoModels, FlextLdifModels):
    """Unified models collection for FLEXT Target LDIF following [Project]Models standard.

    This class extends FlextMeltanoModels and FlextLdifModels and provides a centralized
    access point for all LDIF target-related model classes, ensuring consistency with
    the FLEXT ecosystem patterns and enabling reusable model composition across the project.

    Model Categories:
    - Configuration: LDIF format and export configuration models
    - Entities: Core LDIF data structures and business entities
    - Processing: Batch processing and transformation models
    - Results: Operation results and error context models
    """

    class Ldif(FlextLdifModels.Ldif):
        """LDIF domain model namespace."""

        class LdifFormatOptions(FlextSettings):
            """LDIF format configuration with specification compliance."""

            line_length: Annotated[
                t.PositiveInt,
                Field(
                    default=c.STANDARD_LINE_LENGTH,
                    description="Maximum LDIF line length",
                ),
            ]
            fold_lines: Annotated[
                bool,
                Field(
                    default=True,
                    description="Enable line folding for long lines",
                ),
            ]
            base64_encode: Annotated[
                bool,
                Field(
                    default=False,
                    description="Force base64 encoding for all attributes",
                ),
            ]
            include_version: Annotated[
                bool,
                Field(
                    default=True,
                    description="Include LDIF version header",
                ),
            ]
            encoding: Annotated[
                str,
                Field(
                    default="utf-8",
                    description="Character encoding for LDIF files",
                ),
            ]
            line_separator: Annotated[
                str, Field(default="\n", description="Line separator character")
            ]

        class LdifExportConfig(FlextSettings):
            """LDIF export configuration with file management."""

            output_path: Annotated[
                str, Field(..., description="Output directory for LDIF files")
            ]
            file_naming_pattern: Annotated[
                str,
                Field(
                    default="{stream_name}.ldif",
                    description="File naming pattern template",
                ),
            ]
            dn_template: Annotated[
                str,
                Field(
                    ...,
                    description="DN template for generating LDIF entry DNs",
                ),
            ]
            attribute_mappings: Annotated[
                t.StrMapping,
                Field(
                    default_factory=dict,
                    description="Singer field to LDIF attribute mappings",
                ),
            ]
            object_classes: Annotated[
                t.StrSequence,
                Field(
                    default_factory=list,
                    description="Default LDAP t.NormalizedValue classes for entries",
                ),
            ]

            # File management options
            overwrite_existing: Annotated[
                bool,
                Field(
                    default=False,
                    description="Overwrite existing LDIF files",
                ),
            ]
            create_directories: Annotated[
                bool,
                Field(
                    default=True,
                    description="Create output directories if they don't exist",
                ),
            ]
            compress_output: Annotated[
                bool,
                Field(
                    default=False,
                    description="Compress LDIF files with gzip",
                ),
            ]

            # Format configuration
            format_options: Annotated[
                LdifFormatOptions,
                Field(
                    default_factory=lambda: LdifFormatOptions.model_validate({}),
                    description="LDIF format options",
                ),
            ]

        class LdifEntry(FlextMeltanoModels.Entity):
            """LDIF entry representation with format validation."""

            distinguished_name: Annotated[
                t.NonEmptyStr,
                Field(
                    ...,
                    description="LDIF Distinguished Name (DN)",
                ),
            ]
            attributes: Annotated[
                Mapping[str, t.StrSequence],
                Field(
                    default_factory=dict,
                    description="LDIF attributes with values",
                ),
            ]
            object_classes: Annotated[
                t.StrSequence,
                Field(
                    default_factory=list,
                    description="LDAP t.NormalizedValue classes",
                ),
            ]
            change_type: Annotated[
                str | None,
                Field(
                    None,
                    description="LDIF change type (add, modify, delete, modrdn)",
                ),
            ]
            controls: Annotated[
                t.StrSequence,
                Field(
                    default_factory=list,
                    description="LDAP controls for the entry",
                ),
            ]

            def validate_business_rules(self) -> r[bool]:
                """Validate LDIF entry business rules."""
                try:
                    errors: list[str] = []

                    # Validate DN format
                    if (
                        "=" not in self.distinguished_name
                        or "," not in self.distinguished_name
                    ):
                        errors.append(
                            "DN must contain attribute=value pairs separated by commas",
                        )

                    # Validate t.NormalizedValue classes
                    if not self.object_classes:
                        errors.append(
                            "Entry must have at least one t.NormalizedValue class"
                        )

                    # Validate attributes exist
                    if not self.attributes:
                        errors.append("Entry must have at least one attribute")

                    if errors:
                        return r[bool].fail("; ".join(errors))
                    return r[bool].ok(value=True)
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as e:
                    return r[bool].fail(f"LDIF entry validation failed: {e}")

        class LdifFile(FlextMeltanoModels.Entity):
            """LDIF file representation with metadata."""

            file_path: Annotated[
                t.NonEmptyStr, Field(..., description="Path to the LDIF file")
            ]
            stream_name: Annotated[
                t.NonEmptyStr, Field(..., description="Singer stream name")
            ]
            entries: Annotated[
                Sequence[LdifEntry],
                Field(
                    default_factory=list,
                    description="LDIF entries in the file",
                ),
            ]
            format_options: Annotated[
                LdifFormatOptions,
                Field(
                    ...,
                    description="Format options used for the file",
                ),
            ]

            # File metadata
            file_size_bytes: Annotated[
                t.NonNegativeInt, Field(default=0, description="File size in bytes")
            ]
            entry_count: Annotated[
                t.NonNegativeInt,
                Field(default=0, description="Number of entries in file"),
            ]
            is_compressed: Annotated[
                bool, Field(default=False, description="Whether file is compressed")
            ]

            def validate_business_rules(self) -> r[bool]:
                """Validate LDIF file business rules."""
                try:
                    # Validate file path
                    if not self.file_path.strip():
                        return r[bool].fail("File path cannot be empty")

                    # Validate entry count matches actual entries
                    if len(self.entries) != self.entry_count:
                        return r[bool].fail(
                            f"Entry count mismatch: {len(self.entries)} vs {self.entry_count}",
                        )

                    return r[bool].ok(value=True)
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as e:
                    return r[bool].fail(f"LDIF file validation failed: {e}")

        class LdifTransformationResult(FlextMeltanoModels.Entity):
            """Result of Singer to LDIF transformation."""

            original_record: Annotated[
                Mapping[str, t.ContainerValue],
                Field(
                    ...,
                    description="Original Singer record",
                ),
            ]
            transformed_entry: Annotated[
                LdifEntry,
                Field(
                    ...,
                    description="Resulting LDIF entry",
                ),
            ]
            transformation_errors: Annotated[
                t.StrSequence,
                Field(
                    default_factory=list,
                    description="Transformation errors",
                ),
            ]
            processing_time_ms: Annotated[
                t.NonNegativeFloat,
                Field(
                    default=0.0,
                    description="Processing time in milliseconds",
                ),
            ]
            transformation_timestamp: Annotated[
                datetime,
                Field(
                    default_factory=lambda: datetime.now(UTC),
                    description="Transformation timestamp",
                ),
            ]

            @property
            def has_errors(self) -> bool:
                """Check if transformation has any errors."""
                return bool(self.transformation_errors)

            @property
            def success_rate(self) -> float:
                """Calculate transformation success rate."""
                return 0.0 if self.has_errors else 100.0

            def validate_business_rules(self) -> r[bool]:
                """Validate transformation result business rules."""
                try:
                    if not self.original_record:
                        return r[bool].fail("Original record cannot be empty")

                    # Validate transformed entry
                    entry_validation = self.transformed_entry.validate_business_rules()
                    if entry_validation.is_failure:
                        return r[bool].fail(
                            f"Transformed entry is invalid: {entry_validation.error}",
                        )

                    return r[bool].ok(value=True)
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as e:
                    return r[bool].fail(
                        f"Transformation result validation failed: {e}",
                    )

        class LdifBatchProcessing(FlextMeltanoModels.Entity):
            """LDIF batch processing configuration and state."""

            stream_name: Annotated[
                t.NonEmptyStr, Field(..., description="Singer stream name")
            ]
            batch_size: Annotated[
                t.BatchSize,
                Field(
                    default=c.DEFAULT_BATCH_SIZE,
                    description="Records per batch",
                ),
            ]
            current_batch: Annotated[
                Sequence[LdifEntry],
                Field(
                    default_factory=list,
                    description="Current batch of entries",
                ),
            ]
            total_processed: Annotated[
                t.NonNegativeInt,
                Field(default=0, description="Total entries processed"),
            ]
            successful_exports: Annotated[
                t.NonNegativeInt, Field(default=0, description="Successful exports")
            ]
            failed_exports: Annotated[
                t.NonNegativeInt, Field(default=0, description="Failed exports")
            ]
            last_processed_at: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Last processing timestamp",
                ),
            ]

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

            def validate_business_rules(self) -> r[bool]:
                """Validate batch processing business rules."""
                try:
                    if len(self.current_batch) > self.batch_size:
                        return r[bool].fail(
                            f"Current batch size exceeds maximum: {len(self.current_batch)} > {self.batch_size}",
                        )

                    if (
                        self.successful_exports + self.failed_exports
                        > self.total_processed
                    ):
                        return r[bool].fail("Export counts exceed total processed")

                    return r[bool].ok(value=True)
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as e:
                    return r[bool].fail(f"Batch processing validation failed: {e}")

        class SingerStreamConfig(FlextSettings):
            """Singer stream configuration for LDIF export."""

            stream_name: Annotated[
                t.NonEmptyStr, Field(..., description="Singer stream name")
            ]
            ldif_config: Annotated[
                LdifExportConfig,
                Field(
                    ...,
                    description="LDIF export configuration",
                ),
            ]
            batch_size: Annotated[
                t.BatchSize,
                Field(
                    default=c.DEFAULT_BATCH_SIZE,
                    description="Batch size for processing",
                ),
            ]
            enable_validation: Annotated[
                bool,
                Field(
                    default=True,
                    description="Enable LDIF format validation",
                ),
            ]

        class LdifTargetResult(FlextMeltanoModels.Entity):
            """Result of LDIF target operation processing."""

            stream_name: Annotated[
                t.NonEmptyStr, Field(..., description="Singer stream name")
            ]
            output_files: Annotated[
                t.StrSequence,
                Field(
                    default_factory=list,
                    description="Generated LDIF file paths",
                ),
            ]
            records_processed: Annotated[
                t.NonNegativeInt,
                Field(
                    default=0,
                    description="Total records processed",
                ),
            ]
            entries_exported: Annotated[
                t.NonNegativeInt,
                Field(default=0, description="LDIF entries exported"),
            ]
            entries_failed: Annotated[
                t.NonNegativeInt,
                Field(
                    default=0,
                    description="Entries that failed export",
                ),
            ]

            # File statistics
            total_file_size_bytes: Annotated[
                t.NonNegativeInt,
                Field(
                    default=0,
                    description="Total size of generated files",
                ),
            ]
            files_compressed: Annotated[
                t.NonNegativeInt,
                Field(
                    default=0,
                    description="Number of compressed files",
                ),
            ]

            # Performance metrics
            total_duration_ms: Annotated[
                t.NonNegativeFloat,
                Field(
                    default=0.0,
                    description="Total processing duration",
                ),
            ]
            average_processing_time_ms: Annotated[
                t.NonNegativeFloat,
                Field(
                    default=0.0,
                    description="Average processing time per record",
                ),
            ]

            # Error tracking
            error_messages: Annotated[
                t.StrSequence,
                Field(
                    default_factory=list,
                    description="Error messages encountered",
                ),
            ]
            warnings: Annotated[
                t.StrSequence,
                Field(default_factory=list, description="Warning messages"),
            ]

            @property
            def failure_rate(self) -> float:
                """Calculate failure rate percentage."""
                if self.records_processed == 0:
                    return 0.0
                return (self.entries_failed / self.records_processed) * 100.0

            @property
            def success_rate(self) -> float:
                """Calculate success rate percentage."""
                if self.records_processed == 0:
                    return 0.0
                return (self.entries_exported / self.records_processed) * 100.0

            def validate_business_rules(self) -> r[bool]:
                """Validate LDIF target result business rules."""
                try:
                    # Validate entry counts
                    total_entries = self.entries_exported + self.entries_failed
                    if total_entries > self.records_processed:
                        return r[bool].fail(
                            "Total entries cannot exceed records processed",
                        )

                    # Validate file count
                    if not self.output_files and self.entries_exported > 0:
                        return r[bool].fail(
                            "No output files but entries were exported",
                        )

                    return r[bool].ok(value=True)
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as e:
                    return r[bool].fail(f"Target result validation failed: {e}")

        class LdifErrorContext(FlextMeltanoModels.ArbitraryTypesModel):
            """Error context for LDIF target error handling."""

            error_type: Annotated[
                t.NonEmptyStr, Field(..., description="Error category")
            ]

            # Context information
            file_path: Annotated[
                str | None, Field(None, description="File path that caused error")
            ]
            entry_dn: Annotated[
                str | None, Field(None, description="DN of entry causing error")
            ]
            attribute_name: Annotated[
                str | None, Field(None, description="Attribute causing error")
            ]
            stream_name: Annotated[
                str | None, Field(None, description="Singer stream name")
            ]
            line_number: Annotated[
                int | None, Field(None, description="Line number in LDIF file")
            ]

            # Recovery information
            is_retryable: Annotated[
                bool, Field(default=False, description="Whether error is retryable")
            ]
            suggested_action: Annotated[
                str | None, Field(None, description="Suggested recovery action")
            ]
            max_retry_attempts: Annotated[
                int | None, Field(None, description="Maximum retry attempts")
            ]


# Short aliases
m = FlextTargetLdifModels

__all__ = ["FlextTargetLdifModels", "m"]
