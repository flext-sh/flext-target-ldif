"""Enterprise Singer Target for LDIF data export."""

"""
Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


import importlib.metadata

# flext-core imports
from flext_core import FlextExceptions, FlextResult, FlextModels, FlextLogger
from flext_core import FlextTypes

# === FLEXT-MELTANO INTEGRATION ===
# Re-export available flext-meltano facilities
from flext_meltano import (
    # Bridge integration
    FlextMeltanoBridge,
    # Configuration and validation
    FlextMeltanoConfig,
    # Enterprise services
    FlextMeltanoTargetService,
    # Types and protocols
    FlextSingerTypes,
    FlextTargetAbstractions,
    FlextTargetPlugin,
    # Stream and configuration
    StreamDefinition,
    # Service protocols
    TargetServiceProtocol,
)

# === DIRECT MODULE IMPORTS ===
# Import directly from implementation modules
from flext_target_ldif.sinks import LDIFSink
from flext_target_ldif.target import TargetLDIF
from flext_target_ldif.writer import LdifWriter
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
from flext_target_ldif.cli import main as cli_main

# === BACKWARD COMPATIBILITY IMPORTS ===
# Direct imports for existing code compatibility
from flext_target_ldif.config import FlextTargetLdifConfig as _FlextTargetLdifConfig
from flext_target_ldif.sinks import LDIFSink as _LDIFSink
from flext_target_ldif.target import TargetLDIF as _TargetLDIF
from flext_target_ldif.writer import LdifWriter as _LdifWriter

# === BACKWARD COMPATIBILITY ALIASES ===
# Ensure all existing code continues to work
FlextLDIFTarget = _TargetLDIF
FlextLDIFTargetConfig = _FlextTargetLdifConfig
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
    # === FLEXT-MELTANO RE-EXPORTS ===
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoTargetService",
    "FlextSingerTypes",
    "FlextTargetAbstractions",
    "FlextTargetPlugin",
    "StreamDefinition",
    "TargetServiceProtocol",
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextExceptions",
    "FlextResult",
    "FlextModels",
    "FlextLogger",
    # === DIRECT MODULE IMPORTS ===
    # Core components
    "FlextTargetLdifConfig",
    "LDIFSink",
    "LdifWriter",
    "TargetLDIF",
    # Models (Validation + Transformation)
    "RecordTransformer",
    "ValidationError",
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
    # Exceptions
    "FlextTargetLdifError",
    "FlextTargetLdifErrorDetails",
    "FlextTargetLdifFileError",
    "FlextTargetLdifInfrastructureError",
    "FlextTargetLdifSchemaError",
    "FlextTargetLdifTransformationError",
    "FlextTargetLdifWriterError",
    # CLI
    "cli_main",
    # === BACKWARD COMPATIBILITY ALIASES ===
    "FlextLDIFTarget",
    "FlextLDIFTargetConfig",
    "FlextTargetLDIF",
    "FlextTargetLDIFConfig",
    "LDIFTarget",
    "TargetLDIFConfig",
    # === METADATA ===
    "__version__",
    "__version_info__",
]
