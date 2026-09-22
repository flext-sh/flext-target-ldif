"""Scalar constants for flext-target-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextTargetLdifConstantsValues:
    """Scalar constants mixed into ``c.TargetLdif``."""

    class TargetLdif:
        """Target LDIF scalar constants."""

        DEFAULT_OUTPUT_FILE: Final[str] = "output.ldif"


__all__: list[str] = ["FlextTargetLdifConstantsValues"]
