# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_target_ldif._utilities.service_runtime import (
        FlextTargetLdifServiceRuntime as FlextTargetLdifServiceRuntime,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".service_runtime": ("FlextTargetLdifServiceRuntime",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
