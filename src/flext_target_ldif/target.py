"""Main Singer Target implementation for LDIF output.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, override

from flext_target_ldif import (
    FlextTargetLdifSettings,
    m,
    main as cli_main,
    t,
)

if TYPE_CHECKING:
    from collections.abc import (
        Callable,
    )


class FlextTargetLdif:
    """Singer target for writing data to LDIF format."""

    name: str = "target-ldif"

    @override
    def __init__(
        self,
        settings: t.JsonMapping | None = None,
        validate_config: bool = False,
    ) -> None:
        """Initialize the LDIF target."""
        defaults: t.JsonMapping = {
            "file_naming_pattern": "{stream_name}_{timestamp}.ldif",
            "dn_template": "uid={uid},ou=users,dc=example,dc=com",
            "output_path": "./output",
        }
        # NOTE (multi-agent): mro-rn88 — persist the merged config on the instance so
        # get_sink/validate_config read self._config (was an undefined bare `settings`).
        self._config: t.JsonMapping = {**defaults, **(settings or {})}
        self.sinks: dict[str, m.TargetLdif.Sink] = {}
        self._test_config: t.JsonMapping | None = None
        if validate_config:
            self.validate_config()
        output_path_raw = self._config.get("output_path", "./output")
        output_path_str = (
            output_path_raw if isinstance(output_path_raw, str) else "./output"
        )
        output_path = Path(output_path_str)
        output_path.mkdir(parents=True, exist_ok=True)

    @property
    def settings(self) -> t.JsonMapping:
        """The merged target configuration mapping."""
        # NOTE (multi-agent): mro-rn88 — public accessor for the merged config that
        # tests read as target.settings[...]; backed by the instance _config.
        return self._config

    @property
    def cli(self) -> Callable[..., int]:
        """The CLI entry point for this target."""
        return cli_main

    @property
    def config_jsonschema(self) -> t.JsonMapping:
        """The JSON schema for configuration."""
        return FlextTargetLdifSettings.model_json_schema()

    @property
    def default_sink_class(self) -> type[m.TargetLdif.Sink]:
        """The default sink class for this target."""
        sink_cls: type[m.TargetLdif.Sink] = m.TargetLdif.Sink
        return sink_cls

    def get_sink(
        self,
        stream_name: str,
        schema: t.JsonMapping,
    ) -> m.TargetLdif.Sink:
        """The or create a sink for the given stream."""
        if stream_name not in self.sinks:
            self.sinks[stream_name] = m.TargetLdif.Sink(
                target_config=self._config,
                stream_name=stream_name,
                schema=schema,
            )
        return self.sinks[stream_name]

    def validate_config(self) -> None:
        """Validate the target configuration."""
        config_dict = dict(self._test_config) if self._test_config else dict(self._config)
        if self._test_config is not None and "output_file" not in config_dict:
            msg = "Output file is required"
            raise ValueError(msg)
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
        filtered_config: t.MutableJsonMapping = {
            k: v for k, v in config_dict.items() if k in allowed_fields
        }
        if "output_file" not in filtered_config:
            filtered_config["output_file"] = "output.ldif"
        # NOTE (multi-agent): mro-rn88 — wrap under the TargetLdif namespace so the domain
        # validator runs (a flat dict is dropped by extra="ignore").
        FlextTargetLdifSettings.model_validate({"TargetLdif": filtered_config})
