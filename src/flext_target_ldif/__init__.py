# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Module docstring."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
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
    from flext_target_ldif.constants import FlextTargetLdifConstants, c
    from flext_target_ldif.exceptions import FlextTargetLdifWriterError
    from flext_target_ldif.models import FlextTargetLdifModels, m
    from flext_target_ldif.protocols import FlextTargetLdifProtocols, p
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
    from flext_target_ldif.typings import FlextTargetLdifTypes, t
    from flext_target_ldif.utilities import FlextTargetLdifUtilities, u
    from flext_target_ldif.writer import LdifWriter, logger

# Lazy import mapping: export_name -> (module_path, attr_name)
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
    "c": ("flext_target_ldif.constants", "c"),
    "logger": ("flext_target_ldif.writer", "logger"),
    "m": ("flext_target_ldif.models", "m"),
    "main": ("flext_target_ldif.cli", "main"),
    "normalize_attribute_value": (
        "flext_target_ldif.transformers",
        "normalize_attribute_value",
    ),
    "p": ("flext_target_ldif.protocols", "p"),
    "t": ("flext_target_ldif.typings", "t"),
    "transform_boolean": ("flext_target_ldif.transformers", "transform_boolean"),
    "transform_email": ("flext_target_ldif.transformers", "transform_email"),
    "transform_name": ("flext_target_ldif.transformers", "transform_name"),
    "transform_phone": ("flext_target_ldif.transformers", "transform_phone"),
    "transform_timestamp": ("flext_target_ldif.transformers", "transform_timestamp"),
    "u": ("flext_target_ldif.utilities", "u"),
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
    "logger",
    "m",
    "main",
    "normalize_attribute_value",
    "p",
    "t",
    "transform_boolean",
    "transform_email",
    "transform_name",
    "transform_phone",
    "transform_timestamp",
    "u",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
