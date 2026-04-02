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
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_tests import d, e, h, r, s, x

    from flext_core import FlextTypes
    from tests import (
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

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
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
    "d": "flext_tests",
    "e": "flext_tests",
    "h": "flext_tests",
    "ldif_options": "tests.conftest",
    "m": ("tests.models", "FlextTargetLdifTestModels"),
    "models": "tests.models",
    "multiple_records": "tests.conftest",
    "p": ("tests.protocols", "FlextTargetLdifTestProtocols"),
    "protocols": "tests.protocols",
    "pytest_configure": "tests.conftest",
    "r": "flext_tests",
    "s": "flext_tests",
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
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
