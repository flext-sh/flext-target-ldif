"""FlextTargetLdifConfig — frozen config singleton for flext-target-ldif (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``TargetLdif:`` key and
are exposed through the open ``config.TargetLdif`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TargetLdif.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m

from flext_target_ldif._models.config import FlextTargetLdifConfigModels


class FlextTargetLdifConfig(FlextMeltanoConfig):
    """TargetLdif config auto-loaded model-less from ``config/*.yaml``.

    MRO carries ``FlextSettings`` FIRST (ENFORCE-042); the class stays a frozen,
    YAML-validated config singleton.
    """

    TargetLdif: Annotated[
        FlextTargetLdifConfigModels.ConfigRoot.ConfigNamespace,
        m.Field(
            description=(
                "Open namespace exposing ``config/*.yaml`` under ``TargetLdif``."
            ),
        ),
    ] = FlextTargetLdifConfigModels.ConfigRoot.ConfigNamespace()


config: FlextTargetLdifConfig = FlextTargetLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton.

Exposed as ``from flext_target_ldif import config``.
"""

__all__: list[str] = ["FlextTargetLdifConfig", "config"]
