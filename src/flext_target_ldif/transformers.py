"""Backward-compatible re-export for FlextTargetLdifRecordTransformer.

The RecordTransformer class has been absorbed into u.TargetLdif.RecordTransformer
(utilities.py). This module re-exports the class for import compatibility.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_ldif.utilities import FlextTargetLdifRecordTransformer

__all__ = ["FlextTargetLdifRecordTransformer"]
