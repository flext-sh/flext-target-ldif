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
    from flext_tests import td, tf, tk, tm, tv

    from flext_target_ldif import d, e, h, r, x
    from tests.base import TestsFlextTargetLdifServiceBase, s
    from tests.constants import TestsFlextTargetLdifConstants, c
    from tests.models import TestsFlextTargetLdifModels, m
    from tests.protocols import TestsFlextTargetLdifProtocols, p
    from tests.settings import TestsFlextTargetLdifSettings
    from tests.typings import TestsFlextTargetLdifTypes, t
    from tests.unit.test_target import TestsFlextTargetLdifTarget
    from tests.unit.test_writer import TestsFlextTargetLdifWriter
    from tests.utilities import TestsFlextTargetLdifUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextTargetLdifServiceBase",
                "s",
            ),
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
            ".settings": ("TestsFlextTargetLdifSettings",),
            ".typings": (
                "TestsFlextTargetLdifTypes",
                "t",
            ),
            ".unit.test_target": ("TestsFlextTargetLdifTarget",),
            ".unit.test_writer": ("TestsFlextTargetLdifWriter",),
            ".utilities": (
                "TestsFlextTargetLdifUtilities",
                "u",
            ),
            "flext_target_ldif": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
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
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
    "TestsFlextTargetLdifServiceBase",
    "TestsFlextTargetLdifSettings",
    "TestsFlextTargetLdifTarget",
    "TestsFlextTargetLdifTypes",
    "TestsFlextTargetLdifUtilities",
    "TestsFlextTargetLdifWriter",
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
