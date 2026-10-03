"""Models for LDIF target operations.

This module provides data models for LDIF target operations.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels, u

from flext_target_ldif import c, p, t
from flext_target_ldif.writer import FlextTargetLdifWriter


class FlextTargetLdifModels(FlextMeltanoModels, FlextLdifModels):
    """Models composed from Meltano and LDIF via MRO plus the LDIF runtime sink."""

    class TargetLdif:
        """TargetLdif domain model namespace."""

        class Sink:
            """Singer sink for writing records to LDIF format.

            Absorbed from sinks.py into namespace class.
            """

            def __init__(
                self,
                target_config: t.JsonMapping,
                stream_name: str,
                schema: t.JsonMapping,
                key_properties: t.StrSequence | None = None,
            ) -> None:
                """Initialize the LDIF sink."""
                # NOTE (multi-agent): mro-rn88 — retain target_config; writer/output methods
                # read self._config.get(...) (was an undefined bare `settings`).
                self._config = target_config
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
                            "Failed to close LDIF writer", error=result.error or ""
                        )
                    else:
                        self.logger.info(
                            "LDIF file written", output_file=str(self._output_file)
                        )

            def process_batch(self, context: t.JsonMapping) -> None:
                """Process a batch of records."""
                if context:
                    context_dict = t.json_dict_adapter().validate_python(context)
                    self.logger.debug("Processing LDIF batch", context=context_dict)
                self._get_ldif_writer()

            def process_record(
                self, record: t.JsonMapping, context: t.JsonMapping
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
                """Get or create the LDIF writer for this sink."""
                if self._ldif_writer is None:
                    output_file = self._get_output_file()
                    raw_ldif_options = self._config.get("ldif_options", {})
                    ldif_options: t.JsonMapping = {}
                    if isinstance(raw_ldif_options, Mapping):
                        ldif_options = t.json_mapping_adapter().validate_python(
                            raw_ldif_options
                        )
                    raw_dn_template = self._config.get("dn_template")
                    dn_template: str | None = (
                        raw_dn_template if isinstance(raw_dn_template, str) else None
                    )
                    raw_attribute_mapping = self._config.get("attribute_mapping", {})
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
                """Get the output file path for this stream."""
                if self._output_file is None:
                    output_path_raw = self._config.get(
                        "output_path", c.TargetLdif.DEFAULT_OUTPUT_PATH
                    )
                    output_path_str = (
                        output_path_raw
                        if isinstance(output_path_raw, str)
                        else c.TargetLdif.DEFAULT_OUTPUT_PATH
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
