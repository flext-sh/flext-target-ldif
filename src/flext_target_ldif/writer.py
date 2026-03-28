"""Re-export shim — canonical implementation lives in _utilities.writer."""

from __future__ import annotations

from flext_target_ldif._utilities.writer import FlextTargetLdifWriter, logger

__all__ = ["FlextTargetLdifWriter", "logger"]
