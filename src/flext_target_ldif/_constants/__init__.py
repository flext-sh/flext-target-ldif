# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif. Constants package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .base import FlextTargetLdifConstantsBase
    from .values import FlextTargetLdifConstantsValues


__all__: tuple[str, ...] = (
    "FlextTargetLdifConstantsBase",
    "FlextTargetLdifConstantsValues",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("FlextTargetLdifConstantsBase",),
            ".values": ("FlextTargetLdifConstantsValues",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
