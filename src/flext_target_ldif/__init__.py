"""Enterprise Singer Target for LDIF data export.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

import importlib.metadata

from flext_core import (
    FlextExceptions,
    FlextLogger,
    FlextModels,
    FlextResult,
    FlextTypes,
)
from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoConfig,
    FlextMeltanoTargetService,
    FlextSingerTypes,
    FlextTargetAbstractions,
    FlextTargetPlugin,
    StreamDefinition,
    TargetServiceProtocol,
)
from flext_target_ldif.cli import main as cli_main
from flext_target_ldif.config import FlextTargetLdifConfig
from flext_target_ldif.exceptions import (
    FlextTargetLdifError,
    FlextTargetLdifErrorDetails,
    FlextTargetLdifFileError,
    FlextTargetLdifInfrastructureError,
    FlextTargetLdifSchemaError,
    FlextTargetLdifTransformationError,
    FlextTargetLdifWriterError,
)
from flext_target_ldif.sinks import LDIFSink, LDIFSink as _LDIFSink
from flext_target_ldif.target import TargetLDIF, TargetLDIF as _TargetLDIF
from flext_target_ldif.transformers import RecordTransformer
from flext_target_ldif.validation import (
    ValidationError,
    normalize_attribute_value,
    sanitize_attribute_name,
    transform_boolean,
    transform_email,
    transform_name,
    transform_phone,
    transform_timestamp,
    validate_attribute_name,
    validate_attribute_value,
    validate_dn_component,
    validate_record,
    validate_schema,
)
from flext_target_ldif.writer import LdifWriter, LdifWriter as _LdifWriter

# === FLEXT-MELTANO INTEGRATION ===
# Re-export available flext-meltano facilities


# === BACKWARD COMPATIBILITY IMPORTS ===
# Direct imports for existing code compatibility

# === DIRECT MODULE IMPORTS ===
# Import directly from implementation modules

# === BACKWARD COMPATIBILITY ALIASES ===
# Ensure all existing code continues to work
FlextLdifTarget = _TargetLDIF
_FlextTargetLdifConfig = FlextTargetLdifConfig
FlextTargetLDIF = _TargetLDIF
FlextTargetLDIFConfig = _FlextTargetLdifConfig
LDIFTarget = _TargetLDIF
TargetLDIFConfig = _FlextTargetLdifConfig

# FlextTargetLdifConfig already imported from target_config module above

# Version following semantic versioning
try:
    __version__ = importlib.metadata.version("flext-target-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0-enterprise"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# Complete public API exports with PEP8 consolidation and backward compatibility
__all__: FlextTypes.Core.StringList = [
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextExceptions",
    # === BACKWARD COMPATIBILITY ALIASES ===
    "FlextLdifTarget",
    "FlextLdifTargetConfig",
    "FlextLogger",
    # === FLEXT-MELTANO RE-EXPORTS ===
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoTargetService",
    "FlextModels",
    "FlextResult",
    "FlextSingerTypes",
    "FlextTargetAbstractions",
    "FlextTargetLDIF",
    "FlextTargetLDIFConfig",
    # === DIRECT MODULE IMPORTS ===
    # Core components
    "FlextTargetLdifConfig",
    # Exceptions
    "FlextTargetLdifError",
    "FlextTargetLdifErrorDetails",
    "FlextTargetLdifFileError",
    "FlextTargetLdifInfrastructureError",
    "FlextTargetLdifSchemaError",
    "FlextTargetLdifTransformationError",
    "FlextTargetLdifWriterError",
    "FlextTargetPlugin",
    "LDIFSink",
    "LDIFTarget",
    "LdifWriter",
    # Models (Validation + Transformation)
    "RecordTransformer",
    "StreamDefinition",
    "TargetLDIF",
    "TargetLDIFConfig",
    "TargetServiceProtocol",
    "ValidationError",
    "_LDIFSink",
    "_LdifWriter",
    # === METADATA ===
    "__version__",
    "__version_info__",
    # CLI
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
