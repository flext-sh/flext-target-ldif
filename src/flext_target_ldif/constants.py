"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import Final

from flext_core import FlextConstants
from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants


class FlextMeltanoTargetLdifConstants(FlextMeltanoConstants, FlextLdifConstants):
    """LDIF target export-specific constants following flext-core patterns.

    Composes with FlextLdifConstants to avoid duplication and ensure consistency.
    """

    # LDIF File Configuration using composition
    DEFAULT_LDIF_ENCODING: Final[str] = FlextLdifConstants.Ldif.DEFAULT_ENCODING
    DEFAULT_LINE_LENGTH: Final[int] = FlextLdifConstants.Ldif.Format.MAX_LINE_LENGTH
    MAX_LINE_LENGTH: Final[int] = 1024
    MIN_LINE_LENGTH: Final[int] = 40
    STANDARD_LINE_LENGTH: Final[int] = 78
    MAX_DN_LENGTH: Final[int] = 1000

    # Singer Target Configuration - using FlextConstants composition
    # Note: DEFAULT_BATCH_SIZE inherited from FlextConstants (Final, cannot override)
    MAX_BATCH_SIZE: Final[int] = FlextConstants.Performance.BatchProcessing.MAX_ITEMS

    # LDIF Format Options using composition
    SUPPORTED_ENCODINGS: Final[frozenset[str]] = frozenset([
        "utf-8",
        "utf-16",
        "utf-32",
        "ascii",
        "latin-1",
        "cp1252",
    ])

    # File naming patterns for different environments
    DEV_FILE_PATTERN: Final[str] = "dev_{stream_name}_{timestamp}.ldif"
    PROD_FILE_PATTERN: Final[str] = "prod_{stream_name}_{timestamp}.ldif"
    TEST_FILE_PATTERN: Final[str] = "test_{stream_name}.ldif"
    DEFAULT_FILE_PATTERN: Final[str] = "{stream_name}_{timestamp}.ldif"

    # Development environment offset for line length
    DEV_LINE_LENGTH_OFFSET: Final[int] = 42

    # ASCII character constants for LDIF encoding
    ASCII_SPACE: Final[int] = 32
    ASCII_TILDE: Final[int] = 126
    LDIF_LINE_WRAP_LENGTH: Final[int] = 76

    class ErrorType(StrEnum):
        """LDIF target error types using StrEnum for type safety.

        DRY Pattern:
            StrEnum is the single source of truth. Use ErrorType.FORMAT_VALIDATION.value
            or ErrorType.FORMAT_VALIDATION directly - no base strings needed.
        """

        FORMAT_VALIDATION = "FORMAT_VALIDATION"
        FILE_IO = "FILE_IO"
        TRANSFORMATION = "TRANSFORMATION"
        SINGER_PROTOCOL = "SINGER_PROTOCOL"
        CONFIGURATION = "CONFIGURATION"
        DISK_SPACE = "DISK_SPACE"
        PERMISSION = "PERMISSION"
        ENCODING = "ENCODING"

    class TargetLdif:
        """LDIF target processing configuration.

        Note: Does not override parent Processing class to avoid inheritance conflicts.
        """

        MIN_WORKERS_FOR_PARALLEL: Final[int] = (
            FlextLdifConstants.Ldif.LdifProcessing.MIN_WORKERS_FOR_PARALLEL
        )
        MAX_WORKERS_LIMIT: Final[int] = (
            FlextLdifConstants.Ldif.LdifProcessing.MAX_WORKERS_LIMIT
        )
        PERFORMANCE_MIN_CHUNK_SIZE: Final[int] = (
            FlextLdifConstants.Ldif.LdifProcessing.PERFORMANCE_MIN_CHUNK_SIZE
        )

    class Format:
        """LDIF format specifications."""

        DN_ATTRIBUTE: Final[str] = FlextLdifConstants.Ldif.Format.DN_ATTRIBUTE
        ATTRIBUTE_SEPARATOR: Final[str] = (
            FlextLdifConstants.Ldif.Format.ATTRIBUTE_SEPARATOR
        )
        BASE64_PREFIX: Final[str] = FlextLdifConstants.Ldif.Format.BASE64_PREFIX
        COMMENT_PREFIX: Final[str] = FlextLdifConstants.Ldif.Format.COMMENT_PREFIX

    class TargetLdifValidation:
        """LDIF validation constants.

        Note: Does not override parent Validation class to avoid inheritance conflicts.
        """

        MIN_DN_COMPONENTS: Final[int] = (
            FlextLdifConstants.Ldif.LdifValidation.MIN_DN_COMPONENTS
        )
        MAX_DN_LENGTH: Final[int] = FlextLdifConstants.Ldif.LdifValidation.MAX_DN_LENGTH
        MAX_ATTRIBUTES_PER_ENTRY: Final[int] = (
            FlextLdifConstants.Ldif.LdifValidation.MAX_ATTRIBUTES_PER_ENTRY
        )
        MAX_ATTRIBUTE_VALUE_LENGTH: Final[int] = 1000
        MAX_DN_COMPONENTS: Final[int] = 10


c = FlextMeltanoTargetLdifConstants
FlextTargetLdifConstants = FlextMeltanoTargetLdifConstants

__all__ = ["FlextMeltanoTargetLdifConstants", "FlextTargetLdifConstants", "c"]
