"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants


class FlextTargetLdifConstants(FlextConstants):
    """LDIF target export-specific constants following flext-core patterns."""

    # LDIF File Configuration
    DEFAULT_LDIF_ENCODING = "utf-8"
    DEFAULT_LINE_LENGTH = 78
    MAX_LINE_LENGTH = 1024

    # Singer Target Configuration
    DEFAULT_BATCH_SIZE = 1000
    MAX_BATCH_SIZE = 10000

    # LDIF Format Options
    SUPPORTED_ENCODINGS: ClassVar[list[str]] = ["utf-8", "utf-16", "latin-1"]


__all__ = ["FlextTargetLdifConstants"]
