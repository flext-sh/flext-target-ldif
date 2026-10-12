# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports
from flext_target_ldif.__version__ import __version__

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x

    from flext_target_ldif import _constants, _utilities
    from flext_target_ldif.__version__ import (
        FlextTargetLdifVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version_info__,
    )
    from flext_target_ldif._config import FlextTargetLdifConfig, config
    from flext_target_ldif._settings import FlextTargetLdifSettings, settings
    from flext_target_ldif.api import FlextTargetLdifService, target_ldif
    from flext_target_ldif.cli import FlextTargetLdifCli, main
    from flext_target_ldif.constants import FlextTargetLdifConstants, c
    from flext_target_ldif.errors import FlextTargetLdifWriterError
    from flext_target_ldif.models import FlextTargetLdifModels, m
    from flext_target_ldif.protocols import FlextTargetLdifProtocols, p
    from flext_target_ldif.typings import FlextTargetLdifTypes, t
    from flext_target_ldif.utilities import FlextTargetLdifUtilities, u
    from flext_target_ldif.writer import FlextTargetLdifWriter


__all__: tuple[str, ...] = (
    "FlextTargetLdifCli",
    "FlextTargetLdifConfig",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifService",
    "FlextTargetLdifSettings",
    "FlextTargetLdifTypes",
    "FlextTargetLdifUtilities",
    "FlextTargetLdifVersion",
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
    "_constants",
    "_utilities",
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
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTargetLdifCli": ".cli",
        "FlextTargetLdifConfig": "._config",
        "FlextTargetLdifConstants": ".constants",
        "FlextTargetLdifModels": ".models",
        "FlextTargetLdifProtocols": ".protocols",
        "FlextTargetLdifService": ".api",
        "FlextTargetLdifSettings": "._settings",
        "FlextTargetLdifTypes": ".typings",
        "FlextTargetLdifUtilities": ".utilities",
        "FlextTargetLdifVersion": ".__version__",
        "FlextTargetLdifWriter": ".writer",
        "FlextTargetLdifWriterError": ".errors",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "_constants": "._constants",
        "_utilities": "._utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "settings": "._settings",
        "t": ".typings",
        "target_ldif": ".api",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)
