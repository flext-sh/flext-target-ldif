# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if TYPE_CHECKING:
    from flext_tests import (
        d as d,
        e as e,
        h as h,
        r as r,
        td as td,
        tf as tf,
        tk as tk,
        tm as tm,
        tv as tv,
        x as x,
    )

    from flext_target_ldif.tests.base import (
        TestsFlextTargetLdifServiceBase as TestsFlextTargetLdifServiceBase,
        s as s,
    )
    from flext_target_ldif.tests.constants import (
        TestsFlextTargetLdifConstants as TestsFlextTargetLdifConstants,
        c as c,
    )
    from flext_target_ldif.tests.models import (
        TestsFlextTargetLdifModels as TestsFlextTargetLdifModels,
        m as m,
    )
    from flext_target_ldif.tests.protocols import (
        TestsFlextTargetLdifProtocols as TestsFlextTargetLdifProtocols,
        p as p,
    )
    from flext_target_ldif.tests.settings import (
        TestsFlextTargetLdifSettings as TestsFlextTargetLdifSettings,
    )
    from flext_target_ldif.tests.typings import (
        TestsFlextTargetLdifTypes as TestsFlextTargetLdifTypes,
        t as t,
    )
    from flext_target_ldif.tests.unit.test_target import (
        TestsFlextTargetLdifTarget as TestsFlextTargetLdifTarget,
    )
    from flext_target_ldif.tests.unit.test_writer import (
        TestsFlextTargetLdifWriter as TestsFlextTargetLdifWriter,
    )
    from flext_target_ldif.tests.utilities import (
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
            ".conftest": ("conftest",),
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
            ".unit": ("unit",),
            ".unit.test_target": ("TestsFlextTargetLdifTarget",),
            ".unit.test_writer": ("TestsFlextTargetLdifWriter",),
            ".utilities": (
                "TestsFlextTargetLdifUtilities",
                "u",
            ),
            "flext_tests": (
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
