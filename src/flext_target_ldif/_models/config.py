"""flext-target-ldif config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/target_ldif.yaml`` business-rule SSOT.
The ``_config.py`` facade validates the model-less YAML slice into these
classes and exposes the ready objects under ``config.TargetLdif``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FlextTargetLdifConfigModels:
    """Namespace of typed flext-target-ldif config models."""

    class Output(BaseModel):
        """LDIF output file defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        file: str = Field(description="Default output LDIF filename.")
        path: str = Field(description="Default output directory path.")
        naming_pattern: str = Field(
            description="Pattern for generated LDIF filenames.",
        )

    class Dn(BaseModel):
        """LDIF DN construction defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        template: str = Field(description="Template used to build entry DN values.")

    class Formatting(BaseModel):
        """LDIF formatting defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        line_length: int = Field(
            ge=1,
            description="LDIF line wrap length.",
        )
        line_wrap_length: int = Field(
            ge=1,
            description="LDIF physical line wrap length.",
        )
        base64_encode: bool = Field(
            description="Whether to force base64 encoding for all values.",
        )
        include_timestamps: bool = Field(
            description="Whether to include timestamp metadata in entries.",
        )

    class Validation(BaseModel):
        """LDIF validation defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        schema_validation: bool = Field(
            description="Whether to enable schema validation for transformed records.",
        )

    class TargetLdif(BaseModel):
        """Root LDIF target business-rule namespace."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        output: FlextTargetLdifConfigModels.Output = Field(
            description="LDIF output file defaults.",
        )
        dn: FlextTargetLdifConfigModels.Dn = Field(
            description="LDIF DN construction defaults.",
        )
        formatting: FlextTargetLdifConfigModels.Formatting = Field(
            description="LDIF formatting defaults.",
        )
        validation: FlextTargetLdifConfigModels.Validation = Field(
            description="LDIF validation defaults.",
        )

    class Root(BaseModel):
        """Root flext-target-ldif config validated from ``config/*.yaml``."""

        model_config = ConfigDict(frozen=True, extra="ignore")

        TargetLdif: FlextTargetLdifConfigModels.TargetLdif = Field(
            description="LDIF target business-rule config namespace.",
        )


__all__: list[str] = ["FlextTargetLdifConfigModels"]
