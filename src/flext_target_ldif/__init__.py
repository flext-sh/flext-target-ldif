"""Module docstring."""

from __future__ import annotations

from flext_target_ldif.__version__ import __version__, __version_info__
from flext_target_ldif.cli import main as cli_main
from flext_target_ldif.models import FlextTargetLdifModels, m
from flext_target_ldif.protocols import FlextTargetLdifProtocols
from flext_target_ldif.settings import (
    FlextTargetLDIFSettings,
    FlextTargetLdifSettings,
    TargetLDIFConfig,
)
from flext_target_ldif.sinks import LDIFSink, LDIFSink as _LDIFSink
from flext_target_ldif.target import (
    TargetLDIF,
    TargetLDIF as FlextLdifTarget,
    TargetLDIF as FlextTargetLDIF,
    TargetLDIF as LDIFTarget,
)
from flext_target_ldif.transformers import (
    RecordTransformer,
    normalize_attribute_value,
    transform_boolean,
    transform_email,
    transform_name,
    transform_phone,
    transform_timestamp,
)
from flext_target_ldif.typings import t
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
    "normalize_attribute_value",
    "sanitize_attribute_name",
    "t",
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
