# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

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
    MappingProxyType(
        build_lazy_import_map(
            MappingProxyType({
                "._config": ("FlextTargetLdifConfig", "config"),
                "._settings": ("FlextTargetLdifSettings", "settings"),
                ".api": ("FlextTargetLdifService", "target_ldif"),
                ".cli": ("FlextTargetLdifCli", "main"),
                ".constants": ("FlextTargetLdifConstants", "c"),
                ".models": ("FlextTargetLdifModels", "m"),
                ".protocols": ("FlextTargetLdifProtocols", "p"),
                ".typings": ("FlextTargetLdifTypes", "t"),
                ".utilities": ("FlextTargetLdifUtilities", "u"),
                "flext_ldif": ("d", "e", "h", "r", "s", "x"),
            }),
            alias_groups=MappingProxyType({}),
            sort_keys=False,
        )
    ),
    public_exports=__all__,
)
