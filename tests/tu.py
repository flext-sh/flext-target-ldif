"""Test utilities module for flext-target-ldif.

Provides tu alias for test utilities with namespace u.Ldif.Tests.* pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_target_ldif.tests.utilities import (
    TestsFlextTargetLdifUtilities,
)

# Runtime alias for test utilities
u = TestsFlextTargetLdifUtilities

__all__ = [
    "u",
]
