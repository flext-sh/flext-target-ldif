"""Settings for flext-target-ldif — namespaced under ``settings.TargetLdif``.

Universal fields via MRO; project fields in the ``TargetLdif`` group with simple
scalar types (env-settable).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_meltano import FlextMeltanoSettings, m, u


class FlextTargetLdifSettings(FlextMeltanoSettings):
    """LDIF target settings; fields under ``settings.TargetLdif.*``."""

    model_config = m.SettingsConfigDict(
        env_prefix="FLEXT_TARGET_LDIF_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _TargetLdif(m.BaseModel):
        """Namespaced LDIF target settings."""

        output_file: Annotated[str, m.Field(description="Output LDIF filename")] = (
            "output.ldif"
        )
        output_path: Annotated[str, m.Field(description="Output directory path")] = (
            "./output"
        )
        file_naming_pattern: Annotated[
            str,
            m.Field(
                description="Pattern for generated filenames",
            ),
        ] = "{stream_name}.ldif"
        dn_template: Annotated[
            str,
            m.Field(
                description="Template used to build entry DN values",
            ),
        ] = "uid={uid},ou=users,dc=example,dc=com"
        attribute_mapping: Annotated[
            dict[str, str],
            m.Field(
                description="Source-to-LDIF attribute mapping",
            ),
        ] = m.Field(default_factory=dict)
        ldif_options: Annotated[
            dict[str, str], m.Field(description="Raw LDIF formatter options")
        ] = m.Field(default_factory=dict)
        schema_validation: Annotated[
            bool,
            m.Field(
                description="Enable schema validation for transformed records",
            ),
        ] = True
        line_length: Annotated[
            int, m.Field(ge=1, description="LDIF line wrap length")
        ] = 78
        base64_encode: Annotated[
            bool, m.Field(description="Force base64 encoding for all values")
        ] = False
        include_timestamps: Annotated[
            bool,
            m.Field(
                description="Include timestamp metadata in generated entries",
            ),
        ] = True

        @u.model_validator(mode="after")
        def _validate_domain_rules(self) -> FlextTargetLdifSettings._TargetLdif:
            """Enforce required target configuration invariants at construction.

            Returns:
                The resulting ``FlextTargetLdifSettings._TargetLdif``.

            Raises:
                ValueError: If Output file cannot be empty; or if output_path cannot be
                    empty; or if DN template cannot be empty.
            """
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
        TargetLdif: _TargetLdif = m.Field(
            default_factory=_TargetLdif,
            description="Namespaced LDIF target settings.",
        )


settings: FlextTargetLdifSettings = FlextTargetLdifSettings.fetch_global()
"""Pre-instantiated project settings singleton.

Exposed as ``from flext_target_ldif import settings``.
"""

__all__: list[str] = ["FlextTargetLdifSettings", "settings"]
