"""FLEXT service orchestrator for target-ldif.

Thin facade — all infrastructure from ``FlextMeltanoTargetServiceBase`` via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from typing import Annotated, override

from flext_meltano import FlextMeltanoTargetServiceBase

from flext_target_ldif import (
    FlextTargetLdifServiceRuntime,
    p,
    t,
    u,
)


class FlextTargetLdifService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-ldif. All behavior from base via MRO."""

    target_name: Annotated[
        t.NonEmptyStr,
        u.Field(default="target-ldif", description="Singer target name"),
    ]

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.FlatContainerMapping,
    ) -> p.Meltano.SingerDrainSink:
        """Create an LDIF sink for a stream."""
        target_config: Mapping[str, t.Container] = self.settings_overrides or {}
        return FlextTargetLdifServiceRuntime.create_sink(
            stream_name=stream_name,
            schema=schema,
            target_config=target_config,
        )


target_ldif = FlextTargetLdifService

__all__: list[str] = ["FlextTargetLdifService", "target_ldif"]
