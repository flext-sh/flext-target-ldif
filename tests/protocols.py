"""Test protocol definitions for flext-target-ldif.

Provides TestsFlextTargetLdifProtocols, combining p with
FlextTargetLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_target_ldif.protocols import FlextTargetLdifProtocols


class TestsFlextTargetLdifProtocols(p, FlextTargetLdifProtocols):
    """Test protocols combining p and FlextTargetLdifProtocols.

    Provides access to:
    - p.Tests.Docker.* (from p)
    - p.Tests.Factory.* (from p)
    - p.TargetLdif.* (from FlextTargetLdifProtocols)
    """


p = TestsFlextTargetLdifProtocols
__all__ = ["TestsFlextTargetLdifProtocols", "p"]
