"""Exceptions for flext-target-ldif.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_target_ldif import e, t


class FlextTargetLdifWriterError(e.OperationError):
    """Error raised when LDIF writer operations fail."""

    details: t.StrMapping

    def __init__(self, message: str, details: t.StrMapping | None = None) -> None:
        """Initialize writer error with message and optional details."""
        reason = str(details) if details else ""
        super().__init__(message, reason=reason)
        self.details = details if details is not None else {}

    @override
    def __str__(self) -> str:
        """Return string representation of the error."""
        return f"FlextTargetLdifWriterError: {self.message}"


__all__: list[str] = ["FlextTargetLdifWriterError"]
