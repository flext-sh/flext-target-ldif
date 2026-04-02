"""FLEXT service orchestrator for target-ldif.

Thin facade — all infrastructure from ``FlextMeltanoTargetServiceBase`` via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_meltano import FlextMeltanoSingerSinkBase, FlextMeltanoTargetServiceBase

from flext_target_ldif import FlextTargetLdifModels, t


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
        target_config = self.settings.model_dump() if self.settings else {}
        return FlextTargetLdifModels.TargetLdif.Sink(
            target_config=target_config,
            stream_name=stream_name,
            schema=schema,
        )


__all__ = ["FlextTargetLdifService"]
