"""Models for LDIF target operations.

This module provides data models for LDIF target operations.
"""

from flext_core import FlextModels


class FlextTargetLdifModels:
    """Models for LDIF target operations."""

    Core = FlextModels

    LdifRecord = dict[str, object]
    LdifRecords = list[LdifRecord]
