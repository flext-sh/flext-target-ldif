"""Test models for flext-target-ldif tests.

Provides TestsFlextTargetLdifModels, extending TestsFlextModels with
flext-target-ldif-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_target_ldif import FlextTargetLdifModels


class TestsFlextTargetLdifModels(FlextTestsModels, FlextTargetLdifModels):
    """Models for flext-target-ldif tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. TestsFlextModels - for test infrastructure (.Tests.*)
    2. FlextTargetLdifModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from TestsFlextModels)
    - tm.* (Target LDIF domain models)
    - m.* (production models via alternative alias)
    """

    class Tests(FlextTestsModels.Tests):
        """Internal tests declarations."""


# Short aliases per FLEXT convention
m = TestsFlextTargetLdifModels

__all__: list[str] = [
    "TestsFlextTargetLdifModels",
    "m",
]
