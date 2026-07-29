# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

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
    from flext_ldif import d as d
    from flext_ldif import e as e
    from flext_ldif import h as h
    from flext_ldif import r as r
    from flext_ldif import s as s
    from flext_ldif import x as x

    from ._config import FlextTargetLdifConfig as FlextTargetLdifConfig
    from ._config import config as config
    from ._settings import FlextTargetLdifSettings as FlextTargetLdifSettings
    from ._settings import settings as settings
    from .api import FlextTargetLdifService as FlextTargetLdifService
    from .api import target_ldif as target_ldif
    from .cli import FlextTargetLdifCli as FlextTargetLdifCli
    from .cli import main as main
    from .constants import FlextTargetLdifConstants as FlextTargetLdifConstants

    c: type[FlextTargetLdifConstants]
    from .models import FlextTargetLdifModels as FlextTargetLdifModels

    m: type[FlextTargetLdifModels]
    from .protocols import FlextTargetLdifProtocols as FlextTargetLdifProtocols

    p: type[FlextTargetLdifProtocols]
    from .typings import FlextTargetLdifTypes as FlextTargetLdifTypes

    t: type[FlextTargetLdifTypes]
    from .utilities import FlextTargetLdifUtilities as FlextTargetLdifUtilities

    u: type[FlextTargetLdifUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
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
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
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

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
