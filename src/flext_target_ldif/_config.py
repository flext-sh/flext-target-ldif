"""FlextTargetLdifConfig — frozen config singleton for flext-target-ldif (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``TargetLdif:`` key and
are exposed through the open ``config.TargetLdif`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TargetLdif.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from flext_meltano import FlextMeltanoConfig


class _TargetLdifNamespace(BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = ConfigDict(extra="allow", frozen=True)


class FlextTargetLdifConfig(FlextMeltanoConfig):
    """TargetLdif config auto-loaded model-less from ``config/*.yaml``."""

    TargetLdif: _TargetLdifNamespace = _TargetLdifNamespace()


config: FlextTargetLdifConfig = FlextTargetLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_target_ldif import config``."""

__all__: list[str] = ["FlextTargetLdifConfig", "config"]
