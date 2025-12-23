"""Exceptions for flext-target-ldif.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations


class FlextTargetLdifWriterError(Exception):
    """Error raised when LDIF writer operations fail."""

    def __init__(self, message: str, details: dict | None = None) -> None:
        """Initialize writer error with message and optional details."""
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        """Return string representation of the error."""
        return f"FlextTargetLdifWriterError: {self.message}"


__all__ = ["FlextTargetLdifWriterError"]
