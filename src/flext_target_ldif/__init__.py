# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
from flext_target_ldif.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_ldif import d, e, h, r, s, x

    from ._config import FlextTargetLdifConfig, config
    from ._settings import FlextTargetLdifSettings, settings
    from .api import FlextTargetLdifService, target_ldif
    from .cli import FlextTargetLdifCli, main
    from .constants import FlextTargetLdifConstants, FlextTargetLdifConstants as c
    from .models import FlextTargetLdifModels, FlextTargetLdifModels as m
    from .protocols import FlextTargetLdifProtocols, FlextTargetLdifProtocols as p
    from .typings import FlextTargetLdifTypes, FlextTargetLdifTypes as t
    from .utilities import FlextTargetLdifUtilities, FlextTargetLdifUtilities as u

    _ = (
        c,
        FlextTargetLdifConstants,
        t,
        FlextTargetLdifTypes,
        p,
        FlextTargetLdifProtocols,
        m,
        FlextTargetLdifModels,
        u,
        FlextTargetLdifUtilities,
        d,
        e,
        h,
        r,
        s,
        x,
        main,
        FlextTargetLdifCli,
        FlextTargetLdifConfig,
        config,
        FlextTargetLdifSettings,
        settings,
        FlextTargetLdifService,
        target_ldif,
    )


_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": (
        "FlextTargetLdifConfig",
        "config",
    ),
    "._settings": (
        "FlextTargetLdifSettings",
        "settings",
    ),
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
    ".models": (
        "FlextTargetLdifModels",
        "m",
    ),
    ".protocols": (
        "FlextTargetLdifProtocols",
        "p",
    ),
    ".typings": (
        "FlextTargetLdifTypes",
        "t",
    ),
    ".utilities": (
        "FlextTargetLdifUtilities",
        "u",
    ),
    "flext_ldif": (
        "d",
        "e",
        "h",
        "r",
        "s",
        "x",
    ),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES,
    alias_groups=_LAZY_ALIAS_GROUPS,
    sort_keys=False,
)

_DIRECT_IMPORTS: tuple[str, ...] = (
    "FlextTargetLdifCli",
    "FlextTargetLdifConfig",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifService",
    "FlextTargetLdifSettings",
    "FlextTargetLdifTypes",
    "FlextTargetLdifUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "build_lazy_import_map",
    "c",
    "config",
    "d",
    "e",
    "h",
    "install_lazy_exports",
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
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
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
    _LAZY_IMPORTS,
    public_exports=__all__,
)
