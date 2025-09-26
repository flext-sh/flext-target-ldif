"""Module docstring."""

from __future__ import annotations

"""Models for LDIF target operations.

This module provides data models for LDIF target operations.
"""

from flext_core import FlextModels


class FlextTargetLdifModels(FlextModels):
    """Models for LDIF target operations.

    Extends FlextModels to avoid duplication and ensure consistency.
    All LDIF target models benefit from FlextModels patterns.
    """

    LdifRecord = dict["str", "object"]
    LdifRecords = list[LdifRecord]
