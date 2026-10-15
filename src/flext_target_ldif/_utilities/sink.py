"""LDIF runtime sink for the target-ldif Singer target.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from flext_core import u

from flext_target_ldif import FlextTargetLdifWriter, c, p, t


class FlextTargetLdifSink:
    """Singer sink writing stream records to one LDIF file per stream."""

    logger: p.Logger = u.fetch_logger(__name__)

    def __init__(
        self,
        target_config: t.JsonMapping,
        stream_name: str,
        schema: t.JsonMapping,
        key_properties: t.StrSequence | None = None,
    ) -> None:
        """Initialize the LDIF sink.

        Args:
            target_config: Merged target configuration mapping.
            stream_name: Name of the Singer stream this sink drains.
            schema: Singer schema for the stream.
            key_properties: Singer key properties for the stream.

        """
        self._config = target_config
        self.stream_name = stream_name
        self.schema = schema
        self.key_properties = key_properties or []
        self._ldif_writer: FlextTargetLdifWriter | None = None
        self._output_file: Path | None = None

    @property
    def ldif_writer(self) -> FlextTargetLdifWriter:
        """The LDIF writer bound to this sink."""
        return self._resolve_ldif_writer()

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
            context_dict = u.json_dict_adapter().validate_python(context)
            self.logger.debug("Processing LDIF batch", context=context_dict)
        self._resolve_ldif_writer()

    def process_record(
        self,
        record: t.JsonMapping,
        context: t.JsonMapping,
    ) -> None:
        """Process a single record and write to LDIF.

        Args:
            record: Singer record payload to write.
            context: Singer record context metadata.

        Raises:
            RuntimeError: If the LDIF writer rejects the record.

        """
        if context:
            context_dict = u.json_dict_adapter().validate_python(context)
            self.logger.debug("Processing LDIF record", context=context_dict)
        ldif_writer = self._resolve_ldif_writer()
        result: p.Result[bool] = ldif_writer.write_record(record)
        if not result.success:
            msg: str = f"Failed to write LDIF record: {result.error}"
            raise RuntimeError(msg)

    def _resolve_ldif_writer(self) -> FlextTargetLdifWriter:
        """Resolve the LDIF writer for this sink, creating it on first use.

        Returns:
            The LDIF writer configured from the target configuration.

        """
        if self._ldif_writer is None:
            output_file = self._resolve_output_file()
            raw_ldif_options = self._config.get("ldif_options", {})
            ldif_options: t.JsonMapping = {}
            if isinstance(raw_ldif_options, Mapping):
                ldif_options = u.json_mapping_adapter().validate_python(
                    raw_ldif_options,
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

    def _resolve_output_file(self) -> Path:
        """Resolve the output file path for this stream.

        Returns:
            The output file path derived from the configured output
            directory and sanitized stream name.

        """
        if self._output_file is None:
            output_path_raw = self._config.get(
                "output_path",
                c.TargetLdif.DEFAULT_OUTPUT_PATH,
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


__all__: list[str] = ["FlextTargetLdifSink"]
