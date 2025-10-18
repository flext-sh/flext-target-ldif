"""Configuration classes for FLEXT Target LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Self, cast

from flext_core import FlextConfig, FlextConstants, FlextModels, FlextResult
from pydantic import Field, field_validator
from pydantic_settings import SettingsConfigDict


class FlextTargetLdifConfig(FlextConfig):
    """Configuration for FLEXT Target LDIF using FlextConfig patterns."""

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
    attribute_mapping: dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of stream fields to LDAP attributes",
    )
    ldif_options: dict[str, object] = Field(
        default_factory=lambda: cast(
            "dict[str, object]",
            {
                "line_length": FlextConstants.Limits.MAX_LINE_LENGTH,
                "base64_encode": "False",
                "include_timestamps": "True",
            },
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
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-target-ldif")

    @classmethod
    def create_for_development(cls, **overrides: object) -> Self:
        """Create configuration for development environment."""
        dev_overrides: dict[str, object] = {
            "file_naming_pattern": "dev_{stream_name}_{timestamp}.ldif",
            "ldif_options": {
                "line_length": FlextConstants.Limits.MAX_LINE_LENGTH + 42,
                "base64_encode": "False",
                "include_timestamps": "True",
            },
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-ldif", **dev_overrides
        )

    @classmethod
    def create_for_production(cls, **overrides: object) -> Self:
        """Create configuration for production environment."""
        prod_overrides: dict[str, object] = {
            "file_naming_pattern": "prod_{stream_name}_{timestamp}.ldif",
            "ldif_options": {
                "line_length": 78,
                "base64_encode": "False",
                "include_timestamps": "True",
            },
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-ldif", **prod_overrides
        )

    @classmethod
    def create_for_testing(cls, **overrides: object) -> Self:
        """Create configuration for testing environment."""
        test_overrides: dict[str, object] = {
            "output_path": "./test-output",
            "file_naming_pattern": "test_{stream_name}.ldif",
            "ldif_options": {
                "line_length": 78,
                "base64_encode": "True",
                "include_timestamps": "False",
            },
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-ldif", **test_overrides
        )

    @field_validator("output_path")
    @classmethod
    def validate_output_path(cls, v: str) -> str:
        """Validate output path using centralized FlextModels validation."""
        # Use centralized FlextModels validation instead of duplicate logic
        validation_result: FlextResult[object] = FlextModels.create_validated_file_path(
            v
        )
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

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate LDIF target configuration business rules using FlextConfig pattern."""
        try:
            # Use centralized FlextModels validation instead of duplicate path logic
            path_validation_result = FlextModels.create_validated_file_path(
                self.output_path,
            )
            if path_validation_result.is_failure:
                return FlextResult[None].fail(
                    f"Output path validation failed: {path_validation_result.error}",
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


__all__: list[str] = [
    "FlextTargetLdifConfig",
]
