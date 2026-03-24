# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Module docstring."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_ldif import d, e, h, r, s, x

    from flext_target_ldif.__version__ import (
        __all__,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_target_ldif.cli import main
    from flext_target_ldif.constants import (
        FlextTargetLdifConstants,
        FlextTargetLdifConstants as c,
    )
    from flext_target_ldif.exceptions import FlextTargetLdifWriterError
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
    from flext_target_ldif.transformers import FlextTargetLdifRecordTransformer
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
    "FlextTargetLdifConstants": ["flext_target_ldif.constants", "FlextTargetLdifConstants"],
    "FlextTargetLdifModels": ["flext_target_ldif.models", "FlextTargetLdifModels"],
    "FlextTargetLdifProtocols": ["flext_target_ldif.protocols", "FlextTargetLdifProtocols"],
    "FlextTargetLdifRecordTransformer": ["flext_target_ldif.transformers", "FlextTargetLdifRecordTransformer"],
    "FlextTargetLdifSettings": ["flext_target_ldif.settings", "FlextTargetLdifSettings"],
    "FlextTargetLdifSink": ["flext_target_ldif.sinks", "FlextTargetLdifSink"],
    "FlextTargetLdifTypes": ["flext_target_ldif.typings", "FlextTargetLdifTypes"],
    "FlextTargetLdifUtilities": ["flext_target_ldif.utilities", "FlextTargetLdifUtilities"],
    "FlextTargetLdifWriter": ["flext_target_ldif.writer", "FlextTargetLdifWriter"],
    "FlextTargetLdifWriterError": ["flext_target_ldif.exceptions", "FlextTargetLdifWriterError"],
    "__all__": ["flext_target_ldif.__version__", "__all__"],
    "__author__": ["flext_target_ldif.__version__", "__author__"],
    "__author_email__": ["flext_target_ldif.__version__", "__author_email__"],
    "__description__": ["flext_target_ldif.__version__", "__description__"],
    "__license__": ["flext_target_ldif.__version__", "__license__"],
    "__title__": ["flext_target_ldif.__version__", "__title__"],
    "__url__": ["flext_target_ldif.__version__", "__url__"],
    "__version__": ["flext_target_ldif.__version__", "__version__"],
    "__version_info__": ["flext_target_ldif.__version__", "__version_info__"],
    "c": ["flext_target_ldif.constants", "FlextTargetLdifConstants"],
    "d": ["flext_ldif", "d"],
    "e": ["flext_ldif", "e"],
    "h": ["flext_ldif", "h"],
    "logger": ["flext_target_ldif.writer", "logger"],
    "m": ["flext_target_ldif.models", "FlextTargetLdifModels"],
    "main": ["flext_target_ldif.cli", "main"],
    "p": ["flext_target_ldif.protocols", "FlextTargetLdifProtocols"],
    "r": ["flext_ldif", "r"],
    "s": ["flext_ldif", "s"],
    "t": ["flext_target_ldif.typings", "FlextTargetLdifTypes"],
    "u": ["flext_target_ldif.utilities", "FlextTargetLdifUtilities"],
    "x": ["flext_ldif", "x"],
}

__all__ = [
    "FlextTargetLdif",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifRecordTransformer",
    "FlextTargetLdifSettings",
    "FlextTargetLdifSink",
    "FlextTargetLdifTypes",
    "FlextTargetLdifUtilities",
    "FlextTargetLdifWriter",
    "FlextTargetLdifWriterError",
    "__all__",
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
    "logger",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
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
