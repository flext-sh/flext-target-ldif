# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from flext_target_ldif import (
        FlextTargetLdif,
        FlextTargetLdifCli,
        FlextTargetLdifConfig,
        FlextTargetLdifConstants,
        FlextTargetLdifModels,
        FlextTargetLdifProtocols,
        FlextTargetLdifService,
        FlextTargetLdifServiceRuntime,
        FlextTargetLdifSettings,
        FlextTargetLdifSink,
        FlextTargetLdifTypes,
        FlextTargetLdifUtilities,
        FlextTargetLdifVersion,
        FlextTargetLdifWriter,
        FlextTargetLdifWriterError,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        config,
        main,
        settings,
        target_ldif,
    )
    from tests.base import TestsFlextTargetLdifServiceBase, s
    from tests.constants import TestsFlextTargetLdifConstants, c
    from tests.models import TestsFlextTargetLdifModels, m
    from tests.protocols import TestsFlextTargetLdifProtocols, p
    from tests.settings import TestsFlextTargetLdifSettings
    from tests.typings import TestsFlextTargetLdifTypes, t
    from tests.utilities import TestsFlextTargetLdifUtilities, u


__all__: tuple[str, ...] = (
    "FlextTargetLdif",
    "FlextTargetLdifCli",
    "FlextTargetLdifConfig",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifService",
    "FlextTargetLdifServiceRuntime",
    "FlextTargetLdifSettings",
    "FlextTargetLdifSink",
    "FlextTargetLdifTypes",
    "FlextTargetLdifUtilities",
    "FlextTargetLdifVersion",
    "FlextTargetLdifWriter",
    "FlextTargetLdifWriterError",
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
    "TestsFlextTargetLdifServiceBase",
    "TestsFlextTargetLdifSettings",
    "TestsFlextTargetLdifTypes",
    "TestsFlextTargetLdifUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "target_ldif",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextTargetLdif": "flext_target_ldif",
        "FlextTargetLdifCli": "flext_target_ldif",
        "FlextTargetLdifConfig": "flext_target_ldif",
        "FlextTargetLdifConstants": "flext_target_ldif",
        "FlextTargetLdifModels": "flext_target_ldif",
        "FlextTargetLdifProtocols": "flext_target_ldif",
        "FlextTargetLdifService": "flext_target_ldif",
        "FlextTargetLdifServiceRuntime": "flext_target_ldif",
        "FlextTargetLdifSettings": "flext_target_ldif",
        "FlextTargetLdifSink": "flext_target_ldif",
        "FlextTargetLdifTypes": "flext_target_ldif",
        "FlextTargetLdifUtilities": "flext_target_ldif",
        "FlextTargetLdifVersion": "flext_target_ldif",
        "FlextTargetLdifWriter": "flext_target_ldif",
        "FlextTargetLdifWriterError": "flext_target_ldif",
        "TestsFlextTargetLdifConstants": ".constants",
        "TestsFlextTargetLdifModels": ".models",
        "TestsFlextTargetLdifProtocols": ".protocols",
        "TestsFlextTargetLdifServiceBase": ".base",
        "TestsFlextTargetLdifSettings": ".settings",
        "TestsFlextTargetLdifTypes": ".typings",
        "TestsFlextTargetLdifUtilities": ".utilities",
        "__author__": "flext_target_ldif",
        "__author_email__": "flext_target_ldif",
        "__description__": "flext_target_ldif",
        "__license__": "flext_target_ldif",
        "__title__": "flext_target_ldif",
        "__url__": "flext_target_ldif",
        "__version__": "flext_target_ldif",
        "__version_info__": "flext_target_ldif",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_target_ldif",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_target_ldif",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_target_ldif",
        "t": ".typings",
        "target_ldif": "flext_target_ldif",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
