"""Exceptions for flext-target-ldif.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import e
from flext_core._models.containers import FlextModelsContainers  # noqa: PLC2701


class FlextTargetLdifWriterError(e.OperationError):
    """Error raised when LDIF writer operations fail."""

    details: FlextModelsContainers.ConfigMap

    def __init__(self, message: str, details: FlextModelsContainers.ConfigMap | None = None) -> None:
        """Initialize writer error with message and optional details."""
        super().__init__(message, reason=str(details) if details else None)
        self.details = details if details is not None else FlextModelsContainers.ConfigMap(root={})

    @override
    def __str__(self) -> str:
        """Return string representation of the error."""
        return f"FlextTargetLdifWriterError: {self.message}"


__all__ = ["FlextTargetLdifWriterError"]
