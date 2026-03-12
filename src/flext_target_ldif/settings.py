"""Configuration classes for FLEXT Target LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextSettings, r
from pydantic import Field


class FlextTargetLdifSettings(FlextSettings):
    """Typed runtime configuration for the LDIF target."""

    output_file: str = Field(default="output.ldif", description="Output LDIF filename")
    output_path: str = Field(default="./output", description="Output directory path")
    file_naming_pattern: str = Field(
        default="{stream_name}.ldif", description="Pattern for generated filenames"
    )
    dn_template: str = Field(..., description="Template used to build entry DN values")
    attribute_mapping: dict[str, str] = Field(
        default_factory=dict,
        description="Source-to-LDIF attribute mapping",
    )
    ldif_options: dict[str, object] = Field(
        default_factory=dict,
        description="Raw LDIF formatter options",
    )
    schema_validation: bool = Field(
        default=True,
        description="Enable schema validation for transformed records",
    )
    line_length: int = Field(default=78, ge=1, description="LDIF line wrap length")
    base64_encode: bool = Field(
        default=False,
        description="Force base64 encoding for all values",
    )
    include_timestamps: bool = Field(
        default=True,
        description="Include timestamp metadata in generated entries",
    )

    def validate_domain_rules(self) -> r[bool]:
        """Validate required target configuration constraints."""
        if not self.output_path.strip():
            return r[bool].fail("output_path cannot be empty")
        if not self.dn_template.strip():
            return r[bool].fail("dn_template cannot be empty")
        return r[bool].ok(value=True)


__all__: list[str] = ["FlextTargetLdifSettings"]
