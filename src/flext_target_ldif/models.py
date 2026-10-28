# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models for LDIF target operations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import m
from flext_meltano import m as flext_meltano_m

from flext_target_ldif._models import FlextModelsTargetLdifConfig


class FlextModelsTargetLdif(FlextModelsTargetLdifConfig, flext_meltano_m, m):
    """Models composed from Meltano and LDIF via MRO."""


m = FlextModelsTargetLdif
__all__: list[str] = ["FlextModelsTargetLdif", "m"]
