"""Test models for flext-target-ldif tests.

Provides FlextTargetLdifTestModels, extending FlextTestsModels with
flext-target-ldif-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_target_ldif.models import FlextTargetLdifModels


class FlextTargetLdifTestModels(FlextTestsModels, FlextTargetLdifModels):
    """Models for flext-target-ldif tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextTargetLdifModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.* (Target LDIF domain models)
    - m.* (production models via alternative alias)
    """


# Short aliases per FLEXT convention
tm = FlextTargetLdifTestModels
m = FlextTargetLdifTestModels

__all__ = [
    "FlextTargetLdifTestModels",
    "m",
    "tm",
]
