"""FLEXT service orchestrator for target-ldif.

Thin facade over ``meltano.Target`` — all infrastructure from the base via MRO.
The sink factory is declared, never overridden.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_meltano import FlextMeltanoTargetServiceBase

from flext_target_ldif import c, m, p, t, u


class FlextTargetLdifService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-ldif. All behavior from base via MRO."""

    target_name: Annotated[t.NonEmptyStr, m.Field(description="Singer target name")] = (
        c.TargetLdif.TARGET_NAME
    )

    sink_factory: ClassVar[p.Meltano.SinkFactory] = u.create_sink


target_ldif: FlextTargetLdifService = FlextTargetLdifService.fetch_global()
"""Shared FlextTargetLdifService facade instance."""

__all__: list[str] = ["FlextTargetLdifService", "target_ldif"]
