"""Test protocol definitions for flext-target-ldif.

Provides TestsFlextTargetLdifProtocols, combining FlextTestsProtocols with
FlextTargetLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_ldif.protocols import FlextTargetLdifProtocols
from flext_tests import FlextTestsProtocols


class TestsFlextTargetLdifProtocols(FlextTestsProtocols, FlextTargetLdifProtocols):
    """Test protocols combining FlextTestsProtocols and FlextTargetLdifProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.TargetLdif.* (from FlextTargetLdifProtocols)
    """

    pass


p = TestsFlextTargetLdifProtocols

__all__ = ["TestsFlextTargetLdifProtocols", "p"]
