"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants

from ._constants.base import FlextTargetLdifConstantsBase
from ._constants.values import FlextTargetLdifConstantsValues

if TYPE_CHECKING:
    from flext_meltano import t


class FlextTargetLdifConstants(FlextMeltanoConstants, FlextLdifConstants):
    """LDIF target export-specific constants following flext-core patterns."""

    class TargetLdif(
        FlextTargetLdifConstantsBase, FlextTargetLdifConstantsValues.TargetLdif
    ):
        """Target LDIF domain constants namespace."""


c = FlextTargetLdifConstants

__all__: t.StrSequence = ("FlextTargetLdifConstants", "c")
