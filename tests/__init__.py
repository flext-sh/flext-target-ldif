# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import d, e, h, r, s, td, tf, tk, tm, tv, x

    from tests.constants import TestsFlextTargetLdifConstants, c
    from tests.models import TestsFlextTargetLdifModels, m
    from tests.protocols import TestsFlextTargetLdifProtocols, p
    from tests.typings import TestsFlextTargetLdifTypes, t
    from tests.utilities import TestsFlextTargetLdifUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".constants": (
                "TestsFlextTargetLdifConstants",
                "c",
            ),
            ".models": (
                "TestsFlextTargetLdifModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextTargetLdifProtocols",
                "p",
            ),
            ".typings": (
                "TestsFlextTargetLdifTypes",
                "t",
            ),
            ".utilities": (
                "TestsFlextTargetLdifUtilities",
                "u",
            ),
            "flext_tests": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__ = [
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
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
    "x",
]
