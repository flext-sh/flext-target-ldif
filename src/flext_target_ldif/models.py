"""Models for LDIF target operations.

This module provides data models for LDIF target operations.
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from pathlib import Path
from types import MappingProxyType
from typing import Annotated, override

from flext_core import (
    FlextSettings,
    r,
)
from flext_ldif import FlextLdifModels
from flext_meltano import m
from flext_target_ldif import c, p, t, u
from flext_target_ldif.writer import FlextTargetLdifWriter

"""LDIF target models extending flext-core FlextModels.

Provides complete models for LDIF file export, Singer protocol
compliance, format validation, and target operations following standardized patterns.
"""


class FlextTargetLdifModels(m, FlextLdifModels):
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

    class TargetLdif:
        """TargetLdif domain model namespace."""

        class LdifFormatOptions(FlextSettings):
            """LDIF format configuration with specification compliance."""

            line_length: Annotated[
                t.PositiveInt,
                u.Field(
                    default=c.TargetLdif.STANDARD_LINE_LENGTH,
                    description="Maximum LDIF line length",
                ),
            ]
            fold_lines: Annotated[
                bool,
                u.Field(
                    default=True,
                    description="Enable line folding for long lines",
                ),
            ]
            base64_encode: Annotated[
                bool,
                u.Field(
                    default=False,
                    description="Force base64 encoding for all attributes",
                ),
            ]
            include_version: Annotated[
                bool,
                u.Field(
                    default=True,
                    description="Include LDIF version header",
                ),
            ]
            encoding: Annotated[
                str,
                u.Field(
                    default=c.DEFAULT_ENCODING,
                    description="Character encoding for LDIF files",
                ),
            ]
            line_separator: Annotated[
                str,
                u.Field(default="\n", description="Line separator character"),
            ]

        class LdifEntry(m.Entity):
            """LDIF entry representation with format validation."""

            distinguished_name: Annotated[
                t.NonEmptyStr,
                u.Field(
                    ...,
                    description="LDIF Distinguished Name (DN)",
                ),
            ]
            attributes: Annotated[
                t.MappingKV[str, t.StrSequence],
                u.Field(
                    description="LDIF attributes with values",
                ),
            ] = u.Field(default_factory=MappingProxyType)
            object_classes: Annotated[
                t.StrSequence,
                u.Field(
                    description="LDAP object classes",
                ),
            ] = u.Field(default_factory=tuple)
            change_type: Annotated[
                str | None,
                u.Field(
                    None,
                    description="LDIF change type (add, modify, delete, modrdn)",
                ),
            ]
            controls: Annotated[
                t.StrSequence,
                u.Field(
                    description="LDAP controls for the entry",
                ),
            ] = u.Field(default_factory=tuple)

            def validate_business_rules(self) -> p.Result[bool]:
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

                    # Validate object classes
                    if not self.object_classes:
                        errors.append(
                            "Entry must have at least one object class",
                        )

                    # Validate attributes exist
                    if not self.attributes:
                        errors.append("Entry must have at least one attribute")

                    if errors:
                        return r[bool].fail("; ".join(errors))
                    return r[bool].ok(value=True)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    return r[bool].fail_op("LDIF entry validation", e)

        class LdifFile(m.Entity):
            """LDIF file representation with metadata."""

            file_path: Annotated[
                t.NonEmptyStr,
                u.Field(..., description="Path to the LDIF file"),
            ]
            stream_name: Annotated[
                t.NonEmptyStr,
                u.Field(..., description="Singer stream name"),
            ]
            entries: Annotated[
                t.SequenceOf[FlextTargetLdifModels.TargetLdif.LdifEntry],
                u.Field(
                    description="LDIF entries in the file",
                ),
            ] = u.Field(
                default_factory=lambda: list[
                    FlextTargetLdifModels.TargetLdif.LdifEntry
                ](),
            )
            format_options: Annotated[
                FlextTargetLdifModels.TargetLdif.LdifFormatOptions,
                u.Field(
                    ...,
                    description="Format options used for the file",
                ),
            ]

            # File metadata
            file_size_bytes: Annotated[
                t.NonNegativeInt,
                u.Field(default=0, description="File size in bytes"),
            ]
            entry_count: Annotated[
                t.NonNegativeInt,
                u.Field(default=0, description="Number of entries in file"),
            ]
            is_compressed: Annotated[
                bool,
                u.Field(default=False, description="Whether file is compressed"),
            ]

            def validate_business_rules(self) -> p.Result[bool]:
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
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    return r[bool].fail_op("LDIF file validation", e)

        class Sink:
            """Singer sink for writing records to LDIF format.

            Absorbed from sinks.py into namespace class.
            """

            @override
            def __init__(
                self,
                target_config: t.JsonMapping,
                stream_name: str,
                schema: t.JsonMapping,
                key_properties: t.StrSequence | None = None,
            ) -> None:
                """Initialize the LDIF sink."""
                self.settings: t.JsonMapping = target_config
                self.stream_name = stream_name
                self.schema = schema
                self.key_properties = key_properties or []
                self._ldif_writer: FlextTargetLdifWriter | None = None
                self._output_file: Path | None = None
                self._logger_instance: p.Logger | None = None

            @property
            def ldif_writer(self) -> FlextTargetLdifWriter:
                """The LDIF writer (for testing)."""
                return self._get_ldif_writer()

            @property
            def logger(self) -> p.Logger:
                """Lazy logger for Sink."""
                if self._logger_instance is None:
                    self._logger_instance = u.fetch_logger(__name__)
                return self._logger_instance

            def clean_up(self) -> None:
                """Clean up resources when sink is finished."""
                if self._ldif_writer:
                    result: p.Result[bool] = self._ldif_writer.close()
                    if not result.success:
                        self.logger.error(
                            "Failed to close LDIF writer",
                            error=result.error or "",
                        )
                    else:
                        self.logger.info(
                            "LDIF file written",
                            output_file=str(self._output_file),
                        )

            def process_batch(self, context: t.JsonMapping) -> None:
                """Process a batch of records."""
                if context:
                    context_dict = t.json_dict_adapter().validate_python(context)
                    self.logger.debug("Processing LDIF batch", context=context_dict)
                self._get_ldif_writer()

            def process_record(
                self,
                record: t.JsonMapping,
                context: t.JsonMapping,
            ) -> None:
                """Process a single record and write to LDIF."""
                if context:
                    context_dict = t.json_dict_adapter().validate_python(context)
                    self.logger.debug("Processing LDIF record", context=context_dict)
                ldif_writer = self._get_ldif_writer()
                result: p.Result[bool] = ldif_writer.write_record(record)
                if not result.success:
                    msg: str = f"Failed to write LDIF record: {result.error}"
                    raise RuntimeError(msg)

            def _get_ldif_writer(self) -> FlextTargetLdifWriter:
                """The or create the LDIF writer for this sink."""
                if self._ldif_writer is None:
                    output_file = self._get_output_file()
                    raw_ldif_options = self.settings.get("ldif_options", {})
                    ldif_options: t.JsonMapping = {}
                    if isinstance(raw_ldif_options, Mapping):
                        ldif_options = t.json_mapping_adapter().validate_python(
                            raw_ldif_options,
                        )
                    dn_template = self.settings.get("dn_template")
                    if dn_template is not None and (not isinstance(dn_template, str)):
                        dn_template = None
                    raw_attribute_mapping = self.settings.get("attribute_mapping", {})
                    attribute_mapping: t.StrMapping = {}
                    if isinstance(raw_attribute_mapping, Mapping):
                        attribute_mapping = {
                            key: value
                            for key, value in raw_attribute_mapping.items()
                            if isinstance(value, str)
                        }
                    self._ldif_writer = FlextTargetLdifWriter(
                        output_file=output_file,
                        ldif_options=ldif_options,
                        dn_template=dn_template,
                        attribute_mapping=attribute_mapping,
                        schema=self.schema,
                    )
                return self._ldif_writer

            def _get_output_file(self) -> Path:
                """The output file path for this stream."""
                if self._output_file is None:
                    output_path_raw = self.settings.get("output_path", "./output")
                    output_path_str = (
                        output_path_raw
                        if isinstance(output_path_raw, str)
                        else "./output"
                    )
                    output_path = Path(output_path_str)
                    safe_name = "".join(
                        ch for ch in self.stream_name if ch.isalnum() or ch in "-_"
                    ).strip()
                    if not safe_name:
                        safe_name = "stream"
                    filename = f"{safe_name}.ldif"
                    self._output_file = output_path / filename
                return self._output_file


# Short alias
m = FlextTargetLdifModels

__all__: list[str] = ["FlextTargetLdifModels", "m"]
