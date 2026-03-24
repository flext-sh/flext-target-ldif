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
            t.ContainerValue | Mapping[str, t.ContainerValue],
        ]
        type SingerSchema = Mapping[
            str,
            t.ContainerValue | Sequence[Mapping[str, t.ContainerValue]],
        ]
        type SingerRecord = Mapping[
            str,
            t.ContainerValue | Mapping[str, t.ContainerValue],
        ]
        type SingerState = Mapping[
            str, t.ContainerValue | Mapping[str, t.ContainerValue]
        ]
        type StreamConfiguration = Mapping[
            str, str | bool | Mapping[str, t.ContainerValue]
        ]
        type TargetConfiguration = Mapping[
            str,
            t.ContainerValue | Mapping[str, t.ContainerValue],
        ]
        type MessageProcessing = Mapping[
            str, int | str | Mapping[str, t.ContainerValue]
        ]

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = Mapping[
            str, str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]
        type Attributes = Mapping[
            str, str | Sequence[str] | bytes | Mapping[str, t.ContainerValue]
        ]
        type LdifRecord = Mapping[
            str,
            t.ContainerValue | Sequence[str] | Mapping[str, t.ContainerValue],
        ]
        type LdifFileConfig = Mapping[
            str, t.Scalar | Mapping[str, t.ContainerValue]
        ]
        type LdifFormatting = Mapping[
            str, t.Scalar | Mapping[str, t.ContainerValue]
        ]
        type LdifValidation = Mapping[str, bool | str | Mapping[str, t.ContainerValue]]
        type ExportResult = Mapping[
            str, int | str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = Mapping[
            str, str | int | Mapping[str, t.ContainerValue]
        ]
        type StreamWriter = Mapping[
            str, str | bool | int | Mapping[str, t.ContainerValue]
        ]
        type FileOutput = Mapping[
            str, str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]
        type CompressionConfig = Mapping[
            str, str | bool | int | Mapping[str, t.ContainerValue]
        ]
        type FileValidation = Mapping[str, bool | str | Mapping[str, t.ContainerValue]]
        type IOMetrics = Mapping[str, int | float | Mapping[str, t.ContainerValue]]

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = Mapping[str, str | Mapping[str, t.ContainerValue]]
        type AttributeMapping = Mapping[
            str, str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]
        type SchemaTransformation = Mapping[
            str,
            t.ContainerValue | Mapping[str, t.ContainerValue],
        ]
        type RecordTransformation = Mapping[
            str,
            t.ContainerValue | Mapping[str, t.ContainerValue],
        ]
        type DataNormalization = Mapping[
            str, bool | str | Mapping[str, t.ContainerValue]
        ]
        type TransformationRules = Mapping[
            str, str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]

    class TargetLdifValidation:
        """Validation complex types."""

        type LdifFormatValidation = Mapping[
            str, bool | str | Mapping[str, t.ContainerValue]
        ]
        type SingerCompliance = Mapping[
            str, bool | str | Mapping[str, t.ContainerValue]
        ]
        type SchemaValidation = Mapping[
            str, bool | Sequence[str] | Mapping[str, t.ContainerValue]
        ]
        type RecordValidation = Mapping[
            str, bool | str | Mapping[str, t.ContainerValue]
        ]
        type FormatCompliance = Mapping[
            str, bool | str | Sequence[str] | Mapping[str, t.ContainerValue]
        ]
        type ValidationRules = Mapping[str, bool | str | Mapping[str, t.ContainerValue]]

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = Mapping[
            str,
            t.ContainerValue | Mapping[str, t.ContainerValue],
        ]
        type LdifTargetConfig = Mapping[
            str, t.Scalar | Mapping[str, t.ContainerValue]
        ]
        type OutputConfiguration = Mapping[str, str | Mapping[str, t.ContainerValue]]
        type StreamMapping = Mapping[str, str | Mapping[str, t.ContainerValue]]
        type BatchConfiguration = Mapping[
            str, int | bool | Mapping[str, t.ContainerValue]
        ]
        type ErrorHandling = Mapping[str, str | bool | Mapping[str, t.ContainerValue]]

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = Mapping[
            str, int | float | Mapping[str, t.ContainerValue]
        ]
        type OptimizationConfig = Mapping[
            str, int | bool | Mapping[str, t.ContainerValue]
        ]
        type BufferConfiguration = Mapping[
            str, int | str | Mapping[str, t.ContainerValue]
        ]
        type StreamingConfig = Mapping[str, int | bool | Mapping[str, t.ContainerValue]]
        type MemoryManagement = Mapping[
            str, int | bool | Mapping[str, t.ContainerValue]
        ]
        type IOOptimization = Mapping[
            str, int | bool | str | Mapping[str, t.ContainerValue]
        ]

    class Project:
        """FLEXT Target LDIF-specific project types.

        Adds FLEXT Target LDIF Singer target-specific project types.
        Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        type ProjectType = c.ProjectType
        type ErrorTypeLiteral = c.ErrorTypeLiteral
        type FlextTargetLdifSettings = Mapping[str, t.ContainerValue]
        type SingerTargetConfig = Mapping[
            str, t.Scalar | Mapping[str, t.ContainerValue]
        ]
        type LdifExportConfig = Mapping[str, t.ContainerValue]
        type TargetPipelineConfig = Mapping[
            str, bool | str | Mapping[str, t.ContainerValue]
        ]


t = FlextTargetLdifTypes
__all__ = ["FlextTargetLdifTypes", "t"]
