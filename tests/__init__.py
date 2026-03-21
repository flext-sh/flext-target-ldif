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


if TYPE_CHECKING:
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
    from .constants import (
        TestsFlextTargetLdifConstants,
        TestsFlextTargetLdifConstants as c,
    )
    from .models import TestsFlextTargetLdifModels, TestsFlextTargetLdifModels as m, tm
    from .protocols import (
        TestsFlextTargetLdifProtocols,
        TestsFlextTargetLdifProtocols as p,
    )
    from .test_target import (
        TestFlextTargetLdifSettings,
        TestIntegration,
        TestTargetLDIF,
        TestTargetLDIFClass,
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
    from .typings import TestsFlextTargetLdifTypes, TestsFlextTargetLdifTypes as t, tt
    from .utilities import (
        TestsFlextTargetLdifUtilities,
        TestsFlextTargetLdifUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "EXPECTED_BULK_SIZE": ("tests.test_writer", "EXPECTED_BULK_SIZE"),
    "EXPECTED_DATA_COUNT": ("tests.test_writer", "EXPECTED_DATA_COUNT"),
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
    "TestTargetLDIFClass": ("tests.test_target", "TestTargetLDIFClass"),
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
    "c": ("tests.constants", "TestsFlextTargetLdifConstants"),
    "ldif_options": ("tests.conftest", "ldif_options"),
    "m": ("tests.models", "TestsFlextTargetLdifModels"),
    "multiple_records": ("tests.conftest", "multiple_records"),
    "p": ("tests.protocols", "TestsFlextTargetLdifProtocols"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "sample_config": ("tests.conftest", "sample_config"),
    "sample_record": ("tests.conftest", "sample_record"),
    "sample_schema": ("tests.conftest", "sample_schema"),
    "t": ("tests.typings", "TestsFlextTargetLdifTypes"),
    "temp_dir": ("tests.conftest", "temp_dir"),
    "temp_file": ("tests.conftest", "temp_file"),
    "tm": ("tests.models", "tm"),
    "tt": ("tests.typings", "tt"),
    "u": ("tests.utilities", "TestsFlextTargetLdifUtilities"),
}

__all__ = [
    "EXPECTED_BULK_SIZE",
    "EXPECTED_DATA_COUNT",
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
    "TestTargetLDIFClass",
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


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
