"""FLEXT Target LDIF Types - Domain-specific Singer LDIF target type definitions.

This module provides FLEXT Target LDIF-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes
from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes

# =============================================================================
# FLEXT TARGET LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer LDIF target operations
# =============================================================================


# FLEXT Target LDIF domain TypeVars
class FlextTargetLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """FLEXT Target LDIF-specific type definitions extending t.

    Domain-specific type system for Singer protocol LDIF file export operations.
    Contains ONLY complex Singer target and LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER PROTOCOL TYPES - Singer target implementation types
    # =========================================================================

    class TargetLdif:
        """Singer protocol complex types."""

        type SingerMessage = dict[
            str,
            FlextTypes.JsonValue | dict[str, FlextTypes.ContainerValue],
        ]
        type SingerSchema = dict[
            str,
            FlextTypes.JsonValue | list[dict[str, FlextTypes.ContainerValue]],
        ]
        type SingerRecord = dict[
            str,
            FlextTypes.JsonValue | dict[str, FlextTypes.ContainerValue],
        ]
        type SingerState = dict[
            str,
            FlextTypes.JsonValue | dict[str, FlextTypes.JsonValue],
        ]
        type StreamConfiguration = dict[
            str,
            str | bool | dict[str, FlextTypes.JsonValue],
        ]
        type TargetConfiguration = dict[
            str,
            FlextTypes.ContainerValue | dict[str, FlextTypes.ContainerValue],
        ]
        type MessageProcessing = dict[str, int | str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # LDIF EXPORT TYPES - LDIF file generation and export types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type Attributes = dict[
            str,
            str | list[str] | bytes | dict[str, FlextTypes.ContainerValue],
        ]
        type LdifRecord = dict[
            str,
            FlextTypes.JsonValue | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type LdifFileConfig = dict[
            str,
            str | int | bool | dict[str, FlextTypes.JsonValue],
        ]
        type LdifFormatting = dict[
            str,
            str | int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type LdifValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type ExportResult = dict[
            str,
            int | str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]

    # =========================================================================
    # FILE PROCESSING TYPES - File I/O and processing types
    # =========================================================================

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type StreamWriter = dict[
            str,
            str | bool | int | dict[str, FlextTypes.ContainerValue],
        ]
        type FileOutput = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type CompressionConfig = dict[
            str,
            str | bool | int | dict[str, FlextTypes.ContainerValue],
        ]
        type FileValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type IOMetrics = dict[str, int | float | dict[str, FlextTypes.ContainerValue]]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Singer to LDIF transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AttributeMapping = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type SchemaTransformation = dict[
            str,
            FlextTypes.JsonValue | dict[str, FlextTypes.ContainerValue],
        ]
        type RecordTransformation = dict[
            str,
            FlextTypes.JsonValue | dict[str, FlextTypes.ContainerValue],
        ]
        type DataNormalization = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type TransformationRules = dict[
            str,
            str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]

    # =========================================================================
    # VALIDATION TYPES - LDIF format and Singer compliance validation types
    # =========================================================================

    class TargetLdifValidation:
        """Validation complex types."""

        type LdifFormatValidation = dict[
            str,
            bool | str | dict[str, FlextTypes.JsonValue],
        ]
        type SingerCompliance = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type SchemaValidation = dict[
            str,
            bool | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type RecordValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type FormatCompliance = dict[
            str,
            bool | str | list[str] | dict[str, FlextTypes.ContainerValue],
        ]
        type ValidationRules = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # TARGET CONFIGURATION TYPES - Singer target configuration types
    # =========================================================================

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = dict[
            str,
            FlextTypes.ContainerValue | dict[str, FlextTypes.ContainerValue],
        ]
        type LdifTargetConfig = dict[
            str,
            str | int | bool | dict[str, FlextTypes.JsonValue],
        ]
        type OutputConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StreamMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type BatchConfiguration = dict[
            str,
            int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type ErrorHandling = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # PERFORMANCE TYPES - Performance optimization and monitoring types
    # =========================================================================

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = dict[
            str,
            int | float | dict[str, FlextTypes.ContainerValue],
        ]
        type OptimizationConfig = dict[
            str,
            int | bool | dict[str, FlextTypes.JsonValue],
        ]
        type BufferConfiguration = dict[
            str,
            int | str | dict[str, FlextTypes.ContainerValue],
        ]
        type StreamingConfig = dict[str, int | bool | dict[str, FlextTypes.JsonValue]]
        type MemoryManagement = dict[
            str,
            int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type IOOptimization = dict[
            str,
            int | bool | str | dict[str, FlextTypes.ContainerValue],
        ]

    # =========================================================================
    # FLEXT TARGET LDIF PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """FLEXT Target LDIF-specific project types.

        Adds FLEXT Target LDIF Singer target-specific project types.
        Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        # FLEXT Target LDIF-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from t
            "library",
            "application",
            "service",
            # FLEXT Target LDIF-specific types
            "target-ldif",
            "singer-target",
            "ldif-export",
            "singer-ldif-target",
            "ldif-file-target",
            "singer-protocol-target",
            "data-export-target",
            "ldif-generator",
            "singer-to-ldif",
            "ldif-export-service",
            "target-ldif-singer",
            "ldif-file-export",
            "singer-ldif-export",
            "ldif-data-target",
            "export-target-ldif",
            "singer-export-target",
            "ldif-streaming-target",
            "ldif-batch-export",
            "singer-file-target",
        ]

        # Error type literal - references ErrorType StrEnum from constants
        type ErrorTypeLiteral = Literal[
            "FORMAT_VALIDATION",
            "FILE_IO",
            "TRANSFORMATION",
            "SINGER_PROTOCOL",
            "CONFIGURATION",
            "DISK_SPACE",
            "PERMISSION",
            "ENCODING",
        ]

        # FLEXT Target LDIF-specific project configurations
        type FlextTargetLdifSettings = dict[str, FlextTypes.ContainerValue]
        type SingerTargetConfig = dict[
            str,
            str | int | bool | dict[str, FlextTypes.ContainerValue],
        ]
        type LdifExportConfig = dict[str, FlextTypes.ContainerValue]
        type TargetPipelineConfig = dict[
            str,
            bool | str | dict[str, FlextTypes.ContainerValue],
        ]


# Alias for simplified usage
t = FlextTargetLdifTypes

# Namespace composition via class inheritance
# TargetLdif namespace provides access to nested classes through inheritance
# Access patterns:
# - t.TargetLdif.* for Target LDIF-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

# =============================================================================
# PUBLIC API EXPORTS - FLEXT Target LDIF TypeVars and types
# =============================================================================

__all__ = [
    "FlextTargetLdifTypes",
    "t",
]
