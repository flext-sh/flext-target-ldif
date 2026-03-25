"""Module skeleton for FlextTargetLdifTestConstants.

Test constants for flext-target-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_target_ldif import FlextTargetLdifConstants


class FlextTargetLdifTestConstants(FlextTestsConstants, FlextTargetLdifConstants):
    """Test constants for flext-target-ldif."""


c = FlextTargetLdifTestConstants
__all__ = ["FlextTargetLdifTestConstants", "c"]
