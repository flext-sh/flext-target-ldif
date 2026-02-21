"""Configuration classes for FLEXT Target LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Self

from flext_core import (
    FlextResult,
    FlextSettings,
    FlextTypes as t,
)
from pydantic import Field, field_validator
from pydantic_settings import SettingsConfigDict

from flext_target_ldif.constants import c


class FlextTargetLdifSettings(FlextSettings):
    """Configuration for FLEXT Target LDIF using FlextSettings patterns."""

    output_path: str = Field(
        default="./output",
        description="Directory path for LDIF output files",
    )
    file_naming_pattern: str = Field(
        default="{stream_name}_{timestamp}.ldif",
        description=(
            "Pattern for LDIF file names. Available variables: "
            "{stream_name}, {timestamp}"
        ),
    )
    dn_template: str = Field(
        min_length=1,
        description="Template for generating Distinguished Names (DN) - MUST be configured for production",
        json_schema_extra={"example": "uid={uid},ou=users,dc=company,dc=local"},
    )
    attribute_mapping: dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of stream fields to LDAP attributes",
    )
    ldif_options: dict[str, t.GeneralValueType] = Field(
        default_factory=lambda: dict[str, t.GeneralValueType](
            line_length=c.MAX_LINE_LENGTH,
            base64_encode="False",
            include_timestamps="True",
        ),
        description="LDIF format options",
    )

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_LDIF_",
        case_sensitive=False,
        extra="ignore",
        str_strip_whitespace=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
        frozen=False,
    )

    @classmethod
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using FlextSettings pattern."""
        return cls()

    @classmethod
    def create_for_development(cls, **overrides: t.GeneralValueType) -> Self:
        """Create configuration for development environment."""
        dev_overrides: dict[str, t.GeneralValueType] = {
            "file_naming_pattern": "dev_{stream_name}_{timestamp}.ldif",
            "ldif_options": {
                "line_length": c.MAX_LINE_LENGTH + 42,
                "base64_encode": "False",
                "include_timestamps": "True",
            },
            **overrides,
        }
        return cls(**dev_overrides)

    @classmethod
    def create_for_production(cls, **overrides: t.GeneralValueType) -> Self:
        """Create configuration for production environment."""
        prod_overrides: dict[str, t.GeneralValueType] = {
            "file_naming_pattern": "prod_{stream_name}_{timestamp}.ldif",
            "ldif_options": {
                "line_length": 78,
                "base64_encode": "False",
                "include_timestamps": "True",
            },
            **overrides,
        }
        return cls(**prod_overrides)

    @classmethod
    def create_for_testing(cls, **overrides: t.GeneralValueType) -> Self:
        """Create configuration for testing environment."""
        test_overrides: dict[str, t.GeneralValueType] = {
            "output_path": "./test-output",
            "file_naming_pattern": "test_{stream_name}.ldif",
            "ldif_options": {
                "line_length": 78,
                "base64_encode": "True",
                "include_timestamps": "False",
            },
            **overrides,
        }
        return cls(**test_overrides)

    @field_validator("output_path")
    @classmethod
    def validate_output_path(cls, v: str) -> str:
        """Validate output path is non-empty."""
        if not v or not v.strip():
            error_msg = "Invalid output path: path cannot be empty"
            raise ValueError(error_msg)
        return v.strip()

    @field_validator("dn_template")
    @classmethod
    def validate_dn_template(cls, v: str) -> str:
        """Validate DN template has proper format with variable placeholders."""
        if "{" not in v or "}" not in v:
            msg = "DN template must contain at least one variable placeholder"
            raise ValueError(msg)

        return v

    def validate_business_rules(self) -> FlextResult[bool]:
        """Validate LDIF target configuration business rules using FlextSettings pattern."""
        try:
            # Validate output path is non-empty
            if not self.output_path or not self.output_path.strip():
                return FlextResult[bool].fail("Output path cannot be empty")

            # Validate DN template is non-empty
            if not self.dn_template:
                return FlextResult[bool].fail("DN template cannot be empty")

            # For template validation, create a sample DN with dummy values
            sample_dn = self.dn_template.replace("{uid}", "testuser").replace(
                "{cn}",
                "Test User",
            )
            # Basic DN validation - check if contains = and ,
            if "=" not in sample_dn or not sample_dn.strip():
                return FlextResult[bool].fail(
                    "DN template format is invalid - must follow LDAP DN structure",
                )

            return FlextResult[bool].ok(value=True)
        except Exception as e:
            return FlextResult[bool].fail(f"Configuration validation failed: {e}")


FlextTargetLDIFSettings = FlextTargetLdifSettings
TargetLDIFConfig = FlextTargetLdifSettings


__all__: list[str] = [
    "FlextTargetLDIFSettings",
    "FlextTargetLdifSettings",
    "TargetLDIFConfig",
]
