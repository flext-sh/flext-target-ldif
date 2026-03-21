"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_core import FlextConstants
from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants


class FlextTargetLdifConstants(FlextMeltanoConstants, FlextLdifConstants):
    """LDIF target export-specific constants following flext-core patterns.

    Composes with FlextLdifConstants to avoid duplication and ensure consistency.
    """

    DEFAULT_LDIF_ENCODING: Final[str] = FlextLdifConstants.Ldif.DEFAULT_ENCODING
    DEFAULT_LINE_LENGTH: Final[int] = FlextLdifConstants.Ldif.Format.MAX_LINE_LENGTH
    MAX_LINE_LENGTH: Final[int] = 1024
    MIN_LINE_LENGTH: Final[int] = 40
    STANDARD_LINE_LENGTH: Final[int] = 78
    MAX_DN_LENGTH: Final[int] = 1000
    MAX_BATCH_SIZE: Final[int] = FlextConstants.MAX_ITEMS
    SUPPORTED_ENCODINGS: Final[frozenset[str]] = frozenset([
        "utf-8",
        "utf-16",
        "utf-32",
        "ascii",
        "latin-1",
        "cp1252",
    ])
    DEV_FILE_PATTERN: Final[str] = "dev_{stream_name}_{timestamp}.ldif"
    PROD_FILE_PATTERN: Final[str] = "prod_{stream_name}_{timestamp}.ldif"
    TEST_FILE_PATTERN: Final[str] = "test_{stream_name}.ldif"
    DEFAULT_FILE_PATTERN: Final[str] = "{stream_name}_{timestamp}.ldif"
    DEV_LINE_LENGTH_OFFSET: Final[int] = 42
    ASCII_SPACE: Final[int] = 32
    ASCII_TILDE: Final[int] = 126
    LDIF_LINE_WRAP_LENGTH: Final[int] = 76

    @unique
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

    @unique
    class ProjectType(StrEnum):
        """Project type literals for target package metadata."""

        LIBRARY = "library"
        APPLICATION = "application"
        SERVICE = "service"
        TARGET_LDIF = "target-ldif"
        SINGER_TARGET = "singer-target"
        LDIF_EXPORT = "ldif-export"
        SINGER_LDIF_TARGET = "singer-ldif-target"
        LDIF_FILE_TARGET = "ldif-file-target"
        SINGER_PROTOCOL_TARGET = "singer-protocol-target"
        DATA_EXPORT_TARGET = "data-export-target"
        LDIF_GENERATOR = "ldif-generator"
        SINGER_TO_LDIF = "singer-to-ldif"
        LDIF_EXPORT_SERVICE = "ldif-export-service"
        TARGET_LDIF_SINGER = "target-ldif-singer"
        LDIF_FILE_EXPORT = "ldif-file-export"
        SINGER_LDIF_EXPORT = "singer-ldif-export"
        LDIF_DATA_TARGET = "ldif-data-target"
        EXPORT_TARGET_LDIF = "export-target-ldif"
        SINGER_EXPORT_TARGET = "singer-export-target"
        LDIF_STREAMING_TARGET = "ldif-streaming-target"
        LDIF_BATCH_EXPORT = "ldif-batch-export"
        SINGER_FILE_TARGET = "singer-file-target"

    @unique
    class ErrorTypeLiteral(StrEnum):
        """Error category literals for target operations."""

        FORMAT_VALIDATION = "FORMAT_VALIDATION"
        FILE_IO = "FILE_IO"
        TRANSFORMATION = "TRANSFORMATION"
        SINGER_PROTOCOL = "SINGER_PROTOCOL"
        CONFIGURATION = "CONFIGURATION"
        DISK_SPACE = "DISK_SPACE"
        PERMISSION = "PERMISSION"
        ENCODING = "ENCODING"


c = FlextTargetLdifConstants
__all__ = ["FlextTargetLdifConstants", "c"]
