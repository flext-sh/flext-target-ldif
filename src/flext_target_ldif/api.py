"""FLEXT service orchestrator for target-ldif.

Thin facade — all infrastructure from ``FlextMeltanoTargetServiceBase`` via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_meltano import FlextMeltanoSingerSinkBase, FlextMeltanoTargetServiceBase

from flext_target_ldif import t
from flext_target_ldif._utilities.service_runtime import FlextTargetLdifServiceRuntime


class FlextTargetLdifService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-ldif. All behavior from base via MRO."""

    target_name: t.NonEmptyStr = "target-ldif"

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.FlatContainerMapping,
    ) -> FlextMeltanoSingerSinkBase:
        """Create an LDIF sink for a stream."""
        target_config: t.ContainerMapping = (
            self.config_overrides if self.config_overrides is not None else {}
        )
        return FlextTargetLdifServiceRuntime.create_sink(
            stream_name=stream_name,
            schema=schema,
            target_config=target_config,
        )


__all__ = ["FlextTargetLdifService"]
