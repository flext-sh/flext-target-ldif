"""Exceptions for flext-target-ldif.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import override

from flext_core import e


class FlextTargetLdifWriterError(e.OperationError):
    """Error raised when LDIF writer operations fail."""

    details: Mapping[str, str]

    def __init__(self, message: str, details: Mapping[str, str] | None = None) -> None:
        """Initialize writer error with message and optional details."""
        super().__init__(message, reason=str(details) if details else None)
        self.details = details if details is not None else {}

    @override
    def __str__(self) -> str:
        """Return string representation of the error."""
        return f"FlextTargetLdifWriterError: {self.message}"


__all__ = ["FlextTargetLdifWriterError"]
