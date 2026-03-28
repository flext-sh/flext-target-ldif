"""Backward-compatible re-export for FlextTargetLdifSink.

The Sink class has been absorbed into m.TargetLdif.Sink (models.py).
This module re-exports the class for import compatibility.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_ldif.models import FlextTargetLdifSink

__all__ = ["FlextTargetLdifSink"]
