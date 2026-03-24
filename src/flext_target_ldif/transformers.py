"""Data transformation utilities for LDIF target using flext-ldap infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from datetime import datetime
from typing import override

from flext_core import t


class FlextTargetLdifRecordTransformer:
    """Transform Singer records for LDIF output."""

    @override
    def __init__(
        self,
        attribute_mapping: t.StrMapping | None = None,
        custom_transformers: Mapping[str, Callable[..., str]] | None = None,
    ) -> None:
        """Initialize the record transformer."""
        self.attribute_mapping = attribute_mapping or {}
        self.custom_transformers = custom_transformers or {}

    @staticmethod
    def transform_timestamp(value: t.ContainerValue) -> str:
        """Transform timestamp values to LDAP timestamp format using flext-ldap."""
        if value is None:
            return ""
        if isinstance(value, datetime):
            return value.isoformat()
        if isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value.removesuffix("Z") + "+00:00")
                return dt.isoformat()
            except ValueError:
                return value
        return str(value)

    @staticmethod
    def transform_boolean(value: t.ContainerValue) -> str:
        """Transform boolean values to LDAP boolean format."""
        if isinstance(value, bool):
            return "TRUE" if value else "FALSE"
        if isinstance(value, str):
            lower_val = value.lower()
            if lower_val in {"true", "yes", "1", "on"}:
                return "TRUE"
            if lower_val in {"false", "no", "0", "off"}:
                return "FALSE"
        return ""

    @staticmethod
    def transform_email(value: t.ContainerValue) -> str:
        """Transform email values to ensure LDAP compatibility."""
        email_str = str(value).strip().lower()
        if "@" in email_str and "." in email_str:
            return email_str
        return ""

    @staticmethod
    def transform_phone(value: t.ContainerValue) -> str:
        """Transform phone numbers to standard format."""
        phone_str = str(value)
        return "".join(c for c in phone_str if c.isdigit() or c in "+- ()")

    @staticmethod
    def transform_name(value: t.ContainerValue) -> str:
        """Transform name fields to ensure proper formatting."""
        name_str = str(value).strip()
        return " ".join(word.capitalize() for word in name_str.split())

    @staticmethod
    def _get_builtin_transformer(
        attr_name: str,
    ) -> Callable[[t.ContainerValue], str] | None:
        """Get built-in transformer function for attribute name."""
        attr_lower = attr_name.lower()
        if attr_lower in {"mail", "email"}:
            return FlextTargetLdifRecordTransformer.transform_email
        if attr_lower in {"telephonenumber", "phone", "mobile"}:
            return FlextTargetLdifRecordTransformer.transform_phone
        if attr_lower in {"givenname", "sn", "cn", "displayname"}:
            return FlextTargetLdifRecordTransformer.transform_name
        if attr_lower in {"createtimestamp", "modifytimestamp"}:
            return FlextTargetLdifRecordTransformer.transform_timestamp
        if attr_lower.endswith("boolean") or attr_lower.startswith("is"):
            return FlextTargetLdifRecordTransformer.transform_boolean
        return None

    @staticmethod
    def normalize_attribute_value(
        attr_name: str,
        value: t.ContainerValue,
        transformers: Mapping[str, Callable[[t.ContainerValue], str]] | None = None,
    ) -> str:
        """Normalize attribute value based on attribute type."""
        if transformers and attr_name in transformers:
            return transformers[attr_name](value)
        builtin_transformer = FlextTargetLdifRecordTransformer._get_builtin_transformer(
            attr_name
        )
        if builtin_transformer:
            return builtin_transformer(value)
        return str(value).strip()

    @staticmethod
    def add_required_attributes(
        record: t.StrMapping,
    ) -> Mapping[str, t.ContainerValue]:
        """Add required LDAP attributes to the record."""
        result: dict[str, t.ContainerValue] = dict(record)
        if "objectclass" not in result:
            result["objectclass"] = ["inetOrgPerson", "person"]
        if "cn" not in result:
            if "givenname" in result and "sn" in result:
                result["cn"] = f"{result['givenname']} {result['sn']}"
            elif "displayname" in result:
                result["cn"] = result["displayname"]
            elif "uid" in result:
                result["cn"] = result["uid"]
            else:
                result["cn"] = "Unknown User"
        if "sn" not in result and "cn" in result:
            cn_value = result["cn"]
            words: t.StrSequence = cn_value.split() if isinstance(cn_value, str) else []
            result["sn"] = words[-1] if words else "Unknown"
        return result

    def transform_record(self, record: Mapping[str, t.ContainerValue]) -> t.StrMapping:
        """Transform a Singer record to LDAP-compatible format."""
        transformed: dict[str, str] = {}
        for field, value in record.items():
            if value is None:
                continue
            if field in self.attribute_mapping:
                attr_name = self.attribute_mapping[field]
            else:
                attr_name = field.lower().replace("_", "")
            transformed_value = (
                FlextTargetLdifRecordTransformer.normalize_attribute_value(
                    attr_name, value, self.custom_transformers
                )
            )
            if transformed_value:
                transformed[attr_name] = transformed_value
        return transformed
