"""Settings for flext-target-ldif — namespaced under ``settings.TargetLdif``.

Universal fields via MRO; project fields in the ``TargetLdif`` group with simple
scalar types (env-settable).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field, model_validator
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextTargetLdifSettings(FlextMeltanoSettings):
    """LDIF target settings; fields under ``settings.TargetLdif.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_LDIF_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _TargetLdif(BaseModel):
        """Namespaced LDIF target settings."""

        output_file: Annotated[str, Field(default="output.ldif", description="Output LDIF filename")]
        output_path: Annotated[str, Field(default="./output", description="Output directory path")]
        file_naming_pattern: Annotated[
            str,
            Field(default="{stream_name}.ldif", description="Pattern for generated filenames"),
        ]
        dn_template: Annotated[
            str,
            Field(
                default="uid={uid},ou=users,dc=example,dc=com",
                description="Template used to build entry DN values",
            ),
        ]
        attribute_mapping: Annotated[
            dict[str, str],
            Field(default_factory=dict, description="Source-to-LDIF attribute mapping"),
        ]
        ldif_options: Annotated[
            dict[str, str],
            Field(default_factory=dict, description="Raw LDIF formatter options"),
        ]
        schema_validation: Annotated[
            bool,
            Field(default=True, description="Enable schema validation for transformed records"),
        ]
        line_length: Annotated[int, Field(default=78, ge=1, description="LDIF line wrap length")]
        base64_encode: Annotated[
            bool,
            Field(default=False, description="Force base64 encoding for all values"),
        ]
        include_timestamps: Annotated[
            bool,
            Field(default=True, description="Include timestamp metadata in generated entries"),
        ]

        @model_validator(mode="after")
        def _validate_domain_rules(self) -> FlextTargetLdifSettings._TargetLdif:
            """Enforce required target configuration invariants at construction."""
            if not self.output_file.strip():
                msg = "Output file cannot be empty"
                raise ValueError(msg)
            if not self.output_path.strip():
                msg = "output_path cannot be empty"
                raise ValueError(msg)
            if not self.dn_template.strip():
                msg = "DN template cannot be empty"
                raise ValueError(msg)
            return self

    if TYPE_CHECKING:
        TargetLdif: _TargetLdif
    else:
        TargetLdif: _TargetLdif = Field(
            default_factory=_TargetLdif,
            description="Namespaced LDIF target settings.",
        )


settings: FlextTargetLdifSettings = FlextTargetLdifSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_target_ldif import settings``."""

__all__: list[str] = ["FlextTargetLdifSettings", "settings"]
