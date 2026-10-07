"""FLEXT service orchestrator for target-ldif.

Thin facade over ``meltano.Target`` — all infrastructure from the base via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import meltano

from flext_target_ldif import c, p, t, u
from flext_target_ldif._utilities.service_runtime import FlextTargetLdifServiceRuntime


class FlextTargetLdifService(meltano.Target):
    """Orchestrator for target-ldif. All behavior from base via MRO."""

    target_name: Annotated[t.NonEmptyStr, u.Field(description="Singer target name")] = (
        c.TargetLdif.TARGET_NAME
    )

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.JsonMapping,
    ) -> p.Meltano.SingerDrainSink:
        """Create an LDIF sink for a stream.

        Returns:
            The resulting ``p.Meltano.SingerDrainSink``.
        """
        target_config: t.ScalarMapping = self.settings_overrides or {}
        return FlextTargetLdifServiceRuntime.create_sink(
            stream_name=stream_name,
            schema=schema,
            target_config=target_config,
        )


target_ldif: FlextTargetLdifService = FlextTargetLdifService.fetch_global()
"""Shared FlextTargetLdifService facade instance."""

__all__: list[str] = ["FlextTargetLdifService", "target_ldif"]
