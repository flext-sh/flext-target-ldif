# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Init module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

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
    from tests.typings import (
        FlextTargetLdifTestTypes,
        FlextTargetLdifTestTypes as t,
        tt,
    )
    from tests.utilities import (
        FlextTargetLdifTestUtilities,
        FlextTargetLdifTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "EXPECTED_BULK_SIZE": ["tests.test_writer", "EXPECTED_BULK_SIZE"],
    "EXPECTED_DATA_COUNT": ["tests.test_writer", "EXPECTED_DATA_COUNT"],
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
    "d": ["flext_tests", "d"],
    "e": ["flext_tests", "e"],
    "h": ["flext_tests", "h"],
    "ldif_options": ["tests.conftest", "ldif_options"],
    "m": ["tests.models", "FlextTargetLdifTestModels"],
    "multiple_records": ["tests.conftest", "multiple_records"],
    "p": ["tests.protocols", "FlextTargetLdifTestProtocols"],
    "pytest_configure": ["tests.conftest", "pytest_configure"],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "sample_config": ["tests.conftest", "sample_config"],
    "sample_record": ["tests.conftest", "sample_record"],
    "sample_schema": ["tests.conftest", "sample_schema"],
    "t": ["tests.typings", "FlextTargetLdifTestTypes"],
    "temp_dir": ["tests.conftest", "temp_dir"],
    "temp_file": ["tests.conftest", "temp_file"],
    "tm": ["tests.models", "tm"],
    "tt": ["tests.typings", "tt"],
    "u": ["tests.utilities", "FlextTargetLdifTestUtilities"],
    "x": ["flext_tests", "x"],
}

__all__ = [
    "EXPECTED_BULK_SIZE",
    "EXPECTED_DATA_COUNT",
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
    "d",
    "e",
    "h",
    "ldif_options",
    "m",
    "multiple_records",
    "p",
    "pytest_configure",
    "r",
    "s",
    "sample_config",
    "sample_record",
    "sample_schema",
    "t",
    "temp_dir",
    "temp_file",
    "tm",
    "tt",
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
