# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from typing import Final

    from flext_target_ldif import FlextTargetLdifConstants
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x

    from . import unit as unit
    from .base import (
        TestsFlextTargetLdifServiceBase,
        TestsFlextTargetLdifServiceBase as s,
    )
    from .constants import (
        TestsFlextTargetLdifConstants,
        TestsFlextTargetLdifConstants as c,
    )
    from .models import TestsFlextTargetLdifModels, TestsFlextTargetLdifModels as m
    from .protocols import (
        TestsFlextTargetLdifProtocols,
        TestsFlextTargetLdifProtocols as p,
    )
    from .settings import TestsFlextTargetLdifSettings
    from .typings import TestsFlextTargetLdifTypes, TestsFlextTargetLdifTypes as t
    from .utilities import (
        TestsFlextTargetLdifUtilities,
        TestsFlextTargetLdifUtilities as u,
    )
__all__: tuple[str, ...] = (
    "Final",
    "FlextTargetLdifConstants",
    "FlextTestsConstants",
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
    "TestsFlextTargetLdifServiceBase",
    "TestsFlextTargetLdifSettings",
    "TestsFlextTargetLdifTypes",
    "TestsFlextTargetLdifUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextTargetLdifServiceBase", "s"),
            ".constants": ("TestsFlextTargetLdifConstants", "c"),
            ".models": ("TestsFlextTargetLdifModels", "m"),
            ".protocols": ("TestsFlextTargetLdifProtocols", "p"),
            ".settings": ("TestsFlextTargetLdifSettings",),
            ".typings": ("TestsFlextTargetLdifTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextTargetLdifUtilities", "u"),
            "flext_target_ldif": ("FlextTargetLdifConstants",),
            "flext_tests": (
                "FlextTestsConstants",
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
            "typing": ("Final",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
