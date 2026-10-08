"""Models for LDIF target operations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_ldif/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels


class FlextTargetLdifModels(FlextMeltanoModels, FlextLdifModels):
    """Models composed from Meltano and LDIF via MRO."""


m = FlextTargetLdifModels

__all__: list[str] = ["FlextTargetLdifModels", "m"]
