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
    from flext_cli.base import s
    from flext_tests._fixtures.settings import (
        reset_settings,
        settings,
        settings_factory,
    )
    from flext_tests._utilities.matchers import tm
    from flext_tests.docker import tk
    from flext_tests.domains import td
    from flext_tests.files import tf
    from flext_tests.validator import tv

    from flext_core.decorators import d
    from flext_core.exceptions import e
    from flext_core.handlers import h
    from flext_core.mixins import x
    from flext_core.result import r
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
            "flext_cli.base": ("s",),
            "flext_core.decorators": ("d",),
            "flext_core.exceptions": ("e",),
            "flext_core.handlers": ("h",),
            "flext_core.mixins": ("x",),
            "flext_core.result": ("r",),
            "flext_tests._fixtures.settings": (
                "reset_settings",
                "settings",
                "settings_factory",
            ),
            "flext_tests._utilities.matchers": ("tm",),
            "flext_tests.docker": ("tk",),
            "flext_tests.domains": ("td",),
            "flext_tests.files": ("tf",),
            "flext_tests.validator": ("tv",),
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
    "reset_settings",
    "s",
    "settings",
    "settings_factory",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "x",
]
