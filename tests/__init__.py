# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Init module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from .conftest import (
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
    from .constants import TestsFlextTargetLdifConstants, c
    from .models import TestsFlextTargetLdifModels, tm
    from .protocols import TestsFlextTargetLdifProtocols
    from .test_target import (
        TestFlextTargetLdif,
        TestFlextTargetLdifSettings,
        TestIntegration,
        TestTargetLDIF,
    )
    from .test_writer import (
        EXPECTED_BULK_SIZE,
        EXPECTED_DATA_COUNT,
        TestLdifWriterBase64Encoding,
        TestLdifWriterContextManager,
        TestLdifWriterDnGeneration,
        TestLdifWriterFileOperations,
        TestLdifWriterHeaderGeneration,
        TestLdifWriterInitialization,
        TestLdifWriterLineWrapping,
        TestLdifWriterProperties,
        TestLdifWriterRecordWriting,
    )
    from .tm import m
    from .tp import p
    from .typings import TestsFlextTargetLdifTypes, t, tt
    from .utilities import TestsFlextTargetLdifUtilities, u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "EXPECTED_BULK_SIZE": ("tests.test_writer", "EXPECTED_BULK_SIZE"),
    "EXPECTED_DATA_COUNT": ("tests.test_writer", "EXPECTED_DATA_COUNT"),
    "TestFlextTargetLdif": ("tests.test_target", "TestFlextTargetLdif"),
    "TestFlextTargetLdifSettings": ("tests.test_target", "TestFlextTargetLdifSettings"),
    "TestIntegration": ("tests.test_target", "TestIntegration"),
    "TestLdifWriterBase64Encoding": (
        "tests.test_writer",
        "TestLdifWriterBase64Encoding",
    ),
    "TestLdifWriterContextManager": (
        "tests.test_writer",
        "TestLdifWriterContextManager",
    ),
    "TestLdifWriterDnGeneration": ("tests.test_writer", "TestLdifWriterDnGeneration"),
    "TestLdifWriterFileOperations": (
        "tests.test_writer",
        "TestLdifWriterFileOperations",
    ),
    "TestLdifWriterHeaderGeneration": (
        "tests.test_writer",
        "TestLdifWriterHeaderGeneration",
    ),
    "TestLdifWriterInitialization": (
        "tests.test_writer",
        "TestLdifWriterInitialization",
    ),
    "TestLdifWriterLineWrapping": ("tests.test_writer", "TestLdifWriterLineWrapping"),
    "TestLdifWriterProperties": ("tests.test_writer", "TestLdifWriterProperties"),
    "TestLdifWriterRecordWriting": ("tests.test_writer", "TestLdifWriterRecordWriting"),
    "TestTargetLDIF": ("tests.test_target", "TestTargetLDIF"),
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
    "attribute_mapping": ("tests.conftest", "attribute_mapping"),
    "c": ("tests.constants", "c"),
    "ldif_options": ("tests.conftest", "ldif_options"),
    "m": ("tests.tm", "m"),
    "multiple_records": ("tests.conftest", "multiple_records"),
    "p": ("tests.tp", "p"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "sample_config": ("tests.conftest", "sample_config"),
    "sample_record": ("tests.conftest", "sample_record"),
    "sample_schema": ("tests.conftest", "sample_schema"),
    "t": ("tests.typings", "t"),
    "temp_dir": ("tests.conftest", "temp_dir"),
    "temp_file": ("tests.conftest", "temp_file"),
    "tm": ("tests.models", "tm"),
    "tt": ("tests.typings", "tt"),
    "u": ("tests.utilities", "u"),
}

__all__ = [
    "EXPECTED_BULK_SIZE",
    "EXPECTED_DATA_COUNT",
    "TestFlextTargetLdif",
    "TestFlextTargetLdifSettings",
    "TestIntegration",
    "TestLdifWriterBase64Encoding",
    "TestLdifWriterContextManager",
    "TestLdifWriterDnGeneration",
    "TestLdifWriterFileOperations",
    "TestLdifWriterHeaderGeneration",
    "TestLdifWriterInitialization",
    "TestLdifWriterLineWrapping",
    "TestLdifWriterProperties",
    "TestLdifWriterRecordWriting",
    "TestTargetLDIF",
    "TestsFlextTargetLdifConstants",
    "TestsFlextTargetLdifModels",
    "TestsFlextTargetLdifProtocols",
    "TestsFlextTargetLdifTypes",
    "TestsFlextTargetLdifUtilities",
    "attribute_mapping",
    "c",
    "ldif_options",
    "m",
    "multiple_records",
    "p",
    "pytest_configure",
    "sample_config",
    "sample_record",
    "sample_schema",
    "t",
    "temp_dir",
    "temp_file",
    "tm",
    "tt",
    "u",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
