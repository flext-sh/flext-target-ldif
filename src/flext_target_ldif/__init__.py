# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Module docstring."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

from flext_target_ldif.__version__ import (
    FlextTargetLdifVersion,
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
    from flext_core import FlextTypes
    from flext_ldif import d, e, h, r, s, x

    from flext_target_ldif import (
        cli,
        constants,
        errors,
        exceptions,
        models,
        protocols,
        settings,
        sinks,
        target,
        typings,
        utilities,
        writer,
    )
    from flext_target_ldif.cli import main
    from flext_target_ldif.constants import (
        FlextTargetLdifConstants,
        FlextTargetLdifConstants as c,
    )
    from flext_target_ldif.errors import FlextTargetLdifWriterError
    from flext_target_ldif.models import (
        FlextTargetLdifModels,
        FlextTargetLdifModels as m,
    )
    from flext_target_ldif.protocols import (
        FlextTargetLdifProtocols,
        FlextTargetLdifProtocols as p,
    )
    from flext_target_ldif.settings import FlextTargetLdifSettings
    from flext_target_ldif.sinks import FlextTargetLdifSink
    from flext_target_ldif.target import FlextTargetLdif
    from flext_target_ldif.typings import (
        FlextTargetLdifTypes,
        FlextTargetLdifTypes as t,
    )
    from flext_target_ldif.utilities import (
        FlextTargetLdifUtilities,
        FlextTargetLdifUtilities as u,
    )
    from flext_target_ldif.writer import FlextTargetLdifWriter, logger

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTargetLdif": ["flext_target_ldif.target", "FlextTargetLdif"],
    "FlextTargetLdifConstants": [
        "flext_target_ldif.constants",
        "FlextTargetLdifConstants",
    ],
    "FlextTargetLdifModels": ["flext_target_ldif.models", "FlextTargetLdifModels"],
    "FlextTargetLdifProtocols": [
        "flext_target_ldif.protocols",
        "FlextTargetLdifProtocols",
    ],
    "FlextTargetLdifSettings": [
        "flext_target_ldif.settings",
        "FlextTargetLdifSettings",
    ],
    "FlextTargetLdifSink": ["flext_target_ldif.sinks", "FlextTargetLdifSink"],
    "FlextTargetLdifTypes": ["flext_target_ldif.typings", "FlextTargetLdifTypes"],
    "FlextTargetLdifUtilities": [
        "flext_target_ldif.utilities",
        "FlextTargetLdifUtilities",
    ],
    "FlextTargetLdifWriter": ["flext_target_ldif.writer", "FlextTargetLdifWriter"],
    "FlextTargetLdifWriterError": [
        "flext_target_ldif.errors",
        "FlextTargetLdifWriterError",
    ],
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

__all__ = [
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


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
