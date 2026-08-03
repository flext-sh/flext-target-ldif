"""FLEXT Target LDIF Constants - LDIF target export constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Final

from flext_ldif import FlextLdifConstants
from flext_meltano import c

if TYPE_CHECKING:
    from flext_meltano import t


class FlextTargetLdifConstants(c, FlextLdifConstants):
    """LDIF target export-specific constants following flext-core patterns."""

    class TargetLdif:
        """Target LDIF domain constants namespace."""

        DEFAULT_OUTPUT_FILE: Final[str] = "output.ldif"
        DEFAULT_OUTPUT_PATH: Final[str] = "./output"
        DEFAULT_FILE_NAMING_PATTERN: Final[str] = "{stream_name}.ldif"
        DEFAULT_DN_TEMPLATE: Final[str] = "uid={uid},ou=users,dc=example,dc=com"
        DEFAULT_LINE_LENGTH: Final[int] = 78

        STANDARD_LINE_LENGTH: Final[int] = 78
        ASCII_SPACE: Final[int] = 32
        ASCII_TILDE: Final[int] = 126
        LDIF_LINE_WRAP_LENGTH: Final[int] = 76


c = FlextTargetLdifConstants

__all__: t.StrSequence = ("FlextTargetLdifConstants", "c")
