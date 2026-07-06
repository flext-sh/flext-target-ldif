# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports
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
from flext_target_ldif._exports import FLEXT_TARGET_LDIF_LAZY_IMPORTS

if TYPE_CHECKING:
    from flext_ldif import d as d, e as e, h as h, r as r, s as s, x as x
    from flext_target_ldif.api import (
        FlextTargetLdifService as FlextTargetLdifService,
        target_ldif as target_ldif,
    )
    from flext_target_ldif.cli import (
        FlextTargetLdifCli as FlextTargetLdifCli,
        main as main,
    )
    from flext_target_ldif.constants import (
        FlextTargetLdifConstants as FlextTargetLdifConstants,
        c as c,
    )
    from flext_target_ldif.models import (
        FlextTargetLdifModels as FlextTargetLdifModels,
        m as m,
    )
    from flext_target_ldif.protocols import (
        FlextTargetLdifProtocols as FlextTargetLdifProtocols,
        p as p,
    )
    from flext_target_ldif.settings import (
        FlextTargetLdifSettings as FlextTargetLdifSettings,
    )
    from flext_target_ldif.typings import (
        FlextTargetLdifTypes as FlextTargetLdifTypes,
        t as t,
    )
    from flext_target_ldif.utilities import (
        FlextTargetLdifUtilities as FlextTargetLdifUtilities,
        u as u,
    )


_LAZY_IMPORTS = FLEXT_TARGET_LDIF_LAZY_IMPORTS


_EAGER_EXPORTS = (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)


_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTargetLdifCli",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifService",
    "FlextTargetLdifSettings",
    "FlextTargetLdifTypes",
    "FlextTargetLdifUtilities",
    "target_ldif",
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
    "u",
    "x",
)

__all__: tuple[str, ...] = (
    "FlextTargetLdifCli",
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
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=_PUBLIC_EXPORTS,
)
