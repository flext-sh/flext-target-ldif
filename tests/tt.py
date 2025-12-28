"""Test types module for flext-target-ldif.

Provides tt alias for test types with namespace t.Ldif.Tests.* pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_target_ldif.tests.typings import TestsFlextTargetLdifTypes

# Runtime alias for test types
t = TestsFlextTargetLdifTypes

__all__ = [
    "t",
]
