"""Test protocol definitions for flext-target-ldif.

Provides TestsFlextTargetLdifProtocols, combining TestsFlextProtocols with
FlextTargetLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_target_ldif import FlextTargetLdifProtocols


class TestsFlextTargetLdifProtocols(FlextTestsProtocols, FlextTargetLdifProtocols):
    """Test protocols combining TestsFlextProtocols and FlextTargetLdifProtocols.

    Provides access to:
    - p.Tests.Docker.* (from TestsFlextProtocols)
    - p.Tests.Factory.* (from TestsFlextProtocols)
    - p.TargetLdif.* (from FlextTargetLdifProtocols)
    """

    class Tests(FlextTestsProtocols.Tests):
        """Internal tests declarations."""


p = TestsFlextTargetLdifProtocols

__all__: list[str] = ["TestsFlextTargetLdifProtocols", "p"]
