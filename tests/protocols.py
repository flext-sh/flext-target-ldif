"""Test protocol definitions for flext-target-ldif.

Provides TestsFlextTargetLdifProtocols, combining FlextTestsProtocols with
FlextTargetLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_ldif.protocols import FlextTargetLdifProtocols
from flext_tests.protocols import FlextTestsProtocols


class TestsFlextTargetLdifProtocols(FlextTestsProtocols, FlextTargetLdifProtocols):
    """Test protocols combining FlextTestsProtocols and FlextTargetLdifProtocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.TargetLdif.* (from FlextTargetLdifProtocols)
    """

    class Tests:
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with TargetLdif-specific protocols.
        """

        class TargetLdif:
            """TargetLdif-specific test protocols."""


# Runtime aliases
p = TestsFlextTargetLdifProtocols
tp = TestsFlextTargetLdifProtocols

__all__ = ["TestsFlextTargetLdifProtocols", "p", "tp"]
