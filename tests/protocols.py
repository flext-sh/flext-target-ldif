"""Test protocol definitions for flext-target-ldif.

Provides FlextTargetLdifTestProtocols, combining FlextTestsProtocols with
FlextTargetLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_target_ldif.protocols import FlextTargetLdifProtocols


class FlextTargetLdifTestProtocols(FlextTestsProtocols, FlextTargetLdifProtocols):
    """Test protocols combining FlextTestsProtocols and FlextTargetLdifProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.TargetLdif.* (from FlextTargetLdifProtocols)
    """


p = FlextTargetLdifTestProtocols
__all__ = ["FlextTargetLdifTestProtocols", "p"]
