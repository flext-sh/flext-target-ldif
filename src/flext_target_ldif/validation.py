"""Data validation utilities for LDIF target using flext-ldap infrastructure.

Eliminates code duplication by using LDAP validation functionality from flext-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import re

from flext_core import FlextTypes
from flext_target_ldif.constants import FlextTargetLdifConstants


class ValidationError(Exception):
    """Error raised when record validation fails."""


def validate_dn_component(value: str) -> bool:
    """Validate a DN component value."""
    if not value:
        return False
    # Basic DN component validation
    return bool(re.match(r"^[a-zA-Z0-9\s\-\.@_]+$", value))


def validate_attribute_name(name: str) -> bool:
    """Validate LDAP attribute name."""
    if not name:
        return False
    # Basic LDAP attribute name validation
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9\-]*$", name))


# Constants for validation limits - moved to FlextTargetLdifConstants.Validation.MAX_ATTRIBUTE_VALUE_LENGTH


def validate_attribute_value(value: object) -> bool:
    """Validate LDAP attribute value."""
    if value is None:
        return False
    if isinstance(value, str):
        return (
            len(value) <= FlextTargetLdifConstants.Validation.MAX_ATTRIBUTE_VALUE_LENGTH
        )
    return True


def sanitize_attribute_name(name: str) -> str:
    """Sanitize field name to be LDAP-compatible."""
    # Basic normalization
    normalized = name.lower().strip()

    # Remove invalid characters
    sanitized = re.sub(r"[^a-zA-Z0-9\-]", "", normalized)

    # Ensure starts with letter
    if sanitized and not sanitized[0].isalpha():
        sanitized = "attr" + sanitized

    # Fallback if empty
    if not sanitized:
        sanitized = "unknownAttr"

    return sanitized


def validate_record(
    record: FlextTypes.Core.Dict,
) -> dict[str, FlextTypes.Core.StringList]:
    """Validate a record and return validation errors."""
    errors: dict[str, FlextTypes.Core.StringList] = {}

    if not record:
        errors["record"] = ["Record cannot be empty"]
        return errors

    # Check for required fields for DN generation
    has_id_field = any(
        field in record for field in ["id", "uid", "user_id", "username"]
    )

    if not has_id_field:
        errors["dn"] = [
            "Record must contain at least one ID field (id, uid, user_id, or username)",
        ]

    # Validate individual fields
    for field, value in record.items():
        field_errors: list[str] = []

        # Validate field name
        if not validate_attribute_name(field):
            field_errors.append(f"Invalid attribute name: {field}")

        # Validate field value
        if not validate_attribute_value(value):
            field_errors.append(f"Invalid attribute value for {field}")

        if field_errors:
            errors[field] = field_errors

    return errors


def validate_schema(
    schema: FlextTypes.Core.Dict,
) -> dict[str, FlextTypes.Core.StringList]:
    """Validate Singer schema for LDIF compatibility."""
    errors: dict[str, FlextTypes.Core.StringList] = {}

    if not schema:
        errors["schema"] = ["Schema cannot be empty"]
        return errors

    properties: dict[str, object] = schema.get("properties", {})
    if not properties:
        errors["properties"] = ["Schema must define properties"]
        return errors

    # Ensure properties is a dictionary for type safety
    if not isinstance(properties, dict):
        errors["properties"] = ["Properties must be a dictionary"]
        return errors

    # Check for ID-like fields
    id_fields = [
        field
        for field in properties
        if field.lower() in {"id", "uid", "user_id", "username"}
    ]

    if not id_fields:
        errors["id_fields"] = [
            "Schema should contain at least one ID field for DN generation",
        ]

    # Validate property names
    for prop_name in properties:
        if not validate_attribute_name(prop_name):
            if "invalid_properties" not in errors:
                errors["invalid_properties"] = []
            errors["invalid_properties"].append(f"Invalid property name: {prop_name}")

    return errors
