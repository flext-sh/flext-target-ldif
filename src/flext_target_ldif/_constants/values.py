"""Scalar constants for flext-target-ldif.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar


class FlextTargetLdifConstantsValues:
    """Scalar constants mixed into ``c.TargetLdif``."""

    TARGET_NAME: ClassVar[str] = "target-ldif"
    DEFAULT_OUTPUT_PATH: ClassVar[str] = "./output"
    DEFAULT_DN_TEMPLATE: ClassVar[str] = "uid={uid},ou=users,dc=example,dc=com"
    DEFAULT_LINE_LENGTH: ClassVar[int] = 78
    DEFAULT_OUTPUT_FILE: ClassVar[str] = "output.ldif"


__all__: list[str] = ["FlextTargetLdifConstantsValues"]
