"""FLEXT Target LDIF Types - Domain-specific Singer LDIF target type definitions.

This module provides FLEXT Target LDIF-specific type definitions extending FlextCore.Types.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextCore.Types properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextCore

# =============================================================================
# FLEXT TARGET LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer LDIF target operations
# =============================================================================


# FLEXT Target LDIF domain TypeVars
class FlextTargetLdifTypes(FlextCore.Types):
    """FLEXT Target LDIF-specific type definitions extending FlextCore.Types.

    Domain-specific type system for Singer protocol LDIF file export operations.
    Contains ONLY complex Singer target and LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER PROTOCOL TYPES - Singer target implementation types
    # =========================================================================

    class SingerProtocol:
        """Singer protocol complex types."""

        type SingerMessage = dict[str, FlextCore.Types.JsonValue | FlextCore.Types.Dict]
        type SingerSchema = dict[
            str, FlextCore.Types.JsonValue | list[FlextCore.Types.Dict]
        ]
        type SingerRecord = dict[str, FlextCore.Types.JsonValue | FlextCore.Types.Dict]
        type SingerState = dict[
            str, FlextCore.Types.JsonValue | dict[str, FlextCore.Types.JsonValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type TargetConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type MessageProcessing = dict[
            str, int | str | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # LDIF EXPORT TYPES - LDIF file generation and export types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type LdifAttributes = dict[
            str, str | FlextCore.Types.StringList | bytes | FlextCore.Types.Dict
        ]
        type LdifRecord = dict[
            str,
            FlextCore.Types.JsonValue
            | FlextCore.Types.StringList
            | FlextCore.Types.Dict,
        ]
        type LdifFileConfig = dict[
            str, str | int | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type LdifFormatting = dict[str, str | int | bool | FlextCore.Types.Dict]
        type LdifValidation = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type ExportResult = dict[
            str, int | str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]

    # =========================================================================
    # FILE PROCESSING TYPES - File I/O and processing types
    # =========================================================================

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]
        type StreamWriter = dict[str, str | bool | int | FlextCore.Types.Dict]
        type FileOutput = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type CompressionConfig = dict[str, str | bool | int | FlextCore.Types.Dict]
        type FileValidation = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type IOMetrics = dict[str, int | float | FlextCore.Types.Dict]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Singer to LDIF transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type AttributeMapping = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type SchemaTransformation = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.Dict
        ]
        type RecordTransformation = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.Dict
        ]
        type DataNormalization = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type TransformationRules = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]

    # =========================================================================
    # VALIDATION TYPES - LDIF format and Singer compliance validation types
    # =========================================================================

    class Validation:
        """Validation complex types."""

        type LdifFormatValidation = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type SingerCompliance = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type SchemaValidation = dict[
            str, bool | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type RecordValidation = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type FormatCompliance = dict[
            str, bool | str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type ValidationRules = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # TARGET CONFIGURATION TYPES - Singer target configuration types
    # =========================================================================

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type LdifTargetConfig = dict[
            str, str | int | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type OutputConfiguration = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type StreamMapping = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type BatchConfiguration = dict[str, int | bool | FlextCore.Types.Dict]
        type ErrorHandling = dict[
            str, str | bool | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # PERFORMANCE TYPES - Performance optimization and monitoring types
    # =========================================================================

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = dict[str, int | float | FlextCore.Types.Dict]
        type OptimizationConfig = dict[
            str, int | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type BufferConfiguration = dict[str, int | str | FlextCore.Types.Dict]
        type StreamingConfig = dict[
            str, int | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type MemoryManagement = dict[str, int | bool | FlextCore.Types.Dict]
        type IOOptimization = dict[str, int | bool | str | FlextCore.Types.Dict]

    # =========================================================================
    # FLEXT TARGET LDIF PROJECT TYPES - Domain-specific project types extending FlextCore.Types
    # =========================================================================

    class Project(FlextCore.Types.Project):
        """FLEXT Target LDIF-specific project types extending FlextCore.Types.Project.

        Adds FLEXT Target LDIF Singer target-specific project types while inheriting
        generic types from FlextCore.Types. Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        # FLEXT Target LDIF-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextCore.Types.Project
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

        # FLEXT Target LDIF-specific project configurations
        type FlextTargetLdifConfig = dict[str, FlextCore.Types.ConfigValue | object]
        type SingerTargetConfig = dict[str, str | int | bool | FlextCore.Types.Dict]
        type LdifExportConfig = dict[str, FlextCore.Types.ConfigValue | object]
        type TargetPipelineConfig = dict[str, bool | str | FlextCore.Types.Dict]


# =============================================================================
# PUBLIC API EXPORTS - FLEXT Target LDIF TypeVars and types
# =============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextTargetLdifTypes",
]
