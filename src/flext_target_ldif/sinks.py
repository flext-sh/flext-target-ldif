"""Singer Sink implementation for LDIF output.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import override

from flext_core import p, r
from flext_core.loggings import FlextLogger

from flext_target_ldif import t
from flext_target_ldif.writer import LdifWriter


class LDIFSink:
    """Singer sink for writing records to LDIF format."""

    @override
    def __init__(
        self,
        target_config: Mapping[str, t.ContainerValue],
        stream_name: str,
        schema: Mapping[str, t.ContainerValue],
        key_properties: list[str] | None = None,
    ) -> None:
        """Initialize the LDIF sink."""
        self.config: Mapping[str, t.ContainerValue] = target_config
        self.stream_name = stream_name
        self.schema = schema
        self.key_properties = key_properties or []
        self._ldif_writer: LdifWriter | None = None
        self._output_file: Path | None = None
        self._logger_instance: p.Logger | None = None

    @property
    def ldif_writer(self) -> LdifWriter:
        """Get the LDIF writer (for testing)."""
        return self._get_ldif_writer()

    @property
    def logger(self) -> p.Logger:
        """Lazy logger for LDIFSink."""
        if self._logger_instance is None:
            self._logger_instance = FlextLogger.create_module_logger(__name__)
        return self._logger_instance

    def clean_up(self) -> None:
        """Clean up resources when sink is finished."""
        if self._ldif_writer:
            result: r[bool] = self._ldif_writer.close()
            if not result.is_success:
                self.logger.error(
                    "Failed to close LDIF writer", error=result.error or ""
                )
            else:
                self.logger.info(
                    "LDIF file written", output_file=str(self._output_file)
                )

    def process_batch(self, _context: Mapping[str, t.ContainerValue]) -> None:
        """Process a batch of records."""
        self._get_ldif_writer()

    def process_record(
        self,
        record: Mapping[str, t.ContainerValue],
        _context: Mapping[str, t.ContainerValue],
    ) -> None:
        """Process a single record and write to LDIF.

        Returns:
        object: Description of return value.

        """
        ldif_writer = self._get_ldif_writer()
        result: r[bool] = ldif_writer.write_record(record)
        if not result.is_success:
            msg: str = f"Failed to write LDIF record: {result.error}"
            raise RuntimeError(msg)

    def _get_ldif_writer(self) -> LdifWriter:
        """Get or create the LDIF writer for this sink.

        Returns:
        LdifWriter: The LDIF writer.

        """
        if self._ldif_writer is None:
            output_file = self._get_output_file()
            raw_ldif_options = self.config.get("ldif_options", {})
            ldif_options: dict[str, t.ContainerValue] = {}
            if isinstance(raw_ldif_options, Mapping):
                ldif_options = {
                    str(key): value for key, value in raw_ldif_options.items()
                }
            dn_template = self.config.get("dn_template")
            if dn_template is not None and (not isinstance(dn_template, str)):
                dn_template = None
            raw_attribute_mapping = self.config.get("attribute_mapping", {})
            attribute_mapping: dict[str, str] = {}
            if isinstance(raw_attribute_mapping, Mapping):
                attribute_mapping = {
                    str(key): value
                    for key, value in raw_attribute_mapping.items()
                    if isinstance(value, str)
                }
            self._ldif_writer = LdifWriter(
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
            output_path_raw = self.config.get("output_path", "./output")
            output_path_str = (
                output_path_raw if isinstance(output_path_raw, str) else "./output"
            )
            output_path = Path(output_path_str)
            safe_name = "".join(
                c for c in self.stream_name if c.isalnum() or c in "-_"
            ).strip()
            if not safe_name:
                safe_name = "stream"
            filename = f"{safe_name}.ldif"
            self._output_file = output_path / filename
        return self._output_file
