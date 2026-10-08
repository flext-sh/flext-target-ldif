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
    from flext_target_ldif._utilities.sink import FlextTargetLdifSink


__all__: tuple[str, ...] = ("FlextTargetLdifServiceRuntime", "FlextTargetLdifSink")

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTargetLdifServiceRuntime": ".service_runtime",
        "FlextTargetLdifSink": ".sink",
    }),
    public_exports=__all__,
)
