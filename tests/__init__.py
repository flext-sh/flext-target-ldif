# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_cli import cli
    from flext_infra import docs_main, infra
    from flext_ldif import ldif
    from flext_meltano import meltano
    from flext_tests import (
        active_rules,
        api,
        config,
        discover_repository_root,
        install_local_packages,
        load_infra_report,
        settings,
        split_csv,
        td,
        tf,
        tk,
        tm,
        tv,
    )
    from pydantic_core import from_json, to_json, to_jsonable_python

    from flext_core import core, d, e, h, lazy_attribute, r, x
    from flext_target_ldif import main, target_ldif

    from . import unit
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
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
    "TestsFlextTargetLdifServiceBase",
    "TestsFlextTargetLdifSettings",
    "TestsFlextTargetLdifTypes",
    "TestsFlextTargetLdifUtilities",
    "active_rules",
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "discover_repository_root",
    "docs_main",
    "e",
    "from_json",
    "h",
    "infra",
    "install_local_packages",
    "lazy_attribute",
    "ldif",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "settings",
    "split_csv",
    "t",
    "target_ldif",
    "td",
    "tf",
    "tk",
    "tm",
    "to_json",
    "to_jsonable_python",
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
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_infra": ("docs_main", "infra"),
            "flext_ldif": ("ldif",),
            "flext_meltano": ("meltano",),
            "flext_target_ldif": ("main", "target_ldif"),
            "flext_tests": (
                "active_rules",
                "api",
                "config",
                "discover_repository_root",
                "install_local_packages",
                "load_infra_report",
                "settings",
                "split_csv",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
            "pydantic_core": ("from_json", "to_json", "to_jsonable_python"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
