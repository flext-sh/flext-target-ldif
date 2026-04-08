# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests import (
        conftest,
        constants,
        models,
        protocols,
        test_target,
        test_writer,
        typings,
        utilities,
    )
    from tests.constants import (
        TestsFlextTargetLdifConstants,
        TestsFlextTargetLdifConstants as c,
    )
    from tests.models import TestsFlextTargetLdifModels, TestsFlextTargetLdifModels as m
    from tests.protocols import (
        TestsFlextTargetLdifProtocols,
        TestsFlextTargetLdifProtocols as p,
    )
    from tests.typings import TestsFlextTargetLdifTypes, TestsFlextTargetLdifTypes as t
    from tests.utilities import (
        TestsFlextTargetLdifUtilities,
        TestsFlextTargetLdifUtilities as u,
    )
_LAZY_IMPORTS = {
    "TestsFlextTargetLdifConstants": (
        "tests.constants",
        "TestsFlextTargetLdifConstants",
    ),
    "TestsFlextTargetLdifModels": ("tests.models", "TestsFlextTargetLdifModels"),
    "TestsFlextTargetLdifProtocols": (
        "tests.protocols",
        "TestsFlextTargetLdifProtocols",
    ),
    "TestsFlextTargetLdifTypes": ("tests.typings", "TestsFlextTargetLdifTypes"),
    "TestsFlextTargetLdifUtilities": (
        "tests.utilities",
        "TestsFlextTargetLdifUtilities",
    ),
    "c": ("tests.constants", "TestsFlextTargetLdifConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "TestsFlextTargetLdifModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "TestsFlextTargetLdifProtocols"),
    "protocols": "tests.protocols",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("tests.typings", "TestsFlextTargetLdifTypes"),
    "test_target": "tests.test_target",
    "test_writer": "tests.test_writer",
    "typings": "tests.typings",
    "u": ("tests.utilities", "TestsFlextTargetLdifUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
    "TestsFlextTargetLdifTypes",
    "TestsFlextTargetLdifUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "test_target",
    "test_writer",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
