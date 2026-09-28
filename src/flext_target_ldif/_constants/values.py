"""Scalar constants for flext-target-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextTargetLdifConstantsValues:
    """Scalar constants mixed into ``c.TargetLdif``."""

    class TargetLdif:
        DEFAULT_OUTPUT_PATH: Final[str] = "./output"
        DEFAULT_FILE_NAMING_PATTERN: Final[str] = "{stream_name}.ldif"
        DEFAULT_DN_TEMPLATE: Final[str] = "uid={uid},ou=users,dc=example,dc=com"
        DEFAULT_LINE_LENGTH: Final[int] = 78
        """Target LDIF scalar constants."""

        DEFAULT_OUTPUT_FILE: Final[str] = "output.ldif"


__all__: list[str] = ["FlextTargetLdifConstantsValues"]
