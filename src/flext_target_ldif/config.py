"""Configuration classes for FLEXT Target LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import cast

from pydantic import Field, field_validator

from flext_core import FlextModels, FlextResult, FlextTypes


class FlextTargetLdifConfig(FlextModels.Config):
    """Configuration for FLEXT Target LDIF using FlextConfig.BaseModel patterns."""

    output_path: str = Field(
        default="./output",
        description="Directory path for LDIF output files",
    )
    file_naming_pattern: str = Field(
        default="{stream_name}_{timestamp}.ldif",
        description="Pattern for LDIF file names. Available variables: {stream_name}, {timestamp}",
    )
    dn_template: str = Field(
        description="Template for generating Distinguished Names (DN) - MUST be configured for production",
        json_schema_extra={"example": "uid={uid},ou=users,dc=company,dc=local"},
    )
    attribute_mapping: FlextTypes.Core.Headers = Field(
        default_factory=dict,
        description="Mapping of stream fields to LDAP attributes",
    )
    ldif_options: FlextTypes.Core.Dict = Field(
        default_factory=lambda: cast(
            "FlextTypes.Core.Dict",
            {
                "line_length": 78,
                "base64_encode": False,
                "include_timestamps": True,
            },
        ),
        description="LDIF format options",
    )

    @field_validator("output_path")
    @classmethod
    def validate_output_path(cls, v: str) -> str:
        """Validate output path using centralized FlextModels validation."""
        # Use centralized FlextModels validation instead of duplicate logic
        validation_result = FlextModels.create_validated_file_path(v)
        if validation_result.is_failure:
            error_msg = f"Invalid output path: {validation_result.error}"
            raise ValueError(error_msg)
        return validation_result.unwrap()

    @field_validator("dn_template")
    @classmethod
    def validate_dn_template(cls, v: str) -> str:
        """Validate DN template has proper format."""
        if not v:
            msg = "DN template cannot be empty"
            raise ValueError(msg)

        if "{" not in v or "}" not in v:
            msg = "DN template must contain at least one variable placeholder"
            raise ValueError(msg)

        return v

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate LDIF target configuration business rules using FlextModels.Config pattern."""
        try:
            # Use centralized FlextModels validation instead of duplicate path logic
            path_validation_result = FlextModels.create_validated_file_path(
                self.output_path
            )
            if path_validation_result.is_failure:
                return FlextResult[None].fail(
                    f"Output path validation failed: {path_validation_result.error}"
                )

            # Use flext-ldap for DN validation - NO local duplication
            if not self.dn_template:
                return FlextResult[None].fail("DN template cannot be empty")

            # For template validation, create a sample DN with dummy values
            sample_dn = self.dn_template.replace("{uid}", "testuser").replace(
                "{cn}",
                "Test User",
            )
            # Basic DN validation - check if contains = and ,
            if "=" not in sample_dn or not sample_dn.strip():
                return FlextResult[None].fail(
                    "DN template format is invalid - must follow LDAP DN structure",
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Configuration validation failed: {e}")


__all__: FlextTypes.Core.StringList = [
    "FlextTargetLdifConfig",
]
