# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_target_ldif import (
        conftest,
        constants,
        models,
        protocols,
        test_target,
        test_writer,
        tp,
        tt,
        tu,
        typings,
        utilities,
    )
    from flext_target_ldif.conftest import (
        attribute_mapping,
        ldif_options,
        multiple_records,
        sample_config,
        sample_record,
        sample_schema,
        temp_dir,
        temp_file,
    )
    from flext_target_ldif.constants import (
        FlextTargetLdifTestConstants,
        FlextTargetLdifTestConstants as c,
    )
    from flext_target_ldif.models import (
        FlextTargetLdifTestModels,
        FlextTargetLdifTestModels as m,
        tm,
    )
    from flext_target_ldif.protocols import (
        FlextTargetLdifTestProtocols,
        FlextTargetLdifTestProtocols as p,
    )
    from flext_target_ldif.test_target import (
        FlextTargetLdifSink,
        TestFlextTargetLdifSettings,
    )
    from flext_target_ldif.test_writer import (
        EXPECTED_BULK_SIZE,
        EXPECTED_DATA_COUNT,
        TestFlextTargetLdifWriterInitialization,
    )
    from flext_target_ldif.typings import (
        FlextTargetLdifTestTypes,
        FlextTargetLdifTestTypes as t,
    )
    from flext_target_ldif.utilities import (
        FlextTargetLdifTestUtilities,
        FlextTargetLdifTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "EXPECTED_BULK_SIZE": "flext_target_ldif.test_writer",
    "EXPECTED_DATA_COUNT": "flext_target_ldif.test_writer",
    "FlextTargetLdifSink": "flext_target_ldif.test_target",
    "FlextTargetLdifTestConstants": "flext_target_ldif.constants",
    "FlextTargetLdifTestModels": "flext_target_ldif.models",
    "FlextTargetLdifTestProtocols": "flext_target_ldif.protocols",
    "FlextTargetLdifTestTypes": "flext_target_ldif.typings",
    "FlextTargetLdifTestUtilities": "flext_target_ldif.utilities",
    "TestFlextTargetLdifSettings": "flext_target_ldif.test_target",
    "TestFlextTargetLdifWriterInitialization": "flext_target_ldif.test_writer",
    "attribute_mapping": "flext_target_ldif.conftest",
    "c": ("flext_target_ldif.constants", "FlextTargetLdifTestConstants"),
    "conftest": "flext_target_ldif.conftest",
    "constants": "flext_target_ldif.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "ldif_options": "flext_target_ldif.conftest",
    "m": ("flext_target_ldif.models", "FlextTargetLdifTestModels"),
    "models": "flext_target_ldif.models",
    "multiple_records": "flext_target_ldif.conftest",
    "p": ("flext_target_ldif.protocols", "FlextTargetLdifTestProtocols"),
    "protocols": "flext_target_ldif.protocols",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "sample_config": "flext_target_ldif.conftest",
    "sample_record": "flext_target_ldif.conftest",
    "sample_schema": "flext_target_ldif.conftest",
    "t": ("flext_target_ldif.typings", "FlextTargetLdifTestTypes"),
    "temp_dir": "flext_target_ldif.conftest",
    "temp_file": "flext_target_ldif.conftest",
    "test_target": "flext_target_ldif.test_target",
    "test_writer": "flext_target_ldif.test_writer",
    "tm": "flext_target_ldif.models",
    "tp": "flext_target_ldif.tp",
    "tt": "flext_target_ldif.tt",
    "tu": "flext_target_ldif.tu",
    "typings": "flext_target_ldif.typings",
    "u": ("flext_target_ldif.utilities", "FlextTargetLdifTestUtilities"),
    "utilities": "flext_target_ldif.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
