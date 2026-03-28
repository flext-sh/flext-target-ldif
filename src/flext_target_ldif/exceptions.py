"""Backward-compatible re-export for FlextTargetLdifWriterError.

The canonical location is now errors.py.
This module re-exports for import compatibility.

Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_ldif.errors import FlextTargetLdifWriterError

__all__ = ["FlextTargetLdifWriterError"]
