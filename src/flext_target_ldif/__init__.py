# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext target ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_target_ldif.__version__ import *

if _t.TYPE_CHECKING:
    import flext_target_ldif._utilities as _flext_target_ldif__utilities

    _utilities = _flext_target_ldif__utilities
    import flext_target_ldif.api as _flext_target_ldif_api
    from flext_target_ldif._utilities import (
        FlextTargetLdifServiceRuntime,
        service_runtime,
    )

    api = _flext_target_ldif_api
    import flext_target_ldif.cli as _flext_target_ldif_cli
    from flext_target_ldif.api import (
        FlextTargetLdifService,
        FlextTargetLdifService as s,
    )

    cli = _flext_target_ldif_cli
    import flext_target_ldif.constants as _flext_target_ldif_constants
    from flext_target_ldif.cli import main

    constants = _flext_target_ldif_constants
    import flext_target_ldif.errors as _flext_target_ldif_errors
    from flext_target_ldif.constants import (
        FlextTargetLdifConstants,
        FlextTargetLdifConstants as c,
    )

    errors = _flext_target_ldif_errors
    import flext_target_ldif.exceptions as _flext_target_ldif_exceptions
    from flext_target_ldif.errors import FlextTargetLdifWriterError

    exceptions = _flext_target_ldif_exceptions
    import flext_target_ldif.models as _flext_target_ldif_models

    models = _flext_target_ldif_models
    import flext_target_ldif.protocols as _flext_target_ldif_protocols
    from flext_target_ldif.models import (
        FlextTargetLdifModels,
        FlextTargetLdifModels as m,
    )

    protocols = _flext_target_ldif_protocols
    import flext_target_ldif.settings as _flext_target_ldif_settings
    from flext_target_ldif.protocols import (
        FlextTargetLdifProtocols,
        FlextTargetLdifProtocols as p,
    )

    settings = _flext_target_ldif_settings
    import flext_target_ldif.target as _flext_target_ldif_target
    from flext_target_ldif.settings import FlextTargetLdifSettings

    target = _flext_target_ldif_target
    import flext_target_ldif.typings as _flext_target_ldif_typings
    from flext_target_ldif.target import FlextTargetLdif

    typings = _flext_target_ldif_typings
    import flext_target_ldif.utilities as _flext_target_ldif_utilities
    from flext_target_ldif.typings import (
        FlextTargetLdifTypes,
        FlextTargetLdifTypes as t,
    )

    utilities = _flext_target_ldif_utilities
    import flext_target_ldif.writer as _flext_target_ldif_writer
    from flext_target_ldif.utilities import (
        FlextTargetLdifUtilities,
        FlextTargetLdifUtilities as u,
    )

    writer = _flext_target_ldif_writer
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_target_ldif.writer import FlextTargetLdifWriter
_LAZY_IMPORTS = merge_lazy_imports(
    ("flext_target_ldif._utilities",),
    {
        "FlextTargetLdif": ("flext_target_ldif.target", "FlextTargetLdif"),
        "FlextTargetLdifConstants": (
            "flext_target_ldif.constants",
            "FlextTargetLdifConstants",
        ),
        "FlextTargetLdifModels": ("flext_target_ldif.models", "FlextTargetLdifModels"),
        "FlextTargetLdifProtocols": (
            "flext_target_ldif.protocols",
            "FlextTargetLdifProtocols",
        ),
        "FlextTargetLdifService": ("flext_target_ldif.api", "FlextTargetLdifService"),
        "FlextTargetLdifSettings": (
            "flext_target_ldif.settings",
            "FlextTargetLdifSettings",
        ),
        "FlextTargetLdifTypes": ("flext_target_ldif.typings", "FlextTargetLdifTypes"),
        "FlextTargetLdifUtilities": (
            "flext_target_ldif.utilities",
            "FlextTargetLdifUtilities",
        ),
        "FlextTargetLdifVersion": (
            "flext_target_ldif.__version__",
            "FlextTargetLdifVersion",
        ),
        "FlextTargetLdifWriter": ("flext_target_ldif.writer", "FlextTargetLdifWriter"),
        "FlextTargetLdifWriterError": (
            "flext_target_ldif.errors",
            "FlextTargetLdifWriterError",
        ),
        "__author__": ("flext_target_ldif.__version__", "__author__"),
        "__author_email__": ("flext_target_ldif.__version__", "__author_email__"),
        "__description__": ("flext_target_ldif.__version__", "__description__"),
        "__license__": ("flext_target_ldif.__version__", "__license__"),
        "__title__": ("flext_target_ldif.__version__", "__title__"),
        "__url__": ("flext_target_ldif.__version__", "__url__"),
        "__version__": ("flext_target_ldif.__version__", "__version__"),
        "__version_info__": ("flext_target_ldif.__version__", "__version_info__"),
        "_utilities": "flext_target_ldif._utilities",
        "api": "flext_target_ldif.api",
        "c": ("flext_target_ldif.constants", "FlextTargetLdifConstants"),
        "cli": "flext_target_ldif.cli",
        "constants": "flext_target_ldif.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "errors": "flext_target_ldif.errors",
        "exceptions": "flext_target_ldif.exceptions",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_target_ldif.models", "FlextTargetLdifModels"),
        "main": ("flext_target_ldif.cli", "main"),
        "models": "flext_target_ldif.models",
        "p": ("flext_target_ldif.protocols", "FlextTargetLdifProtocols"),
        "protocols": "flext_target_ldif.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_target_ldif.api", "FlextTargetLdifService"),
        "settings": "flext_target_ldif.settings",
        "t": ("flext_target_ldif.typings", "FlextTargetLdifTypes"),
        "target": "flext_target_ldif.target",
        "typings": "flext_target_ldif.typings",
        "u": ("flext_target_ldif.utilities", "FlextTargetLdifUtilities"),
        "utilities": "flext_target_ldif.utilities",
        "writer": "flext_target_ldif.writer",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "FlextTargetLdif",
    "FlextTargetLdifConstants",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifService",
    "FlextTargetLdifServiceRuntime",
    "FlextTargetLdifSettings",
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
    "_utilities",
    "api",
    "c",
    "cli",
    "constants",
    "d",
    "e",
    "errors",
    "exceptions",
    "h",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "service_runtime",
    "settings",
    "t",
    "target",
    "typings",
    "u",
    "utilities",
    "writer",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
