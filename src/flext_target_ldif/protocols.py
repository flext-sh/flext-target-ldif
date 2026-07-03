"""Singer LDIF target protocols for FLEXT ecosystem.

The 6 inner ``TargetLdif.*`` Protocol classes that previously lived here had
**zero workspace consumers**. Per AGENTS.md §3.5 + STRICT YAGNI they were
deleted; the canonical ``FlextTargetLdifProtocols`` facade remains intact
(re-exported via ``p``) and inherits behaviour from the parent
``FlextMeltanoProtocols`` (``p``) + ``FlextLdifProtocols`` MRO chain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifProtocols
from flext_meltano import p as meltano_p


class FlextTargetLdifProtocols(meltano_p, FlextLdifProtocols):
    """Singer Target LDIF protocols facade — composes Meltano + LDIF."""


p = FlextTargetLdifProtocols
__all__: list[str] = ["FlextTargetLdifProtocols", "p"]
