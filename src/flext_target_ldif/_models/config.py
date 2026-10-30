"""Validated TargetLdif config models for flext-target-ldif.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m


class FlextModelsTargetLdifConfig:
    """Field-only declarations for the TargetLdif config singleton."""

    class ConfigRoot(m.FrozenModel):
        """Validated root loaded by the private config composition."""

        model_config = m.ConfigDict(frozen=True, extra="ignore")

        class ConfigNamespace(m.BaseModel):
            """Open namespace loaded from ``config/target_ldif.yaml``."""

            model_config = m.ConfigDict(frozen=True, extra="allow")

        TargetLdif: ConfigNamespace = m.Field(
            description="Open namespace exposing ``config/*.yaml`` under TargetLdif.",
        )


__all__: list[str] = ["FlextModelsTargetLdifConfig"]
