"""Module skeleton for TestsFlextTargetLdifConstants.

Test constants for flext-target-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_target_ldif import FlextTargetLdifConstants


class TestsFlextTargetLdifConstants(FlextTestsConstants, FlextTargetLdifConstants):
    """Test constants for flext-target-ldif."""


c = TestsFlextTargetLdifConstants

__all__: list[str] = ["TestsFlextTargetLdifConstants", "c"]
