"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants
from flext_ldif.constants import FlextLdifConstants


class FlextTargetLdifConstants(FlextConstants):
    """LDIF target export-specific constants following flext-core patterns.

    Composes with FlextLdifConstants to avoid duplication and ensure consistency.
    """

    # LDIF File Configuration using composition
    DEFAULT_LDIF_ENCODING = FlextLdifConstants.Encoding.DEFAULT_ENCODING
    DEFAULT_LINE_LENGTH = FlextLdifConstants.Format.MAX_LINE_LENGTH
    MAX_LINE_LENGTH = 1024

    # Singer Target Configuration - using FlextConstants composition
    DEFAULT_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
    MAX_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.MAX_ITEMS

    # LDIF Format Options using composition
    SUPPORTED_ENCODINGS: ClassVar[list[str]] = list(
        FlextLdifConstants.Encoding.SUPPORTED_ENCODINGS,
    )

    class Processing:
        """LDIF target processing configuration."""

        MIN_WORKERS_FOR_PARALLEL = (
            FlextLdifConstants.Processing.MIN_WORKERS_FOR_PARALLEL
        )
        MAX_WORKERS_LIMIT = FlextLdifConstants.Processing.MAX_WORKERS_LIMIT
        PERFORMANCE_MIN_CHUNK_SIZE = (
            FlextLdifConstants.Processing.PERFORMANCE_MIN_CHUNK_SIZE
        )

    class Format:
        """LDIF format specifications."""

        DN_ATTRIBUTE = FlextLdifConstants.Format.DN_ATTRIBUTE
        ATTRIBUTE_SEPARATOR = FlextLdifConstants.Format.ATTRIBUTE_SEPARATOR
        BASE64_PREFIX = FlextLdifConstants.Format.BASE64_PREFIX
        COMMENT_PREFIX = FlextLdifConstants.Format.COMMENT_PREFIX

    class Validation:
        """LDIF validation constants."""

        MIN_DN_COMPONENTS = FlextLdifConstants.LdifValidation.MIN_DN_COMPONENTS
        MAX_DN_LENGTH = FlextLdifConstants.LdifValidation.MAX_DN_LENGTH
        MAX_ATTRIBUTES_PER_ENTRY = (
            FlextLdifConstants.LdifValidation.MAX_ATTRIBUTES_PER_ENTRY
        )
        MAX_ATTRIBUTE_VALUE_LENGTH = 1000


__all__ = ["FlextTargetLdifConstants"]
