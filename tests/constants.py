"""Module skeleton for TestsFlextTargetLdifConstants.

Test constants for flext-target-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_tests import FlextTestsConstants

from flext_target_ldif import FlextTargetLdifConstants


class TestsFlextTargetLdifConstants(FlextTestsConstants, FlextTargetLdifConstants):
    """Test constants for flext-target-ldif."""

    class TargetLdif(FlextTargetLdifConstants.TargetLdif):
        """Target LDIF domain test constants namespace."""

        class Tests(FlextTestsConstants.Tests):
            """Target LDIF-specific test constants."""

            EXPECTED_BULK_SIZE: Final[int] = 2
            EXPECTED_DATA_COUNT: Final[int] = 3


c = TestsFlextTargetLdifConstants

__all__: list[str] = ["TestsFlextTargetLdifConstants", "c"]
