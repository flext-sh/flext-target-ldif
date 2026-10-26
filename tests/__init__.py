# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import (
        api,
        config,
        d,
        e,
        h,
        install_local_packages,
        r,
        settings,
        td,
        tf,
        tk,
        tm,
        x,
    )

    from flext_target_ldif import cli, ldif, main, meltano, target_ldif
    from tests.base import TestsFlextTargetLdifServiceBase, s
    from tests.constants import TestsFlextTargetLdifConstants, c
    from tests.models import TestsFlextTargetLdifModels, m
    from tests.protocols import TestsFlextTargetLdifProtocols, p
    from tests.settings import TestsFlextTargetLdifSettings
    from tests.typings import TestsFlextTargetLdifTypes, t
    from tests.utilities import TestsFlextTargetLdifUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
    "TestsFlextTargetLdifServiceBase",
    "TestsFlextTargetLdifSettings",
    "TestsFlextTargetLdifTypes",
    "TestsFlextTargetLdifUtilities",
    "api",
    "c",
    "cli",
    "config",
    "d",
    "e",
    "h",
    "install_local_packages",
    "ldif",
    "m",
    "main",
    "meltano",
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
    MappingProxyType({
        "TestsFlextTargetLdifConstants": ".constants",
        "TestsFlextTargetLdifModels": ".models",
        "TestsFlextTargetLdifProtocols": ".protocols",
        "TestsFlextTargetLdifServiceBase": ".base",
        "TestsFlextTargetLdifSettings": ".settings",
        "TestsFlextTargetLdifTypes": ".typings",
        "TestsFlextTargetLdifUtilities": ".utilities",
        "api": "flext_tests",
        "c": ".constants",
        "cli": "flext_target_ldif",
        "config": "flext_tests",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "install_local_packages": "flext_tests",
        "ldif": "flext_target_ldif",
        "m": ".models",
        "main": "flext_target_ldif",
        "meltano": "flext_target_ldif",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_tests",
        "t": ".typings",
        "target_ldif": "flext_target_ldif",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    }),
    public_exports=__all__,
)
