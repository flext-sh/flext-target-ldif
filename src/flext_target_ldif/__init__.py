# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_target_ldif.__version__ import *

if _t.TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x
    from flext_target_ldif._utilities.service_runtime import (
        FlextTargetLdifServiceRuntime,
    )
    from flext_target_ldif.api import FlextTargetLdifService, target_ldif
    from flext_target_ldif.cli import FlextTargetLdifCli, main
    from flext_target_ldif.constants import FlextTargetLdifConstants, c
    from flext_target_ldif.errors import FlextTargetLdifWriterError
    from flext_target_ldif.models import FlextTargetLdifModels, m
    from flext_target_ldif.protocols import FlextTargetLdifProtocols, p
    from flext_target_ldif.settings import FlextTargetLdifSettings
    from flext_target_ldif.target import FlextTargetLdif
    from flext_target_ldif.typings import FlextTargetLdifTypes, t
    from flext_target_ldif.utilities import FlextTargetLdifUtilities, u
    from flext_target_ldif.writer import FlextTargetLdifWriter
_LAZY_IMPORTS = merge_lazy_imports(
    ("._utilities",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            "._utilities.service_runtime": ("FlextTargetLdifServiceRuntime",),
            ".api": (
                "FlextTargetLdifService",
                "target_ldif",
            ),
            ".cli": (
                "FlextTargetLdifCli",
                "main",
            ),
            ".constants": (
                "FlextTargetLdifConstants",
                "c",
            ),
            ".errors": ("FlextTargetLdifWriterError",),
            ".models": (
                "FlextTargetLdifModels",
                "m",
            ),
            ".protocols": (
                "FlextTargetLdifProtocols",
                "p",
            ),
            ".settings": ("FlextTargetLdifSettings",),
            ".target": ("FlextTargetLdif",),
            ".typings": (
                "FlextTargetLdifTypes",
                "t",
            ),
            ".utilities": (
                "FlextTargetLdifUtilities",
                "u",
            ),
            ".writer": ("FlextTargetLdifWriter",),
            "flext_meltano": (
                "d",
                "e",
                "h",
                "r",
                "s",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "FlextTargetLdif",
    "FlextTargetLdifCli",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifService",
    "FlextTargetLdifServiceRuntime",
    "FlextTargetLdifSettings",
    "FlextTargetLdifTypes",
    "FlextTargetLdifUtilities",
    "FlextTargetLdifWriter",
    "FlextTargetLdifWriterError",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "target_ldif",
    "u",
    "x",
]
