# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports
from flext_core.mixins import FlextMixins as x
from flext_core.result import FlextResult as r
from flext_core.service import FlextService as s
from tests.conftest import (
    attribute_mapping,
    ldif_options,
    multiple_records,
    pytest_configure,
    sample_config,
    sample_record,
    sample_schema,
    temp_dir,
    temp_file,
)
from tests.constants import (
    FlextTargetLdifTestConstants,
    FlextTargetLdifTestConstants as c,
)
from tests.models import (
    FlextTargetLdifTestModels,
    FlextTargetLdifTestModels as m,
    tm,
)
from tests.protocols import (
    FlextTargetLdifTestProtocols,
    FlextTargetLdifTestProtocols as p,
)
from tests.test_target import (
    FlextTargetLdifSink,
    TestFlextTargetLdif,
    TestFlextTargetLdifClass,
    TestFlextTargetLdifSettings,
    TestIntegration,
)
from tests.test_writer import (
    EXPECTED_BULK_SIZE,
    EXPECTED_DATA_COUNT,
    TestFlextTargetLdifWriterBase64Encoding,
    TestFlextTargetLdifWriterContextManager,
    TestFlextTargetLdifWriterDnGeneration,
    TestFlextTargetLdifWriterFileOperations,
    TestFlextTargetLdifWriterHeaderGeneration,
    TestFlextTargetLdifWriterInitialization,
    TestFlextTargetLdifWriterLineWrapping,
    TestFlextTargetLdifWriterProperties,
    TestFlextTargetLdifWriterRecordWriting,
)
from tests.typings import FlextTargetLdifTestTypes, FlextTargetLdifTestTypes as t
from tests.utilities import (
    FlextTargetLdifTestUtilities,
    FlextTargetLdifTestUtilities as u,
)

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.models as _tests_models

    models = _tests_models
    import tests.protocols as _tests_protocols

    protocols = _tests_protocols
    import tests.test_target as _tests_test_target

    test_target = _tests_test_target
    import tests.test_writer as _tests_test_writer

    test_writer = _tests_test_writer
    import tests.tp as _tests_tp

    tp = _tests_tp
    import tests.tt as _tests_tt

    tt = _tests_tt
    import tests.tu as _tests_tu

    tu = _tests_tu
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.utilities as _tests_utilities

    utilities = _tests_utilities

    _ = (
        EXPECTED_BULK_SIZE,
        EXPECTED_DATA_COUNT,
        FlextTargetLdifSink,
        FlextTargetLdifTestConstants,
        FlextTargetLdifTestModels,
        FlextTargetLdifTestProtocols,
        FlextTargetLdifTestTypes,
        FlextTargetLdifTestUtilities,
        TestFlextTargetLdif,
        TestFlextTargetLdifClass,
        TestFlextTargetLdifSettings,
        TestFlextTargetLdifWriterBase64Encoding,
        TestFlextTargetLdifWriterContextManager,
        TestFlextTargetLdifWriterDnGeneration,
        TestFlextTargetLdifWriterFileOperations,
        TestFlextTargetLdifWriterHeaderGeneration,
        TestFlextTargetLdifWriterInitialization,
        TestFlextTargetLdifWriterLineWrapping,
        TestFlextTargetLdifWriterProperties,
        TestFlextTargetLdifWriterRecordWriting,
        TestIntegration,
        attribute_mapping,
        c,
        conftest,
        constants,
        d,
        e,
        h,
        ldif_options,
        m,
        models,
        multiple_records,
        p,
        protocols,
        pytest_configure,
        r,
        s,
        sample_config,
        sample_record,
        sample_schema,
        t,
        temp_dir,
        temp_file,
        test_target,
        test_writer,
        tm,
        tp,
        tt,
        tu,
        typings,
        u,
        utilities,
        x,
    )
_LAZY_IMPORTS = {
    "EXPECTED_BULK_SIZE": "tests.test_writer",
    "EXPECTED_DATA_COUNT": "tests.test_writer",
    "FlextTargetLdifSink": "tests.test_target",
    "FlextTargetLdifTestConstants": "tests.constants",
    "FlextTargetLdifTestModels": "tests.models",
    "FlextTargetLdifTestProtocols": "tests.protocols",
    "FlextTargetLdifTestTypes": "tests.typings",
    "FlextTargetLdifTestUtilities": "tests.utilities",
    "TestFlextTargetLdif": "tests.test_target",
    "TestFlextTargetLdifClass": "tests.test_target",
    "TestFlextTargetLdifSettings": "tests.test_target",
    "TestFlextTargetLdifWriterBase64Encoding": "tests.test_writer",
    "TestFlextTargetLdifWriterContextManager": "tests.test_writer",
    "TestFlextTargetLdifWriterDnGeneration": "tests.test_writer",
    "TestFlextTargetLdifWriterFileOperations": "tests.test_writer",
    "TestFlextTargetLdifWriterHeaderGeneration": "tests.test_writer",
    "TestFlextTargetLdifWriterInitialization": "tests.test_writer",
    "TestFlextTargetLdifWriterLineWrapping": "tests.test_writer",
    "TestFlextTargetLdifWriterProperties": "tests.test_writer",
    "TestFlextTargetLdifWriterRecordWriting": "tests.test_writer",
    "TestIntegration": "tests.test_target",
    "attribute_mapping": "tests.conftest",
    "c": ("tests.constants", "FlextTargetLdifTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "ldif_options": "tests.conftest",
    "m": ("tests.models", "FlextTargetLdifTestModels"),
    "models": "tests.models",
    "multiple_records": "tests.conftest",
    "p": ("tests.protocols", "FlextTargetLdifTestProtocols"),
    "protocols": "tests.protocols",
    "pytest_configure": "tests.conftest",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "sample_config": "tests.conftest",
    "sample_record": "tests.conftest",
    "sample_schema": "tests.conftest",
    "t": ("tests.typings", "FlextTargetLdifTestTypes"),
    "temp_dir": "tests.conftest",
    "temp_file": "tests.conftest",
    "test_target": "tests.test_target",
    "test_writer": "tests.test_writer",
    "tm": "tests.models",
    "tp": "tests.tp",
    "tt": "tests.tt",
    "tu": "tests.tu",
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextTargetLdifTestUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "EXPECTED_BULK_SIZE",
    "EXPECTED_DATA_COUNT",
    "FlextTargetLdifSink",
    "FlextTargetLdifTestConstants",
    "FlextTargetLdifTestModels",
    "FlextTargetLdifTestProtocols",
    "FlextTargetLdifTestTypes",
    "FlextTargetLdifTestUtilities",
    "TestFlextTargetLdif",
    "TestFlextTargetLdifClass",
    "TestFlextTargetLdifSettings",
    "TestFlextTargetLdifWriterBase64Encoding",
    "TestFlextTargetLdifWriterContextManager",
    "TestFlextTargetLdifWriterDnGeneration",
    "TestFlextTargetLdifWriterFileOperations",
    "TestFlextTargetLdifWriterHeaderGeneration",
    "TestFlextTargetLdifWriterInitialization",
    "TestFlextTargetLdifWriterLineWrapping",
    "TestFlextTargetLdifWriterProperties",
    "TestFlextTargetLdifWriterRecordWriting",
    "TestIntegration",
    "attribute_mapping",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "ldif_options",
    "m",
    "models",
    "multiple_records",
    "p",
    "protocols",
    "pytest_configure",
    "r",
    "s",
    "sample_config",
    "sample_record",
    "sample_schema",
    "t",
    "temp_dir",
    "temp_file",
    "test_target",
    "test_writer",
    "tm",
    "tp",
    "tt",
    "tu",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
