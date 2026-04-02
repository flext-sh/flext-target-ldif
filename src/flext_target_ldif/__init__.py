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
    from flext_ldif import d, e, h, r, s, x
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
    from flext_target_ldif.writer import FlextTargetLdifWriter, logger

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
        "d": "flext_ldif",
        "e": "flext_ldif",
        "errors": "flext_target_ldif.errors",
        "exceptions": "flext_target_ldif.exceptions",
        "h": "flext_ldif",
        "logger": "flext_target_ldif.writer",
        "m": ("flext_target_ldif.models", "FlextTargetLdifModels"),
        "main": "flext_target_ldif.cli",
        "models": "flext_target_ldif.models",
        "p": ("flext_target_ldif.protocols", "FlextTargetLdifProtocols"),
        "protocols": "flext_target_ldif.protocols",
        "r": "flext_ldif",
        "s": "flext_ldif",
        "settings": "flext_target_ldif.settings",
        "sinks": "flext_target_ldif.sinks",
        "t": ("flext_target_ldif.typings", "FlextTargetLdifTypes"),
        "target": "flext_target_ldif.target",
        "typings": "flext_target_ldif.typings",
        "u": ("flext_target_ldif.utilities", "FlextTargetLdifUtilities"),
        "utilities": "flext_target_ldif.utilities",
        "writer": "flext_target_ldif.writer",
        "x": "flext_ldif",
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
