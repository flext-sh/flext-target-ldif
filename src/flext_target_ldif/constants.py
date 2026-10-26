# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import c
from flext_meltano import c as flext_meltano_c

from flext_target_ldif._constants import (
    FlextTargetLdifConstantsBase,
    FlextTargetLdifConstantsValues,
)


class FlextTargetLdifConstants(flext_meltano_c, c):
    """LDIF target export-specific constants following flext-core patterns."""

    class TargetLdif(
        FlextTargetLdifConstantsBase,
        FlextTargetLdifConstantsValues,
    ):
        """Target LDIF domain constants namespace."""


c = FlextTargetLdifConstants
__all__: list[str] = ["FlextTargetLdifConstants", "c"]
