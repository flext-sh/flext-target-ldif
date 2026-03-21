# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Module docstring."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import d, e, h, r, s, x
    from flext_core.typings import FlextTypes

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
    from flext_target_ldif.sinks import LDIFSink
    from flext_target_ldif.target import TargetLDIF
    from flext_target_ldif.transformers import (
        RecordTransformer,
        normalize_attribute_value,
        transform_boolean,
        transform_email,
        transform_name,
        transform_phone,
        transform_timestamp,
    )
    from flext_target_ldif.typings import (
        FlextTargetLdifTypes,
        FlextTargetLdifTypes as t,
    )
    from flext_target_ldif.utilities import (
        FlextTargetLdifUtilities,
        FlextTargetLdifUtilities as u,
    )
    from flext_target_ldif.writer import LdifWriter, logger

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextTargetLdifConstants": (
        "flext_target_ldif.constants",
        "FlextTargetLdifConstants",
    ),
    "FlextTargetLdifModels": ("flext_target_ldif.models", "FlextTargetLdifModels"),
    "FlextTargetLdifProtocols": (
        "flext_target_ldif.protocols",
        "FlextTargetLdifProtocols",
    ),
    "FlextTargetLdifSettings": (
        "flext_target_ldif.settings",
        "FlextTargetLdifSettings",
    ),
    "FlextTargetLdifTypes": ("flext_target_ldif.typings", "FlextTargetLdifTypes"),
    "FlextTargetLdifUtilities": (
        "flext_target_ldif.utilities",
        "FlextTargetLdifUtilities",
    ),
    "FlextTargetLdifWriterError": (
        "flext_target_ldif.exceptions",
        "FlextTargetLdifWriterError",
    ),
    "LDIFSink": ("flext_target_ldif.sinks", "LDIFSink"),
    "LdifWriter": ("flext_target_ldif.writer", "LdifWriter"),
    "RecordTransformer": ("flext_target_ldif.transformers", "RecordTransformer"),
    "TargetLDIF": ("flext_target_ldif.target", "TargetLDIF"),
    "__all__": ("flext_target_ldif.__version__", "__all__"),
    "__author__": ("flext_target_ldif.__version__", "__author__"),
    "__author_email__": ("flext_target_ldif.__version__", "__author_email__"),
    "__description__": ("flext_target_ldif.__version__", "__description__"),
    "__license__": ("flext_target_ldif.__version__", "__license__"),
    "__title__": ("flext_target_ldif.__version__", "__title__"),
    "__url__": ("flext_target_ldif.__version__", "__url__"),
    "__version__": ("flext_target_ldif.__version__", "__version__"),
    "__version_info__": ("flext_target_ldif.__version__", "__version_info__"),
    "c": ("flext_target_ldif.constants", "FlextTargetLdifConstants"),
    "d": ("flext_core", "d"),
    "e": ("flext_core", "e"),
    "h": ("flext_core", "h"),
    "logger": ("flext_target_ldif.writer", "logger"),
    "m": ("flext_target_ldif.models", "FlextTargetLdifModels"),
    "main": ("flext_target_ldif.cli", "main"),
    "normalize_attribute_value": (
        "flext_target_ldif.transformers",
        "normalize_attribute_value",
    ),
    "p": ("flext_target_ldif.protocols", "FlextTargetLdifProtocols"),
    "r": ("flext_core", "r"),
    "s": ("flext_core", "s"),
    "t": ("flext_target_ldif.typings", "FlextTargetLdifTypes"),
    "transform_boolean": ("flext_target_ldif.transformers", "transform_boolean"),
    "transform_email": ("flext_target_ldif.transformers", "transform_email"),
    "transform_name": ("flext_target_ldif.transformers", "transform_name"),
    "transform_phone": ("flext_target_ldif.transformers", "transform_phone"),
    "transform_timestamp": ("flext_target_ldif.transformers", "transform_timestamp"),
    "u": ("flext_target_ldif.utilities", "FlextTargetLdifUtilities"),
    "x": ("flext_core", "x"),
}

__all__ = [
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifSettings",
    "FlextTargetLdifTypes",
    "FlextTargetLdifUtilities",
    "FlextTargetLdifWriterError",
    "LDIFSink",
    "LdifWriter",
    "RecordTransformer",
    "TargetLDIF",
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
    "normalize_attribute_value",
    "p",
    "r",
    "s",
    "t",
    "transform_boolean",
    "transform_email",
    "transform_name",
    "transform_phone",
    "transform_timestamp",
    "u",
    "x",
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
