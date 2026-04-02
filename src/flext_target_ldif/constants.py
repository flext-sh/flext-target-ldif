"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Final

from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants


class FlextTargetLdifConstants(FlextMeltanoConstants, FlextLdifConstants):
    """LDIF target export-specific constants following flext-core patterns."""

    STANDARD_LINE_LENGTH: Final[int] = 78
    ASCII_SPACE: Final[int] = 32
    ASCII_TILDE: Final[int] = 126
    LDIF_LINE_WRAP_LENGTH: Final[int] = 76


c = FlextTargetLdifConstants
__all__ = ["FlextTargetLdifConstants", "c"]
