"""FLEXT Target LDIF Types - Domain-specific Singer LDIF target type definitions.

This module provides FLEXT Target LDIF-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# FLEXT TARGET LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer LDIF target operations
# =============================================================================


# FLEXT Target LDIF domain TypeVars
class FlextTargetLdifTypes(FlextTypes):
    """FLEXT Target LDIF-specific type definitions extending FlextTypes.

    Domain-specific type system for Singer protocol LDIF file export operations.
    Contains ONLY complex Singer target and LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER PROTOCOL TYPES - Singer target implementation types
    # =========================================================================

    class SingerProtocol:
        """Singer protocol complex types."""

        type SingerMessage = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type SingerSchema = dict[str, FlextTypes.JsonValue | list[FlextTypes.Dict]]
        type SingerRecord = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type SingerState = dict[
            str, FlextTypes.JsonValue | dict[str, FlextTypes.JsonValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.JsonValue]
        ]
        type TargetConfiguration = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type MessageProcessing = dict[str, int | str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # LDIF EXPORT TYPES - LDIF file generation and export types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type LdifAttributes = dict[
            str, str | FlextTypes.StringList | bytes | FlextTypes.Dict
        ]
        type LdifRecord = dict[
            str,
            FlextTypes.JsonValue | FlextTypes.StringList | FlextTypes.Dict,
        ]
        type LdifFileConfig = dict[
            str, str | int | bool | dict[str, FlextTypes.JsonValue]
        ]
        type LdifFormatting = dict[str, str | int | bool | FlextTypes.Dict]
        type LdifValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type ExportResult = dict[
            str, int | str | FlextTypes.StringList | FlextTypes.Dict
        ]

    # =========================================================================
    # FILE PROCESSING TYPES - File I/O and processing types
    # =========================================================================

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type StreamWriter = dict[str, str | bool | int | FlextTypes.Dict]
        type FileOutput = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type CompressionConfig = dict[str, str | bool | int | FlextTypes.Dict]
        type FileValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type IOMetrics = dict[str, int | float | FlextTypes.Dict]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Singer to LDIF transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AttributeMapping = dict[str, str | FlextTypes.StringList | FlextTypes.Dict]
        type SchemaTransformation = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type RecordTransformation = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type DataNormalization = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type TransformationRules = dict[
            str, str | FlextTypes.StringList | FlextTypes.Dict
        ]

    # =========================================================================
    # VALIDATION TYPES - LDIF format and Singer compliance validation types
    # =========================================================================

    class Validation:
        """Validation complex types."""

        type LdifFormatValidation = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue]
        ]
        type SingerCompliance = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type SchemaValidation = dict[
            str, bool | FlextTypes.StringList | FlextTypes.Dict
        ]
        type RecordValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type FormatCompliance = dict[
            str, bool | str | FlextTypes.StringList | FlextTypes.Dict
        ]
        type ValidationRules = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # TARGET CONFIGURATION TYPES - Singer target configuration types
    # =========================================================================

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type LdifTargetConfig = dict[
            str, str | int | bool | dict[str, FlextTypes.JsonValue]
        ]
        type OutputConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StreamMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type BatchConfiguration = dict[str, int | bool | FlextTypes.Dict]
        type ErrorHandling = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # PERFORMANCE TYPES - Performance optimization and monitoring types
    # =========================================================================

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = dict[str, int | float | FlextTypes.Dict]
        type OptimizationConfig = dict[
            str, int | bool | dict[str, FlextTypes.JsonValue]
        ]
        type BufferConfiguration = dict[str, int | str | FlextTypes.Dict]
        type StreamingConfig = dict[str, int | bool | dict[str, FlextTypes.JsonValue]]
        type MemoryManagement = dict[str, int | bool | FlextTypes.Dict]
        type IOOptimization = dict[str, int | bool | str | FlextTypes.Dict]

    # =========================================================================
    # FLEXT TARGET LDIF PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """FLEXT Target LDIF-specific project types extending FlextTypes.Project.

        Adds FLEXT Target LDIF Singer target-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        # FLEXT Target LDIF-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
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
        type FlextTargetLdifConfig = dict[str, FlextTypes.ConfigValue | object]
        type SingerTargetConfig = dict[str, str | int | bool | FlextTypes.Dict]
        type LdifExportConfig = dict[str, FlextTypes.ConfigValue | object]
        type TargetPipelineConfig = dict[str, bool | str | FlextTypes.Dict]


# =============================================================================
# PUBLIC API EXPORTS - FLEXT Target LDIF TypeVars and types
# =============================================================================

__all__: FlextTypes.StringList = [
    "FlextTargetLdifTypes",
]
