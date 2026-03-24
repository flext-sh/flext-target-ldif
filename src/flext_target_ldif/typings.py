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

from collections.abc import Mapping, Sequence

from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes

from flext_target_ldif.constants import c


class FlextTargetLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """FLEXT Target LDIF-specific type definitions extending t.

    Domain-specific type system for Singer protocol LDIF file export operations.
    Contains ONLY complex Singer target and LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TargetLdif:
        """Singer protocol complex types."""

        type SingerMessage = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type SingerSchema = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue
            | Sequence[FlextMeltanoTypes.ContainerValueMapping],
        ]
        type SingerRecord = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type SingerState = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type StreamConfiguration = Mapping[
            str,
            str | bool | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type TargetConfiguration = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type MessageProcessing = Mapping[
            str,
            int | str | FlextMeltanoTypes.ContainerValueMapping,
        ]

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = Mapping[
            str,
            str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type Attributes = Mapping[
            str,
            str
            | FlextMeltanoTypes.StrSequence
            | bytes
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type LdifRecord = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type LdifFileConfig = Mapping[
            str,
            FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type LdifFormatting = Mapping[
            str,
            FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type LdifValidation = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type ExportResult = Mapping[
            str,
            int
            | str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = Mapping[
            str,
            str | int | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type StreamWriter = Mapping[
            str,
            str | bool | int | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type FileOutput = Mapping[
            str,
            str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type CompressionConfig = Mapping[
            str,
            str | bool | int | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type FileValidation = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type IOMetrics = Mapping[
            str,
            int | float | FlextMeltanoTypes.ContainerValueMapping,
        ]

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = Mapping[
            str,
            str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type AttributeMapping = Mapping[
            str,
            str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type SchemaTransformation = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type RecordTransformation = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type DataNormalization = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type TransformationRules = Mapping[
            str,
            str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]

    class TargetLdifValidation:
        """Validation complex types."""

        type LdifFormatValidation = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type SingerCompliance = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type SchemaValidation = Mapping[
            str,
            bool
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type RecordValidation = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type FormatCompliance = Mapping[
            str,
            bool
            | str
            | FlextMeltanoTypes.StrSequence
            | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type ValidationRules = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = Mapping[
            str,
            FlextMeltanoTypes.ContainerValue | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type LdifTargetConfig = Mapping[
            str,
            FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type OutputConfiguration = Mapping[
            str,
            str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type StreamMapping = Mapping[str, str | FlextMeltanoTypes.ContainerValueMapping]
        type BatchConfiguration = Mapping[
            str,
            int | bool | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type ErrorHandling = Mapping[
            str,
            str | bool | FlextMeltanoTypes.ContainerValueMapping,
        ]

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = Mapping[
            str,
            int | float | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type OptimizationConfig = Mapping[
            str,
            int | bool | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type BufferConfiguration = Mapping[
            str,
            int | str | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type StreamingConfig = Mapping[
            str,
            int | bool | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type MemoryManagement = Mapping[
            str,
            int | bool | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type IOOptimization = Mapping[
            str,
            int | bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]

    class Project:
        """FLEXT Target LDIF-specific project types.

        Adds FLEXT Target LDIF Singer target-specific project types.
        Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        type ProjectType = c.ProjectType
        type ErrorTypeLiteral = c.ErrorTypeLiteral
        type FlextTargetLdifSettings = Mapping[str, FlextMeltanoTypes.ContainerValue]
        type SingerTargetConfig = Mapping[
            str,
            FlextMeltanoTypes.Scalar | FlextMeltanoTypes.ContainerValueMapping,
        ]
        type LdifExportConfig = Mapping[str, FlextMeltanoTypes.ContainerValue]
        type TargetPipelineConfig = Mapping[
            str,
            bool | str | FlextMeltanoTypes.ContainerValueMapping,
        ]


t = FlextTargetLdifTypes
__all__ = ["FlextTargetLdifTypes", "t"]
