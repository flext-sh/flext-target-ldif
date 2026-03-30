# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Init module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import d, e, h, r, s, x

    from tests import (
        conftest as conftest,
        constants as constants,
        models as models,
        protocols as protocols,
        test_target as test_target,
        test_writer as test_writer,
        tp as tp,
        tt as tt,
        tu as tu,
        typings as typings,
        utilities as utilities,
    )
    from tests.conftest import (
        attribute_mapping as attribute_mapping,
        ldif_options as ldif_options,
        multiple_records as multiple_records,
        pytest_configure as pytest_configure,
        sample_config as sample_config,
        sample_record as sample_record,
        sample_schema as sample_schema,
        temp_dir as temp_dir,
        temp_file as temp_file,
    )
    from tests.constants import (
        FlextTargetLdifTestConstants as FlextTargetLdifTestConstants,
        FlextTargetLdifTestConstants as c,
    )
    from tests.models import (
        FlextTargetLdifTestModels as FlextTargetLdifTestModels,
        FlextTargetLdifTestModels as m,
        tm as tm,
    )
    from tests.protocols import (
        FlextTargetLdifTestProtocols as FlextTargetLdifTestProtocols,
        FlextTargetLdifTestProtocols as p,
    )
    from tests.test_target import (
        FlextTargetLdifSink as FlextTargetLdifSink,
        TestFlextTargetLdif as TestFlextTargetLdif,
        TestFlextTargetLdifClass as TestFlextTargetLdifClass,
        TestFlextTargetLdifSettings as TestFlextTargetLdifSettings,
        TestIntegration as TestIntegration,
    )
    from tests.test_writer import (
        EXPECTED_BULK_SIZE as EXPECTED_BULK_SIZE,
        EXPECTED_DATA_COUNT as EXPECTED_DATA_COUNT,
        TestFlextTargetLdifWriterBase64Encoding as TestFlextTargetLdifWriterBase64Encoding,
        TestFlextTargetLdifWriterContextManager as TestFlextTargetLdifWriterContextManager,
        TestFlextTargetLdifWriterDnGeneration as TestFlextTargetLdifWriterDnGeneration,
        TestFlextTargetLdifWriterFileOperations as TestFlextTargetLdifWriterFileOperations,
        TestFlextTargetLdifWriterHeaderGeneration as TestFlextTargetLdifWriterHeaderGeneration,
        TestFlextTargetLdifWriterInitialization as TestFlextTargetLdifWriterInitialization,
        TestFlextTargetLdifWriterLineWrapping as TestFlextTargetLdifWriterLineWrapping,
        TestFlextTargetLdifWriterProperties as TestFlextTargetLdifWriterProperties,
        TestFlextTargetLdifWriterRecordWriting as TestFlextTargetLdifWriterRecordWriting,
    )
    from tests.typings import (
        FlextTargetLdifTestTypes as FlextTargetLdifTestTypes,
        FlextTargetLdifTestTypes as t,
    )
    from tests.utilities import (
        FlextTargetLdifTestUtilities as FlextTargetLdifTestUtilities,
        FlextTargetLdifTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "EXPECTED_BULK_SIZE": ["tests.test_writer", "EXPECTED_BULK_SIZE"],
    "EXPECTED_DATA_COUNT": ["tests.test_writer", "EXPECTED_DATA_COUNT"],
    "FlextTargetLdifSink": ["tests.test_target", "FlextTargetLdifSink"],
    "FlextTargetLdifTestConstants": ["tests.constants", "FlextTargetLdifTestConstants"],
    "FlextTargetLdifTestModels": ["tests.models", "FlextTargetLdifTestModels"],
    "FlextTargetLdifTestProtocols": ["tests.protocols", "FlextTargetLdifTestProtocols"],
    "FlextTargetLdifTestTypes": ["tests.typings", "FlextTargetLdifTestTypes"],
    "FlextTargetLdifTestUtilities": ["tests.utilities", "FlextTargetLdifTestUtilities"],
    "TestFlextTargetLdif": ["tests.test_target", "TestFlextTargetLdif"],
    "TestFlextTargetLdifClass": ["tests.test_target", "TestFlextTargetLdifClass"],
    "TestFlextTargetLdifSettings": ["tests.test_target", "TestFlextTargetLdifSettings"],
    "TestFlextTargetLdifWriterBase64Encoding": ["tests.test_writer", "TestFlextTargetLdifWriterBase64Encoding"],
    "TestFlextTargetLdifWriterContextManager": ["tests.test_writer", "TestFlextTargetLdifWriterContextManager"],
    "TestFlextTargetLdifWriterDnGeneration": ["tests.test_writer", "TestFlextTargetLdifWriterDnGeneration"],
    "TestFlextTargetLdifWriterFileOperations": ["tests.test_writer", "TestFlextTargetLdifWriterFileOperations"],
    "TestFlextTargetLdifWriterHeaderGeneration": ["tests.test_writer", "TestFlextTargetLdifWriterHeaderGeneration"],
    "TestFlextTargetLdifWriterInitialization": ["tests.test_writer", "TestFlextTargetLdifWriterInitialization"],
    "TestFlextTargetLdifWriterLineWrapping": ["tests.test_writer", "TestFlextTargetLdifWriterLineWrapping"],
    "TestFlextTargetLdifWriterProperties": ["tests.test_writer", "TestFlextTargetLdifWriterProperties"],
    "TestFlextTargetLdifWriterRecordWriting": ["tests.test_writer", "TestFlextTargetLdifWriterRecordWriting"],
    "TestIntegration": ["tests.test_target", "TestIntegration"],
    "attribute_mapping": ["tests.conftest", "attribute_mapping"],
    "c": ["tests.constants", "FlextTargetLdifTestConstants"],
    "conftest": ["tests.conftest", ""],
    "constants": ["tests.constants", ""],
    "d": ["flext_tests", "d"],
    "e": ["flext_tests", "e"],
    "h": ["flext_tests", "h"],
    "ldif_options": ["tests.conftest", "ldif_options"],
    "m": ["tests.models", "FlextTargetLdifTestModels"],
    "models": ["tests.models", ""],
    "multiple_records": ["tests.conftest", "multiple_records"],
    "p": ["tests.protocols", "FlextTargetLdifTestProtocols"],
    "protocols": ["tests.protocols", ""],
    "pytest_configure": ["tests.conftest", "pytest_configure"],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "sample_config": ["tests.conftest", "sample_config"],
    "sample_record": ["tests.conftest", "sample_record"],
    "sample_schema": ["tests.conftest", "sample_schema"],
    "t": ["tests.typings", "FlextTargetLdifTestTypes"],
    "temp_dir": ["tests.conftest", "temp_dir"],
    "temp_file": ["tests.conftest", "temp_file"],
    "test_target": ["tests.test_target", ""],
    "test_writer": ["tests.test_writer", ""],
    "tm": ["tests.models", "tm"],
    "tp": ["tests.tp", ""],
    "tt": ["tests.tt", ""],
    "tu": ["tests.tu", ""],
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextTargetLdifTestUtilities"],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_tests", "x"],
}

_EXPORTS: Sequence[str] = [
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
