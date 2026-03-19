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

from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes

from flext_target_ldif import c


class FlextTargetLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """FLEXT Target LDIF-specific type definitions extending t.

    Domain-specific type system for Singer protocol LDIF file export operations.
    Contains ONLY complex Singer target and LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TargetLdif:
        """Singer protocol complex types."""

        type SingerMessage = dict[
            str,
            t.ContainerValue | dict[str, t.ContainerValue],
        ]
        type SingerSchema = dict[
            str,
            t.ContainerValue | list[dict[str, t.ContainerValue]],
        ]
        type SingerRecord = dict[
            str,
            t.ContainerValue | dict[str, t.ContainerValue],
        ]
        type SingerState = dict[str, t.ContainerValue | dict[str, t.ContainerValue]]
        type StreamConfiguration = dict[str, str | bool | dict[str, t.ContainerValue]]
        type TargetConfiguration = dict[
            str,
            t.ContainerValue | dict[str, t.ContainerValue],
        ]
        type MessageProcessing = dict[str, int | str | dict[str, t.ContainerValue]]

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = dict[str, str | list[str] | dict[str, t.ContainerValue]]
        type Attributes = dict[
            str, str | list[str] | bytes | dict[str, t.ContainerValue]
        ]
        type LdifRecord = dict[
            str,
            t.ContainerValue | list[str] | dict[str, t.ContainerValue],
        ]
        type LdifFileConfig = dict[str, str | int | bool | dict[str, t.ContainerValue]]
        type LdifFormatting = dict[str, str | int | bool | dict[str, t.ContainerValue]]
        type LdifValidation = dict[str, bool | str | dict[str, t.ContainerValue]]
        type ExportResult = dict[
            str, int | str | list[str] | dict[str, t.ContainerValue]
        ]

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = dict[str, str | int | dict[str, t.ContainerValue]]
        type StreamWriter = dict[str, str | bool | int | dict[str, t.ContainerValue]]
        type FileOutput = dict[str, str | list[str] | dict[str, t.ContainerValue]]
        type CompressionConfig = dict[
            str, str | bool | int | dict[str, t.ContainerValue]
        ]
        type FileValidation = dict[str, bool | str | dict[str, t.ContainerValue]]
        type IOMetrics = dict[str, int | float | dict[str, t.ContainerValue]]

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = dict[str, str | dict[str, t.ContainerValue]]
        type AttributeMapping = dict[str, str | list[str] | dict[str, t.ContainerValue]]
        type SchemaTransformation = dict[
            str,
            t.ContainerValue | dict[str, t.ContainerValue],
        ]
        type RecordTransformation = dict[
            str,
            t.ContainerValue | dict[str, t.ContainerValue],
        ]
        type DataNormalization = dict[str, bool | str | dict[str, t.ContainerValue]]
        type TransformationRules = dict[
            str, str | list[str] | dict[str, t.ContainerValue]
        ]

    class TargetLdifValidation:
        """Validation complex types."""

        type LdifFormatValidation = dict[str, bool | str | dict[str, t.ContainerValue]]
        type SingerCompliance = dict[str, bool | str | dict[str, t.ContainerValue]]
        type SchemaValidation = dict[
            str, bool | list[str] | dict[str, t.ContainerValue]
        ]
        type RecordValidation = dict[str, bool | str | dict[str, t.ContainerValue]]
        type FormatCompliance = dict[
            str, bool | str | list[str] | dict[str, t.ContainerValue]
        ]
        type ValidationRules = dict[str, bool | str | dict[str, t.ContainerValue]]

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = dict[
            str,
            t.ContainerValue | dict[str, t.ContainerValue],
        ]
        type LdifTargetConfig = dict[
            str, str | int | bool | dict[str, t.ContainerValue]
        ]
        type OutputConfiguration = dict[str, str | dict[str, t.ContainerValue]]
        type StreamMapping = dict[str, str | dict[str, t.ContainerValue]]
        type BatchConfiguration = dict[str, int | bool | dict[str, t.ContainerValue]]
        type ErrorHandling = dict[str, str | bool | dict[str, t.ContainerValue]]

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = dict[str, int | float | dict[str, t.ContainerValue]]
        type OptimizationConfig = dict[str, int | bool | dict[str, t.ContainerValue]]
        type BufferConfiguration = dict[str, int | str | dict[str, t.ContainerValue]]
        type StreamingConfig = dict[str, int | bool | dict[str, t.ContainerValue]]
        type MemoryManagement = dict[str, int | bool | dict[str, t.ContainerValue]]
        type IOOptimization = dict[str, int | bool | str | dict[str, t.ContainerValue]]

    class Project:
        """FLEXT Target LDIF-specific project types.

        Adds FLEXT Target LDIF Singer target-specific project types.
        Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        type ProjectType = c.ProjectType
        type ErrorTypeLiteral = c.ErrorTypeLiteral
        type FlextTargetLdifSettings = dict[str, t.ContainerValue]
        type SingerTargetConfig = dict[
            str, str | int | bool | dict[str, t.ContainerValue]
        ]
        type LdifExportConfig = dict[str, t.ContainerValue]
        type TargetPipelineConfig = dict[str, bool | str | dict[str, t.ContainerValue]]


t = FlextTargetLdifTypes
__all__ = ["FlextTargetLdifTypes", "t"]
