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

from flext import FlextTypes

# =============================================================================
# FLEXT TARGET LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer LDIF target operations
# =============================================================================


# FLEXT Target LDIF domain TypeVars
class FlextTargetLdifTypes(FlextTypes):
    """FLEXT Target LDIF-specific type definitions extending t.

    Domain-specific type system for Singer protocol LDIF file export operations.
    Contains ONLY complex Singer target and LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER PROTOCOL TYPES - Singer target implementation types
    # =========================================================================

    class SingerProtocol:
        """Singer protocol complex types."""

        type SingerMessage = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type SingerSchema = dict[str, FlextTypes.JsonValue | list[dict[str, object]]]
        type SingerRecord = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type SingerState = dict[
            str, FlextTypes.JsonValue | dict[str, FlextTypes.JsonValue],
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.JsonValue],
        ]
        type TargetConfiguration = dict[str, object | dict[str, object]]
        type MessageProcessing = dict[str, int | str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # LDIF EXPORT TYPES - LDIF file generation and export types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type Attributes = dict[str, str | list[str] | bytes | dict[str, object]]
        type LdifRecord = dict[
            str,
            FlextTypes.JsonValue | list[str] | dict[str, object],
        ]
        type LdifFileConfig = dict[
            str, str | int | bool | dict[str, FlextTypes.JsonValue],
        ]
        type LdifFormatting = dict[str, str | int | bool | dict[str, object]]
        type LdifValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type ExportResult = dict[str, int | str | list[str] | dict[str, object]]

    # =========================================================================
    # FILE PROCESSING TYPES - File I/O and processing types
    # =========================================================================

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type StreamWriter = dict[str, str | bool | int | dict[str, object]]
        type FileOutput = dict[str, str | list[str] | dict[str, FlextTypes.JsonValue]]
        type CompressionConfig = dict[str, str | bool | int | dict[str, object]]
        type FileValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type IOMetrics = dict[str, int | float | dict[str, object]]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Singer to LDIF transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AttributeMapping = dict[str, str | list[str] | dict[str, object]]
        type SchemaTransformation = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type RecordTransformation = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type DataNormalization = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type TransformationRules = dict[str, str | list[str] | dict[str, object]]

    # =========================================================================
    # VALIDATION TYPES - LDIF format and Singer compliance validation types
    # =========================================================================

    class TargetLdifValidation:
        """Validation complex types."""

        type LdifFormatValidation = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue],
        ]
        type SingerCompliance = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type SchemaValidation = dict[str, bool | list[str] | dict[str, object]]
        type RecordValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type FormatCompliance = dict[str, bool | str | list[str] | dict[str, object]]
        type ValidationRules = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # TARGET CONFIGURATION TYPES - Singer target configuration types
    # =========================================================================

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = dict[str, object | dict[str, object]]
        type LdifTargetConfig = dict[
            str, str | int | bool | dict[str, FlextTypes.JsonValue],
        ]
        type OutputConfiguration = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StreamMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type BatchConfiguration = dict[str, int | bool | dict[str, object]]
        type ErrorHandling = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # PERFORMANCE TYPES - Performance optimization and monitoring types
    # =========================================================================

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = dict[str, int | float | dict[str, object]]
        type OptimizationConfig = dict[
            str, int | bool | dict[str, FlextTypes.JsonValue],
        ]
        type BufferConfiguration = dict[str, int | str | dict[str, object]]
        type StreamingConfig = dict[str, int | bool | dict[str, FlextTypes.JsonValue]]
        type MemoryManagement = dict[str, int | bool | dict[str, object]]
        type IOOptimization = dict[str, int | bool | str | dict[str, object]]

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

        # FLEXT Target LDIF-specific project configurations
        type FlextTargetLdifSettings = dict[str, object]
        type SingerTargetConfig = dict[str, str | int | bool | dict[str, object]]
        type LdifExportConfig = dict[str, object]
        type TargetPipelineConfig = dict[str, bool | str | dict[str, object]]

    class TargetLdif:
        """Target LDIF types namespace for cross-project access.

        Provides organized access to all Target LDIF types for other FLEXT projects.
        Usage: Other projects can reference `t.TargetLdif.SingerProtocol.*`, `t.TargetLdif.Project.*`, etc.
        This enables consistent namespace patterns for cross-project type access.

        Examples:
            from flext_target_ldif.typings import t
            config: t.TargetLdif.Project.FlextTargetLdifSettings = ...
            message: t.TargetLdif.SingerProtocol.SingerMessage = ...

        Note: Namespace composition via inheritance - no aliases needed.
        Access parent namespaces directly through inheritance.

        """


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
