"""FLEXT Target LDIF Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import t as _ldif_t
from flext_meltano import t


class FlextTargetLdifTypes(t, _ldif_t):
    """MRO facade composing Meltano + Ldif type namespaces."""


t = FlextTargetLdifTypes

__all__: list[str] = ["FlextTargetLdifTypes", "t"]
