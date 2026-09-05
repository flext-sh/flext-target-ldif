# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif. Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .service_runtime import FlextTargetLdifServiceRuntime
__all__: tuple[str, ...] = ("FlextTargetLdifServiceRuntime",)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({".service_runtime": ("FlextTargetLdifServiceRuntime",)}),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
