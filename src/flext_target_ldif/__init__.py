"""Module docstring."""

from __future__ import annotations

from typing import Final

from flext_target_ldif.__version__ import VERSION, FlextTargetLdifVersion
from flext_target_ldif.cli import main as cli_main
from flext_target_ldif.models import FlextTargetLdifModels, m, m_target_ldif
from flext_target_ldif.protocols import FlextTargetLdifProtocols
from flext_target_ldif.settings import FlextTargetLdifSettings
from flext_target_ldif.sinks import LDIFSink, LDIFSink as _LDIFSink
from flext_target_ldif.target import TargetLDIF, TargetLDIF as _TargetLDIF
from flext_target_ldif.transformers import (
    RecordTransformer,
    normalize_attribute_value,
    transform_boolean,
    transform_email,
    transform_name,
    transform_phone,
    transform_timestamp,
)
from flext_target_ldif.utilities import FlextTargetLdifUtilities as u
from flext_target_ldif.validation import (
    ValidationError,
    sanitize_attribute_name,
    validate_attribute_name,
    validate_attribute_value,
    validate_dn_component,
    validate_record,
    validate_schema,
)
from flext_target_ldif.writer import LdifWriter, LdifWriter as _LdifWriter

PROJECT_VERSION: Final[type[FlextTargetLdifVersion]] = VERSION

__version__: str = VERSION.version
__version_info__: tuple[int | str, ...] = VERSION.version_info

FlextLdifTarget = _TargetLDIF
_FlextTargetLdifSettings = FlextTargetLdifSettings
FlextTargetLDIF = _TargetLDIF
FlextTargetLDIFSettings = _FlextTargetLdifSettings
LDIFTarget = _TargetLDIF
TargetLDIFConfig = _FlextTargetLdifSettings

__all__ = [
    "FlextLdifTarget",
    "FlextTargetLDIF",
    "FlextTargetLDIFSettings",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifSettings",
    "LDIFSink",
    "LDIFTarget",
    "LdifWriter",
    "RecordTransformer",
    "TargetLDIF",
    "TargetLDIFConfig",
    "ValidationError",
    "_LDIFSink",
    "_LdifWriter",
    "__version__",
    "__version_info__",
    "cli_main",
    "m",
    "m_target_ldif",
    "normalize_attribute_value",
    "sanitize_attribute_name",
    "transform_boolean",
    "transform_email",
    "transform_name",
    "transform_phone",
    "transform_timestamp",
    "u",
    "validate_attribute_name",
    "validate_attribute_value",
    "validate_dn_component",
    "validate_record",
    "validate_schema",
]
