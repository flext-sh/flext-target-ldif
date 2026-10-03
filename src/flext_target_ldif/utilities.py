"""Singer target utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities


class FlextTargetLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Utilities composed from Meltano and LDIF via MRO."""


u = FlextTargetLdifUtilities

__all__: list[str] = ["FlextTargetLdifUtilities", "u"]
