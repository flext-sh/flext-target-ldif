"""Test protocols module for flext-target-ldif.

Provides p alias for test protocols with namespace p.Ldif.Tests.* pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from .protocols import TestsFlextTargetLdifProtocols

# Runtime alias for test protocols
p = TestsFlextTargetLdifProtocols

__all__ = [
    "p",
]
