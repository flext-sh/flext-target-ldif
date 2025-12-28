"""Types for flext-target-ldif tests - uses t.TargetLdif.Tests.* namespace pattern.

This module provides test-specific types that extend the main flext-target-ldif types.
Uses the unified namespace pattern t.TargetLdif.Tests.* for test-only objects.
Combines FlextTestsTypes functionality with project-specific test types.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_target_ldif.typings import FlextTargetLdifTypes


class TestsFlextTargetLdifTypes(FlextTestsTypes, FlextTargetLdifTypes):
    """Test types for flext-target-ldif extending both test and project types."""

    class TargetLdif(FlextTargetLdifTypes.TargetLdif):
        """TargetLdif test namespace."""

        class Tests:
            """Internal tests declarations."""


t = TestsFlextTargetLdifTypes
tt = TestsFlextTargetLdifTypes

__all__ = ["TestsFlextTargetLdifTypes", "t", "tt"]
