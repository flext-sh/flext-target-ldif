"""Utilities for flext-target-ldif tests - uses u.TargetLdif.Tests.* namespace pattern.

This module provides test-specific utilities that extend the main flext-target-ldif utilities.
Uses the unified namespace pattern u.TargetLdif.Tests.* for test-only objects.
Combines FlextTestsUtilities functionality with project-specific test utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_target_ldif.utilities import FlextTargetLdifUtilities
from flext_tests import FlextTestsUtilities


class TestsFlextTargetLdifUtilities(FlextTestsUtilities, FlextTargetLdifUtilities):
    """Test utilities for flext-target-ldif extending both test and project utilities."""


u = TestsFlextTargetLdifUtilities

__all__ = ["TestsFlextTargetLdifUtilities", "u"]
