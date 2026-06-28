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
    from flext_tests import td as td, tf as tf, tk as tk, tv as tv

    from flext_target_ldif import d as d, e as e, h as h, r as r, x as x
    from tests.base import (
        TestsFlextTargetLdifServiceBase as TestsFlextTargetLdifServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextTargetLdifConstants as TestsFlextTargetLdifConstants,
        c as c,
    )
    from tests.models import (
        TestsFlextTargetLdifModels as TestsFlextTargetLdifModels,
        m as m,
    )
    from tests.protocols import (
        TestsFlextTargetLdifProtocols as TestsFlextTargetLdifProtocols,
        p as p,
    )
    from tests.settings import (
        TestsFlextTargetLdifSettings as TestsFlextTargetLdifSettings,
    )
    from tests.typings import (
        TestsFlextTargetLdifTypes as TestsFlextTargetLdifTypes,
        t as t,
    )
    from tests.unit.test_target import (
        TestsFlextTargetLdifTarget as TestsFlextTargetLdifTarget,
    )
    from tests.unit.test_writer import (
        TestsFlextTargetLdifWriter as TestsFlextTargetLdifWriter,
    )
    from tests.utilities import (
        TestsFlextTargetLdifUtilities as TestsFlextTargetLdifUtilities,
        u as u,
    )
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
    "tv",
    "u",
    "x",
]
