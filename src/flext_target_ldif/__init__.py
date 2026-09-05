# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from typing import TYPE_CHECKING, Final

    from flext_ldif import FlextLdifConstants, d, e, h, r, s, x

    from ._config import FlextTargetLdifConfig, config
    from ._settings import FlextTargetLdifSettings, settings
    from .api import FlextTargetLdifService, target_ldif
    from .cli import FlextTargetLdifCli, main
    from .constants import FlextTargetLdifConstants, FlextTargetLdifConstants as c
    from .errors import FlextTargetLdifWriterError
    from .models import FlextTargetLdifModels, FlextTargetLdifModels as m
    from .protocols import FlextTargetLdifProtocols, FlextTargetLdifProtocols as p
    from .typings import FlextTargetLdifTypes, FlextTargetLdifTypes as t
    from .utilities import FlextTargetLdifUtilities, FlextTargetLdifUtilities as u
    from .writer import FlextTargetLdifWriter
__all__: tuple[str, ...] = (
    "TYPE_CHECKING",
    "Final",
    "FlextLdifConstants",
    "FlextTargetLdifCli",
    "FlextTargetLdifConfig",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifService",
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

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextTargetLdifConfig", "config"),
            "._settings": ("FlextTargetLdifSettings", "settings"),
            ".api": ("FlextTargetLdifService", "target_ldif"),
            ".cli": ("FlextTargetLdifCli", "main"),
            ".constants": ("FlextTargetLdifConstants", "c"),
            ".errors": ("FlextTargetLdifWriterError",),
            ".models": ("FlextTargetLdifModels", "m"),
            ".protocols": ("FlextTargetLdifProtocols", "p"),
            ".typings": ("FlextTargetLdifTypes", "t"),
            ".utilities": ("FlextTargetLdifUtilities", "u"),
            ".writer": ("FlextTargetLdifWriter",),
            "flext_ldif": ("FlextLdifConstants", "d", "e", "h", "r", "s", "x"),
            "typing": ("Final", "TYPE_CHECKING"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
