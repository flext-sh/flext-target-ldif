"""Data transformation utilities for LDIF target using flext-ldap infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from datetime import datetime
from typing import override


from flext_target_ldif.typings import t
from flext_core import u


def transform_timestamp(value: object) -> str:
    """Transform timestamp values to LDAP timestamp format using flext-ldap."""
    if value is None:
        return ""
    if value.__class__ is datetime:
        # ISO 8601 representation compatible with many systems
        return value.isoformat()
    if u.Guards._is_str(value):
        try:
            # Try to parse ISO format first, then use flext-ldap parsing
            dt = datetime.fromisoformat(value.removesuffix("Z") + "+00:00")
            return dt.isoformat()
        except ValueError:
            # Return as-is if not parseable
            return value
    # Fallback - convert to string for other types
    return str(value)


def transform_boolean(value: object) -> str:
    """Transform boolean values to LDAP boolean format."""
    if u.Guards._is_bool(value):
        return "TRUE" if value else "FALSE"
    if u.Guards._is_str(value):
        lower_val = value.lower()
        if lower_val in {"true", "yes", "1", "on"}:
            return "TRUE"
        if lower_val in {"false", "no", "0", "off"}:
            return "FALSE"
    return ""


def transform_email(value: object) -> str:
    """Transform email values to ensure LDAP compatibility."""
    email_str = str(value).strip().lower()
    # Basic email validation and cleanup
    if "@" in email_str and "." in email_str:
        return email_str
    return ""


def transform_phone(value: object) -> str:
    """Transform phone numbers to standard format."""
    phone_str = str(value)
    # Remove common formatting characters
    return "".join(c for c in phone_str if c.isdigit() or c in "+- ()")


def transform_name(value: object) -> str:
    """Transform name fields to ensure proper formatting."""
    name_str = str(value).strip()
    # Capitalize first letter of each word
    return " ".join(word.capitalize() for word in name_str.split())


def _get_builtin_transformer(attr_name: str) -> Callable[[object], str] | None:
    """Get built-in transformer function for attribute name."""
    attr_lower = attr_name.lower()
    if attr_lower in {"mail", "email"}:
        return transform_email
    if attr_lower in {"telephonenumber", "phone", "mobile"}:
        return transform_phone
    if attr_lower in {"givenname", "sn", "cn", "displayname"}:
        return transform_name
    if attr_lower in {"createtimestamp", "modifytimestamp"}:
        return transform_timestamp
    if attr_lower.endswith("boolean") or attr_lower.startswith("is"):
        return transform_boolean
    return None


def normalize_attribute_value(
    attr_name: str,
    value: object,
    transformers: Mapping[str, Callable[[object], str]] | None = None,
) -> str:
    """Normalize attribute value based on attribute type."""
    # Use custom transformers if provided
    if transformers and attr_name in transformers:
        return transformers[attr_name](value)
    # Try built-in transformations
    builtin_transformer = _get_builtin_transformer(attr_name)
    if builtin_transformer:
        return builtin_transformer(value)
    # Default: convert to string and strip whitespace
    return str(value).strip()


class RecordTransformer:
    """Transform Singer records for LDIF output."""

    @override
    def __init__(
        self,
        attribute_mapping: Mapping[str, str] | None = None,
        custom_transformers: Mapping[str, Callable[[object], str]] | None = None,
    ) -> None:
        """Initialize the record transformer."""
        self.attribute_mapping = attribute_mapping or {}
        self.custom_transformers = custom_transformers or {}

    def transform_record(
        self, record: Mapping[str, t.GeneralValueType]
    ) -> Mapping[str, str]:
        """Transform a Singer record to LDAP-compatible format."""
        transformed = {}
        for field, value in record.items():
            # Skip None values
            if value is None:
                continue
            # Map field name if needed
            if field in self.attribute_mapping:
                attr_name = self.attribute_mapping[field]
            else:
                # Default mapping: convert to lowercase, remove underscores
                attr_name = field.lower().replace("_", "")
            # Transform value
            transformed_value = normalize_attribute_value(
                attr_name,
                value,
                self.custom_transformers,
            )
            # Only include non-empty values
            if transformed_value:
                transformed[attr_name] = transformed_value
        return transformed

    @staticmethod
    def add_required_attributes(
        record: Mapping[str, str],
    ) -> Mapping[str, t.GeneralValueType]:
        """Add required LDAP attributes to the record."""
        result: dict[str, t.GeneralValueType] = dict(record)
        # Ensure objectClass is present
        if "objectclass" not in result:
            result["objectclass"] = ["inetOrgPerson", "person"]
        # Ensure cn (common name) is present
        if "cn" not in result:
            # Try to build from other name fields
            if "givenname" in result and "sn" in result:
                result["cn"] = f"{result['givenname']} {result['sn']}"
            elif "displayname" in result:
                result["cn"] = result["displayname"]
            elif "uid" in result:
                result["cn"] = result["uid"]
                result["cn"] = "Unknown User"
        # Ensure sn (surname) is present for person objectClass
        if "sn" not in result and "cn" in result:
            # Use last word of cn as surname
            cn_value = result["cn"]
            words: list[str] = cn_value.split() if u.Guards._is_str(cn_value) else []
            result["sn"] = words[-1] if words else "Unknown"
            result["sn"] = "Unknown"
        return result
