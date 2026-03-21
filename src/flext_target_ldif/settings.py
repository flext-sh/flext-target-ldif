"""Configuration classes for FLEXT Target LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, Any, override as _override

from flext_core import FlextSettings, r
from flext_core.typings import t
from pydantic import Field, ValidationError
from pydantic_core import PydanticUndefined


class FlextTargetLdifSettings(FlextSettings):
    """Typed runtime configuration for the LDIF target."""

    _allow_mutation: bool = True

    def __init__(self, **kwargs: Any) -> None:
        """Initialize settings and freeze after construction.

        Explicitly applies field defaults for missing kwargs to ensure
        clean initialization when FlextSettings DI provider
        short-circuits BaseSettings.__init__.
        """
        object.__setattr__(self, "_allow_mutation", True)
        for field_name, field_info in type(self).model_fields.items():
            if field_name not in kwargs:
                if field_info.default is not PydanticUndefined:
                    kwargs[field_name] = field_info.default
                elif field_info.default_factory is not None:
                    factory: Any = field_info.default_factory
                    kwargs[field_name] = factory()
        super().__init__(**kwargs)
        object.__setattr__(self, "_allow_mutation", False)

    @_override
    def __setattr__(self, name: str, value: Any) -> None:
        """Block attribute mutation after initialization."""
        try:
            allow = object.__getattribute__(self, "_allow_mutation")
        except AttributeError:
            allow = True
        if not allow and name != "_allow_mutation" and name in type(self).model_fields:
            raise ValidationError.from_exception_data(
                type(self).__name__,
                [{"type": "frozen_instance", "loc": (name,), "input": value}],
            )
        super().__setattr__(name, value)

    output_file: Annotated[
        str, Field(default="output.ldif", description="Output LDIF filename")
    ]
    output_path: Annotated[
        str, Field(default="./output", description="Output directory path")
    ]
    file_naming_pattern: Annotated[
        str,
        Field(
            default="{stream_name}.ldif", description="Pattern for generated filenames"
        ),
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
        Field(
            default_factory=dict,
            description="Source-to-LDIF attribute mapping",
        ),
    ]
    ldif_options: Annotated[
        dict[str, t.ContainerValue],
        Field(
            default_factory=dict,
            description="Raw LDIF formatter options",
        ),
    ]
    schema_validation: Annotated[
        bool,
        Field(
            default=True,
            description="Enable schema validation for transformed records",
        ),
    ]
    line_length: Annotated[
        int, Field(default=78, ge=1, description="LDIF line wrap length")
    ]
    base64_encode: Annotated[
        bool,
        Field(
            default=False,
            description="Force base64 encoding for all values",
        ),
    ]
    include_timestamps: Annotated[
        bool,
        Field(
            default=True,
            description="Include timestamp metadata in generated entries",
        ),
    ]

    def validate_domain_rules(self) -> r[bool]:
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


__all__: list[str] = ["FlextTargetLdifSettings"]
