# AUTO-GENERATED FILE — Regenerate with: make gen
"""Singer target utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import u as flext_ldif_u
from flext_meltano import u as flext_meltano_u

from flext_target_ldif._utilities import (
    FlextTargetLdifServiceRuntime,
    FlextTargetLdifSink,
)


class FlextTargetLdifUtilities(
    FlextTargetLdifServiceRuntime,
    FlextTargetLdifSink,
    flext_meltano_u,
    flext_ldif_u,
):
    """Utilities composed from Meltano and LDIF via MRO."""


u = FlextTargetLdifUtilities
__all__: list[str] = ["FlextTargetLdifUtilities", "u"]
