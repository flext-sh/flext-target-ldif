"""Singer target utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
import re
from collections.abc import Callable, Mapping, MutableMapping, MutableSequence
from datetime import datetime
from pathlib import Path
from typing import ClassVar, override

from flext_core import r
from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_target_ldif import c, t


class FlextTargetLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Single unified utilities class for Singer target LDIF operations."""

    DEFAULT_BATCH_SIZE: ClassVar[int] = c.DEFAULT_SIZE
    DEFAULT_TIMEOUT: ClassVar[int] = c.DEFAULT_TIMEOUT_SECONDS
    MAX_RETRIES: ClassVar[int] = c.BACKUP_COUNT
    LDIF_LINE_WRAP_LENGTH: ClassVar[int] = c.LDIF_LINE_WRAP_LENGTH
    ASCII_SPACE: ClassVar[int] = c.ASCII_SPACE
    ASCII_TILDE: ClassVar[int] = c.ASCII_TILDE

    @override
    def __init__(self) -> None:
        """Initialize LDIF target utilities."""
        super().__init__()

    class TargetLdif:
        """Singer protocol utilities for target operations."""

        class LdifDataProcessing:
            """LDIF-specific data processing utilities."""

            @staticmethod
            def build_ldif_dn(
                record: Mapping[str, t.ContainerValue],
                dn_template: str,
                base_dn: str | None = None,
            ) -> r[str]:
                """Build LDIF Distinguished Name from record data.

                Args:
                record: Record data
                dn_template: DN template with placeholders
                base_dn: Optional base DN to append

                Returns:
                r[str]: Built DN or error

                """
                if not record or not dn_template:
                    return r[str].fail("Record and DN template are required")
                try:
                    dn_rdn = dn_template
                    for key, value in record.items():
                        placeholder = f"{{{key}}}"
                        if placeholder in dn_rdn:
                            dn_rdn = dn_rdn.replace(placeholder, str(value))
                    if "{" in dn_rdn and "}" in dn_rdn:
                        return r[str].fail(f"Unresolved placeholders in DN: {dn_rdn}")
                    full_dn = f"{dn_rdn},{base_dn}" if base_dn else dn_rdn
                    if not FlextTargetLdifUtilities.TargetLdif.LdifDataProcessing.split(
                        full_dn,
                    ):
                        return r[str].fail(f"Invalid DN format: {full_dn}")
                    return r[str].ok(full_dn)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"Error building DN: {e}")

            @staticmethod
            def convert_record_to_ldif_entry(
                record: Mapping[str, t.ContainerValue],
                dn: str,
                object_classes: t.StrSequence | None = None,
                attribute_mapping: t.StrMapping | None = None,
            ) -> r[str]:
                """Convert Singer record to LDIF entry format.

                Args:
                record: Singer record data
                dn: Distinguished Name for the entry
                object_classes: Object classes for the entry
                attribute_mapping: Optional mapping from record keys to LDIF attributes

                Returns:
                r[str]: LDIF entry or error

                """
                if not record or not dn:
                    return r[str].fail("Record and DN are required")
                try:
                    ldif_lines: MutableSequence[str] = []
                    mapping = attribute_mapping or {}
                    ldif_lines.append(f"dn: {dn}")
                    if object_classes:
                        ldif_lines.extend(f"objectClass: {oc}" for oc in object_classes)
                    for key, value in record.items():
                        ldif_attr = mapping.get(key, key)
                        if isinstance(value, list):
                            for item in value:
                                ldif_value = FlextTargetLdifUtilities.TargetLdif.LdifDataProcessing.format_ldif_value(
                                    str(item),
                                )
                                ldif_lines.append(f"{ldif_attr}: {ldif_value}")
                        else:
                            ldif_value = FlextTargetLdifUtilities.TargetLdif.LdifDataProcessing.format_ldif_value(
                                str(value),
                            )
                            ldif_lines.append(f"{ldif_attr}: {ldif_value}")
                    ldif_lines.append("")
                    return r[str].ok("\n".join(ldif_lines))
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"Error converting to LDIF entry: {e}")

            @staticmethod
            def format_ldif_value(value: str) -> str:
                """Format value for LDIF attribute.

                Args:
                value: Value to format

                Returns:
                str: Formatted LDIF value

                """
                if not value:
                    return ""
                if value.startswith((" ", ":", "<")) or any(
                    ord(ch) < FlextTargetLdifUtilities.ASCII_SPACE
                    or ord(ch) > FlextTargetLdifUtilities.ASCII_TILDE
                    for ch in value
                ):
                    encoded = base64.b64encode(value.encode("utf-8")).decode("ascii")
                    return f":: {encoded}"
                if len(value) > FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                    return FlextTargetLdifUtilities.TargetLdif.LdifDataProcessing.wrap_ldif_line(
                        value,
                    )
                return value

            @staticmethod
            def split(dn: str) -> bool:
                """Validate LDIF Distinguished Name format.

                Args:
                dn: Distinguished Name to validate

                Returns:
                bool: True if valid, False otherwise

                """
                if not dn:
                    return False
                dn_pattern = "^[a-zA-Z][\\w\\-]*\\s*=\\s*[^,]+(?:\\s*,\\s*[a-zA-Z][\\w\\-]*\\s*=\\s*[^,]+)*$"
                return bool(re.match(dn_pattern, dn.strip()))

            @staticmethod
            def validate_ldif_entry(entry: str) -> r[bool]:
                """Validate LDIF entry format.

                Args:
                entry: LDIF entry to validate

                Returns:
                r[bool]: Validation result

                """
                if not entry or not entry.strip():
                    return r[bool].fail("LDIF entry cannot be empty")
                lines = entry.strip().split("\n")
                if not lines:
                    return r[bool].fail("LDIF entry must have at least one line")
                first_line = lines[0].strip()
                if not first_line.startswith("dn:"):
                    return r[bool].fail("LDIF entry must start with DN")
                dn_value = first_line[3:].strip()
                if not dn_value:
                    return r[bool].fail("DN cannot be empty")
                if not FlextTargetLdifUtilities.TargetLdif.LdifDataProcessing.split(
                    dn_value,
                ):
                    return r[bool].fail(f"Invalid DN format: {dn_value}")
                return r[bool].ok(value=True)

            @staticmethod
            def wrap_ldif_line(value: str) -> str:
                """Wrap long LDIF lines according to RFC 2849.

                Args:
                value: Value to wrap

                Returns:
                str: Wrapped value

                """
                if len(value) <= FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                    return value
                lines: MutableSequence[str] = []
                remaining = value
                while remaining:
                    if len(remaining) <= FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH:
                        lines.append(remaining)
                        break
                    break_point = FlextTargetLdifUtilities.LDIF_LINE_WRAP_LENGTH
                    if " " in remaining[:break_point]:
                        break_point = remaining[:break_point].rfind(" ")
                    lines.append(remaining[:break_point])
                    remaining = " " + remaining[break_point:].lstrip()
                return "\n".join(lines)

        class FileUtilities:
            """File handling utilities for LDIF operations."""

            @staticmethod
            def append_to_ldif_file(file_path: str, entries: t.StrSequence) -> r[str]:
                """Append entries to existing LDIF file.

                Args:
                file_path: Path to LDIF file
                entries: List of LDIF entries to append

                Returns:
                r[str]: Success message or error

                """
                if not file_path or not entries:
                    return r[str].fail("File path and entries are required")
                try:
                    path = Path(file_path)
                    if not path.exists():
                        path.parent.mkdir(parents=True, exist_ok=True)
                    with Path(path).open("a", encoding="utf-8") as f:
                        for entry in entries:
                            f.write(entry)
                            if not entry.endswith("\n"):
                                f.write("\n")
                    return r[str].ok(f"Entries appended to LDIF file: {file_path}")
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"Error appending to LDIF file: {e}")

            @staticmethod
            def create_ldif_file(
                file_path: str,
                entries: t.StrSequence,
                *,
                overwrite: bool = False,
            ) -> r[str]:
                """Create LDIF file with entries.

                Args:
                file_path: Path to LDIF file
                entries: List of LDIF entries
                overwrite: Whether to overwrite existing file

                Returns:
                r[str]: Success message or error

                """
                if not file_path or not entries:
                    return r[str].fail("File path and entries are required")
                try:
                    path = Path(file_path)
                    if path.exists() and (not overwrite):
                        return r[str].fail(f"File already exists: {file_path}")
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with Path(path).open("w", encoding="utf-8") as f:
                        for entry in entries:
                            f.write(entry)
                            if not entry.endswith("\n"):
                                f.write("\n")
                    return r[str].ok(f"LDIF file created: {file_path}")
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"Error creating LDIF file: {e}")

            @staticmethod
            def validate_ldif_file_path(file_path: str) -> r[str]:
                """Validate LDIF file path.

                Args:
                file_path: Path to validate

                Returns:
                r[str]: Validated path or error

                """
                if not file_path or not file_path.strip():
                    return r[str].fail("File path cannot be empty")
                try:
                    path = Path(file_path)
                    if not path.name:
                        return r[str].fail("Invalid file path")
                    if path.suffix.lower() != ".ldif":
                        return r[str].fail("File must have .ldif extension")
                    if path.parent.exists() and (not path.parent.is_dir()):
                        return r[str].fail("Parent path is not a directory")
                    return r[str].ok(str(path.resolve()))
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"Invalid file path: {e}")

        class RecordTransformer:
            """Transform Singer records for LDIF output.

            Absorbed from transformers.py into namespace class.
            """

            @staticmethod
            def transform_timestamp(value: t.ContainerValue) -> str:
                """Transform timestamp values to LDAP timestamp format."""
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
                return "".join(ch for ch in phone_str if ch.isdigit() or ch in "+- ()")

            @staticmethod
            def transform_name(value: t.ContainerValue) -> str:
                """Transform name fields to ensure proper formatting."""
                name_str = str(value).strip()
                return " ".join(word.capitalize() for word in name_str.split())

            @staticmethod
            def get_builtin_transformer(
                attr_name: str,
            ) -> Callable[[t.ContainerValue], str] | None:
                """Get built-in transformer function for attribute name."""
                rt = FlextTargetLdifUtilities.TargetLdif.RecordTransformer
                attr_lower = attr_name.lower()
                if attr_lower in {"mail", "email"}:
                    return rt.transform_email
                if attr_lower in {"telephonenumber", "phone", "mobile"}:
                    return rt.transform_phone
                if attr_lower in {"givenname", "sn", "cn", "displayname"}:
                    return rt.transform_name
                if attr_lower in {"createtimestamp", "modifytimestamp"}:
                    return rt.transform_timestamp
                if attr_lower.endswith("boolean") or attr_lower.startswith("is"):
                    return rt.transform_boolean
                return None

            @staticmethod
            def normalize_attribute_value(
                attr_name: str,
                value: t.ContainerValue,
                transformers: Mapping[str, Callable[[t.ContainerValue], str]]
                | None = None,
            ) -> str:
                """Normalize attribute value based on attribute type."""
                rt = FlextTargetLdifUtilities.TargetLdif.RecordTransformer
                if transformers and attr_name in transformers:
                    return transformers[attr_name](value)
                builtin_transformer = rt.get_builtin_transformer(attr_name)
                if builtin_transformer:
                    return builtin_transformer(value)
                return str(value).strip()

            @staticmethod
            def add_required_attributes(
                record: t.StrMapping,
            ) -> Mapping[str, t.ContainerValue]:
                """Add required LDAP attributes to the record."""
                result: MutableMapping[str, t.ContainerValue] = dict(record)
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
                    words: t.StrSequence = (
                        cn_value.split() if isinstance(cn_value, str) else []
                    )
                    result["sn"] = words[-1] if words else "Unknown"
                return result

            def __init__(
                self,
                attribute_mapping: t.StrMapping | None = None,
                custom_transformers: Mapping[str, Callable[..., str]] | None = None,
            ) -> None:
                """Initialize the record transformer."""
                self.attribute_mapping = attribute_mapping or {}
                self.custom_transformers = custom_transformers or {}

            def transform_record(
                self,
                record: Mapping[str, t.ContainerValue],
            ) -> t.StrMapping:
                """Transform a Singer record to LDAP-compatible format."""
                rt = FlextTargetLdifUtilities.TargetLdif.RecordTransformer
                transformed: MutableMapping[str, str] = {}
                for field, value in record.items():
                    if field in self.attribute_mapping:
                        attr_name = self.attribute_mapping[field]
                    else:
                        attr_name = field.lower().replace("_", "")
                    transformed_value = rt.normalize_attribute_value(
                        attr_name,
                        value,
                        self.custom_transformers,
                    )
                    if transformed_value:
                        transformed[attr_name] = transformed_value
                return transformed


u = FlextTargetLdifUtilities

__all__ = ["FlextTargetLdifUtilities", "u"]
