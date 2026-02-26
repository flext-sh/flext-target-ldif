"""Test models module for flext-target-ldif.

Provides tm alias for test models with namespace m.Ldif.Tests.* pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from .models import TestsFlextTargetLdifModels

# Runtime alias for test models
m = TestsFlextTargetLdifModels

__all__ = [
    "m",
]
