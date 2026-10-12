# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_ldif._constants.values import FlextTargetLdifConstantsValues


__all__: tuple[str, ...] = ("FlextTargetLdifConstantsValues",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"FlextTargetLdifConstantsValues": ".values"}),
    public_exports=__all__,
)
