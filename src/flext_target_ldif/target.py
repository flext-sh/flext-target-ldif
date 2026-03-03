"""Main Singer Target implementation for LDIF output.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import override

from flext_target_ldif.cli import main as cli_main
from flext_target_ldif.settings import FlextTargetLdifSettings
from flext_target_ldif.sinks import LDIFSink
from flext_target_ldif.typings import t


class TargetLDIF:
    """Singer target for writing data to LDIF format."""

    name: str = "target-ldif"

    @override
    def __init__(
        self,
        config: Mapping[str, t.GeneralValueType] | None = None,
        validate_config: bool = False,
    ) -> None:
        """Initialize the LDIF target."""
        self.config: Mapping[str, t.GeneralValueType] = config or {}
        self.sinks: dict[str, LDIFSink] = {}
        self._test_config: dict[str, t.GeneralValueType] | None = None

        # Validate config if requested
        if validate_config:
            self.validate_config()

        # Ensure output directory exists
        output_path_raw = self.config.get("output_path", "./output")
        output_path_str = (
            output_path_raw if isinstance(output_path_raw, str) else "./output"
        )
        output_path = Path(output_path_str)
        output_path.mkdir(parents=True, exist_ok=True)

    def get_sink(
        self,
        stream_name: str,
        schema: Mapping[str, t.GeneralValueType],
    ) -> LDIFSink:
        """Get or create a sink for the given stream."""
        if stream_name not in self.sinks:
            self.sinks[stream_name] = LDIFSink(
                target_config=self.config,
                stream_name=stream_name,
                schema=schema,
            )
        return self.sinks[stream_name]

    @property
    def default_sink_class(self) -> type[LDIFSink]:
        """Return the default sink class for this target."""
        return LDIFSink

    @property
    def config_jsonschema(self) -> dict[str, t.GeneralValueType]:
        """Return JSON schema for configuration."""
        return FlextTargetLdifSettings.model_json_schema()

    @property
    def cli(self) -> Callable[..., None]:
        """Return the CLI entry point for this target."""
        return cli_main

    def validate_config(self) -> None:
        """Validate the target configuration."""
        config_dict = (
            dict(self._test_config) if self._test_config else dict(self.config)
        )
        # Filter to only include FlextTargetLdifSettings fields
        allowed_fields: set[str] = {
            "output_file",
            "output_path",
            "file_naming_pattern",
            "dn_template",
            "attribute_mapping",
            "ldif_options",
            "schema_validation",
            "line_length",
            "base64_encode",
            "include_timestamps",
        }
        filtered_config: dict[str, t.GeneralValueType] = {
            k: v for k, v in config_dict.items() if k in allowed_fields
        }
        settings = FlextTargetLdifSettings.model_validate(filtered_config)
        result = settings.validate_domain_rules()
        if not result.is_success:
            msg = f"Configuration validation failed: {result.error}"
            raise ValueError(msg)


if __name__ == "__main__":
    # Use flext-target-ldif CLI entry point instead
    pass
