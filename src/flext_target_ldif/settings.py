"""Configuration classes for FLEXT Target LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_core import FlextSettingsBase
from flext_target_ldif import c, m, p, r, t, u


class FlextTargetLdifSettings(FlextSettingsBase):
    """Typed runtime configuration for the LDIF target.

    Mutation is blocked by ``model_config.frozen=True`` (Pydantic-2 native);
    runtime overrides go through ``cls.update_global(**overrides)`` which
    creates a fresh validated instance via ``model_copy(update=…)`` and
    replaces the singleton — no custom ``__setattr__`` hack required.
    """

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_TARGET_LDIF_",
        extra="ignore",
        frozen=True,
        validate_assignment=True,
    )

    output_file: Annotated[
        str,
        u.Field(
            default=c.TargetLdif.DEFAULT_OUTPUT_FILE,
            description="Output LDIF filename",
        ),
    ]
    output_path: Annotated[
        str,
        u.Field(
            default=c.TargetLdif.DEFAULT_OUTPUT_PATH,
            description="Output directory path",
        ),
    ]
    file_naming_pattern: Annotated[
        str,
        u.Field(
            default=c.TargetLdif.DEFAULT_FILE_NAMING_PATTERN,
            description="Pattern for generated filenames",
        ),
    ]
    dn_template: Annotated[
        str,
        u.Field(
            default=c.TargetLdif.DEFAULT_DN_TEMPLATE,
            description="Template used to build entry DN values",
        ),
    ]
    attribute_mapping: Annotated[
        t.StrMapping,
        u.Field(
            description="Source-to-LDIF attribute mapping",
        ),
    ] = u.Field(default_factory=dict)
    ldif_options: Annotated[
        t.JsonMapping,
        u.Field(
            description="Raw LDIF formatter options",
        ),
    ] = u.Field(default_factory=dict)
    schema_validation: Annotated[
        bool,
        u.Field(
            default=True,
            description="Enable schema validation for transformed records",
        ),
    ]
    line_length: Annotated[
        int,
        u.Field(
            default=c.TargetLdif.DEFAULT_LINE_LENGTH,
            ge=1,
            description="LDIF line wrap length",
        ),
    ]
    base64_encode: Annotated[
        bool,
        u.Field(
            default=False,
            description="Force base64 encoding for all values",
        ),
    ]
    include_timestamps: Annotated[
        bool,
        u.Field(
            default=True,
            description="Include timestamp metadata in generated entries",
        ),
    ]

    def validate_domain_rules(self) -> p.Result[bool]:
        """Validate required target configuration constraints."""
        if not self.output_file.strip():
            msg = "Output file cannot be empty"
            raise ValueError(msg)
        if not self.output_path.strip():
            msg = "output_path cannot be empty"
            raise ValueError(msg)
        if not self.dn_template.strip():
            msg = "DN template cannot be empty"
            raise ValueError(msg)
        return r[bool].ok(value=True)
