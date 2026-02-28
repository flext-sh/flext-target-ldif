"""Module docstring."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_target_ldif.__version__ import __version__, __version_info__
    from flext_target_ldif.cli import main as cli_main
    from flext_target_ldif.constants import (
        FlextTargetLdifConstants,
        FlextTargetLdifConstants as c,
    )
    from flext_target_ldif.exceptions import FlextTargetLdifWriterError
    from flext_target_ldif.models import (
        FlextTargetLdifModels,
        FlextTargetLdifModels as m,
    )
    from flext_target_ldif.protocols import FlextTargetLdifProtocols
    from flext_target_ldif.settings import FlextTargetLdifSettings
    from flext_target_ldif.sinks import LDIFSink, LDIFSink as _LDIFSink
    from flext_target_ldif.target import (
        TargetLDIF,
        TargetLDIF as FlextLdifTarget,
        TargetLDIF as FlextTargetLDIF,
        TargetLDIF as LDIFTarget,
    )
    from flext_target_ldif.transformers import (
        RecordTransformer,
        normalize_attribute_value,
        transform_boolean,
        transform_email,
        transform_name,
        transform_phone,
        transform_timestamp,
    )
    from flext_target_ldif.typings import t
    from flext_target_ldif.utilities import u
    from flext_target_ldif.writer import LdifWriter, LdifWriter as _LdifWriter

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextLdifTarget": ("flext_target_ldif.target", "TargetLDIF"),
    "FlextTargetLDIF": ("flext_target_ldif.target", "TargetLDIF"),
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
    "FlextTargetLdifWriterError": (
        "flext_target_ldif.exceptions",
        "FlextTargetLdifWriterError",
    ),
    "LDIFSink": ("flext_target_ldif.sinks", "LDIFSink"),
    "LDIFTarget": ("flext_target_ldif.target", "TargetLDIF"),
    "LdifWriter": ("flext_target_ldif.writer", "LdifWriter"),
    "RecordTransformer": ("flext_target_ldif.transformers", "RecordTransformer"),
    "TargetLDIF": ("flext_target_ldif.target", "TargetLDIF"),
    "_LDIFSink": ("flext_target_ldif.sinks", "LDIFSink"),
    "_LdifWriter": ("flext_target_ldif.writer", "LdifWriter"),
    "__version__": ("flext_target_ldif.__version__", "__version__"),
    "__version_info__": ("flext_target_ldif.__version__", "__version_info__"),
    "c": ("flext_target_ldif.constants", "FlextTargetLdifConstants"),
    "cli_main": ("flext_target_ldif.cli", "main"),
    "m": ("flext_target_ldif.models", "FlextTargetLdifModels"),
    "normalize_attribute_value": (
        "flext_target_ldif.transformers",
        "normalize_attribute_value",
    ),
    "t": ("flext_target_ldif.typings", "t"),
    "transform_boolean": ("flext_target_ldif.transformers", "transform_boolean"),
    "transform_email": ("flext_target_ldif.transformers", "transform_email"),
    "transform_name": ("flext_target_ldif.transformers", "transform_name"),
    "transform_phone": ("flext_target_ldif.transformers", "transform_phone"),
    "transform_timestamp": ("flext_target_ldif.transformers", "transform_timestamp"),
    "u": ("flext_target_ldif.utilities", "u"),
}

__all__ = [
    "FlextLdifTarget",
    "FlextTargetLDIF",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifSettings",
    "FlextTargetLdifWriterError",
    "LDIFSink",
    "LDIFTarget",
    "LdifWriter",
    "RecordTransformer",
    "TargetLDIF",
    "_LDIFSink",
    "_LdifWriter",
    "__version__",
    "__version_info__",
    "c",
    "cli_main",
    "m",
    "normalize_attribute_value",
    "t",
    "transform_boolean",
    "transform_email",
    "transform_name",
    "transform_phone",
    "transform_timestamp",
    "u",
]


def __getattr__(name: str) -> t.GeneralValueType:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
