# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_ldif._utilities.service_runtime import (
        FlextTargetLdifServiceRuntime,
    )


__all__: tuple[str, ...] = ("FlextTargetLdifServiceRuntime",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"FlextTargetLdifServiceRuntime": ".service_runtime"}),
    public_exports=__all__,
)
