# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models for LDIF target operations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels

from flext_target_ldif._models import FlextTargetLdifConfigModels


class FlextTargetLdifModels(
    FlextTargetLdifConfigModels, FlextMeltanoModels, FlextLdifModels
):
    """Models composed from Meltano and LDIF via MRO."""


m = FlextTargetLdifModels

__all__: list[str] = ["FlextTargetLdifModels", "m"]
