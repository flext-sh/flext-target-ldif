# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Module docstring."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
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

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_target_ldif import (
        _utilities,
        api,
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
    from flext_target_ldif._utilities import (
        FlextTargetLdifServiceRuntime,
        service_runtime,
    )
    from flext_target_ldif.api import FlextTargetLdifService
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
    from flext_target_ldif.writer import FlextTargetLdifWriter

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_target_ldif._utilities",),
    {
        "FlextTargetLdif": "flext_target_ldif.target",
        "FlextTargetLdifConstants": "flext_target_ldif.constants",
        "FlextTargetLdifModels": "flext_target_ldif.models",
        "FlextTargetLdifProtocols": "flext_target_ldif.protocols",
        "FlextTargetLdifService": "flext_target_ldif.api",
        "FlextTargetLdifSettings": "flext_target_ldif.settings",
        "FlextTargetLdifSink": "flext_target_ldif.sinks",
        "FlextTargetLdifTypes": "flext_target_ldif.typings",
        "FlextTargetLdifUtilities": "flext_target_ldif.utilities",
        "FlextTargetLdifWriter": "flext_target_ldif.writer",
        "FlextTargetLdifWriterError": "flext_target_ldif.errors",
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
        "main": "flext_target_ldif.cli",
        "models": "flext_target_ldif.models",
        "p": ("flext_target_ldif.protocols", "FlextTargetLdifProtocols"),
        "protocols": "flext_target_ldif.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "settings": "flext_target_ldif.settings",
        "sinks": "flext_target_ldif.sinks",
        "t": ("flext_target_ldif.typings", "FlextTargetLdifTypes"),
        "target": "flext_target_ldif.target",
        "typings": "flext_target_ldif.typings",
        "u": ("flext_target_ldif.utilities", "FlextTargetLdifUtilities"),
        "utilities": "flext_target_ldif.utilities",
        "writer": "flext_target_ldif.writer",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "FlextTargetLdifVersion",
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
