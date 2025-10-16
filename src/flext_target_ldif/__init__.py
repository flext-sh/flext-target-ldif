"""Module docstring."""

from __future__ import annotations

from flext_target_ldif.cli import main as cli_main
from flext_target_ldif.config import FlextTargetLdifConfig
from flext_target_ldif.models import FlextTargetLdifModels
from flext_target_ldif.protocols import FlextTargetLdifProtocols
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
from flext_target_ldif.utilities import FlextTargetLdifUtilities
from flext_target_ldif.validation import (
    ValidationError,
    sanitize_attribute_name,
    validate_attribute_name,
    validate_attribute_value,
    validate_dn_component,
    validate_record,
    validate_schema,
)
from flext_target_ldif.version import VERSION, FlextTargetLdifVersion
from flext_target_ldif.writer import LdifWriter, LdifWriter as _LdifWriter

PROJECT_VERSION: Final[FlextTargetLdifVersion] = VERSION

__version__: str = VERSION.version
__version_info__: tuple[int | str, ...] = VERSION.version_info

FlextLdifTarget = _TargetLDIF
_FlextTargetLdifConfig = FlextTargetLdifConfig
FlextTargetLDIF = _TargetLDIF
FlextTargetLDIFConfig = _FlextTargetLdifConfig
LDIFTarget = _TargetLDIF
TargetLDIFConfig = _FlextTargetLdifConfig

__all__ = [
    "FlextLdifTarget",
    "FlextLogger",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoTargetAbstractions",
    "FlextMeltanoTypes",
    "FlextResult",
    "FlextTargetLDIF",
    "FlextTargetLDIFConfig",
    "FlextTargetLdifConfig",
    "FlextTargetLdifError",
    "FlextTargetLdifErrorDetails",
    "FlextTargetLdifFileError",
    "FlextTargetLdifInfrastructureError",
    "FlextTargetLdifModels",
    "FlextTargetLdifProtocols",
    "FlextTargetLdifSchemaError",
    "FlextTargetLdifTransformationError",
    "FlextTargetLdifUtilities",
    "LDIFSink",
    "LDIFTarget",
    "LdifWriter",
    "RecordTransformer",
    "StreamDefinition",
    "TargetLDIF",
    "TargetLDIFConfig",
    "ValidationError",
    "_LDIFSink",
    "_LdifWriter",
    "__version__",
    "__version_info__",
    "cli_main",
    "normalize_attribute_value",
    "sanitize_attribute_name",
    "transform_boolean",
    "transform_email",
    "transform_name",
    "transform_phone",
    "transform_timestamp",
    "validate_attribute_name",
    "validate_attribute_value",
    "validate_dn_component",
    "validate_record",
    "validate_schema",
]
