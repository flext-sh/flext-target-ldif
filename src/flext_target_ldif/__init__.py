# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Module docstring."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_target_ldif.__version__ import (
    FlextTargetLdifVersion as FlextTargetLdifVersion,
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
    from flext_ldif import d, e, h, r, s, x

    from flext_target_ldif import (
        cli as cli,
        constants as constants,
        errors as errors,
        exceptions as exceptions,
        models as models,
        protocols as protocols,
        settings as settings,
        sinks as sinks,
        target as target,
        typings as typings,
        utilities as utilities,
        writer as writer,
    )
    from flext_target_ldif.cli import main as main
    from flext_target_ldif.constants import (
        FlextTargetLdifConstants as FlextTargetLdifConstants,
        FlextTargetLdifConstants as c,
    )
    from flext_target_ldif.errors import (
        FlextTargetLdifWriterError as FlextTargetLdifWriterError,
    )
    from flext_target_ldif.models import (
        FlextTargetLdifModels as FlextTargetLdifModels,
        FlextTargetLdifModels as m,
    )
    from flext_target_ldif.protocols import (
        FlextTargetLdifProtocols as FlextTargetLdifProtocols,
        FlextTargetLdifProtocols as p,
    )
    from flext_target_ldif.settings import (
        FlextTargetLdifSettings as FlextTargetLdifSettings,
    )
    from flext_target_ldif.sinks import FlextTargetLdifSink as FlextTargetLdifSink
    from flext_target_ldif.target import FlextTargetLdif as FlextTargetLdif
    from flext_target_ldif.typings import (
        FlextTargetLdifTypes as FlextTargetLdifTypes,
        FlextTargetLdifTypes as t,
    )
    from flext_target_ldif.utilities import (
        FlextTargetLdifUtilities as FlextTargetLdifUtilities,
        FlextTargetLdifUtilities as u,
    )
    from flext_target_ldif.writer import (
        FlextTargetLdifWriter as FlextTargetLdifWriter,
        logger as logger,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetLdif": ["flext_target_ldif.target", "FlextTargetLdif"],
    "FlextTargetLdifConstants": ["flext_target_ldif.constants", "FlextTargetLdifConstants"],
    "FlextTargetLdifModels": ["flext_target_ldif.models", "FlextTargetLdifModels"],
    "FlextTargetLdifProtocols": ["flext_target_ldif.protocols", "FlextTargetLdifProtocols"],
    "FlextTargetLdifSettings": ["flext_target_ldif.settings", "FlextTargetLdifSettings"],
    "FlextTargetLdifSink": ["flext_target_ldif.sinks", "FlextTargetLdifSink"],
    "FlextTargetLdifTypes": ["flext_target_ldif.typings", "FlextTargetLdifTypes"],
    "FlextTargetLdifUtilities": ["flext_target_ldif.utilities", "FlextTargetLdifUtilities"],
    "FlextTargetLdifWriter": ["flext_target_ldif.writer", "FlextTargetLdifWriter"],
    "FlextTargetLdifWriterError": ["flext_target_ldif.errors", "FlextTargetLdifWriterError"],
    "c": ["flext_target_ldif.constants", "FlextTargetLdifConstants"],
    "cli": ["flext_target_ldif.cli", ""],
    "constants": ["flext_target_ldif.constants", ""],
    "d": ["flext_ldif", "d"],
    "e": ["flext_ldif", "e"],
    "errors": ["flext_target_ldif.errors", ""],
    "exceptions": ["flext_target_ldif.exceptions", ""],
    "h": ["flext_ldif", "h"],
    "logger": ["flext_target_ldif.writer", "logger"],
    "m": ["flext_target_ldif.models", "FlextTargetLdifModels"],
    "main": ["flext_target_ldif.cli", "main"],
    "models": ["flext_target_ldif.models", ""],
    "p": ["flext_target_ldif.protocols", "FlextTargetLdifProtocols"],
    "protocols": ["flext_target_ldif.protocols", ""],
    "r": ["flext_ldif", "r"],
    "s": ["flext_ldif", "s"],
    "settings": ["flext_target_ldif.settings", ""],
    "sinks": ["flext_target_ldif.sinks", ""],
    "t": ["flext_target_ldif.typings", "FlextTargetLdifTypes"],
    "target": ["flext_target_ldif.target", ""],
    "typings": ["flext_target_ldif.typings", ""],
    "u": ["flext_target_ldif.utilities", "FlextTargetLdifUtilities"],
    "utilities": ["flext_target_ldif.utilities", ""],
    "writer": ["flext_target_ldif.writer", ""],
    "x": ["flext_ldif", "x"],
}

_EXPORTS: Sequence[str] = [
    "FlextTargetLdif",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifSettings",
    "FlextTargetLdifSink",
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
    "c",
    "cli",
    "constants",
    "d",
    "e",
    "errors",
    "exceptions",
    "h",
    "logger",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "sinks",
    "t",
    "target",
    "typings",
    "u",
    "utilities",
    "writer",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
