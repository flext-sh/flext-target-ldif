"""Configuration classes for FLEXT Target LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Callable,
)
from typing import Annotated, ClassVar, override as _override

from flext_core import FlextSettings

from flext_target_ldif import c, p, r, t, u
from flext_target_ldif.models import m


@FlextSettings.auto_register("target-ldif")
class FlextTargetLdifSettings(FlextSettings):
    """Typed runtime configuration for the LDIF target."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_TARGET_LDIF_", extra="ignore"
    )

    _allow_mutation: bool = True

    def __init__(self, **kwargs: t.SettingsValue) -> None:
        """Initialize settings and freeze after construction.

        Explicitly applies field defaults for missing kwargs to ensure
        clean initialization when FlextSettings DI provider
        short-circuits BaseSettings.__init__.
        """
        object.__setattr__(self, "_allow_mutation", True)
        for field_name, field_info in type(self).model_fields.items():
            if field_name not in kwargs:
                if field_info.default is not c.PydanticUndefined:
                    kwargs[field_name] = field_info.default
                elif field_info.default_factory is not None:
                    factory_fn: Callable[..., t.SettingsValue] = (
                        field_info.default_factory
                    )
                    kwargs[field_name] = factory_fn()
        super().__init__(**kwargs)
        object.__setattr__(self, "_allow_mutation", False)

    @_override
    def __setattr__(self, name: str, value: t.Container) -> None:
        """Block attribute mutation after initialization."""
        try:
            allow = object.__getattribute__(self, "_allow_mutation")
        except AttributeError:
            allow = True
        if not allow and name != "_allow_mutation" and name in type(self).model_fields:
            raise c.ValidationError.from_exception_data(
                type(self).__name__,
                [{"type": "frozen_instance", "loc": (name,), "input": value}],
            )
        super().__setattr__(name, value)

    output_file: Annotated[
        str,
        u.Field(
            default=c.TargetLdif.DEFAULT_OUTPUT_FILE, description="Output LDIF filename"
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
        t.ContainerValueMapping,
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
