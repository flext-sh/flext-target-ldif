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
            t.ContainerValue | t.ContainerValueMapping,
        ]
        type SingerSchema = Mapping[
            str,
            t.ContainerValue | Sequence[t.ContainerValueMapping],
        ]
        type SingerRecord = Mapping[
            str,
            t.ContainerValue | t.ContainerValueMapping,
        ]
        type SingerState = Mapping[str, t.ContainerValue | t.ContainerValueMapping]
        type StreamConfiguration = Mapping[str, str | bool | t.ContainerValueMapping]
        type TargetConfiguration = Mapping[
            str,
            t.ContainerValue | t.ContainerValueMapping,
        ]
        type MessageProcessing = Mapping[str, int | str | t.ContainerValueMapping]

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = Mapping[str, str | t.StrSequence | t.ContainerValueMapping]
        type Attributes = Mapping[
            str, str | t.StrSequence | bytes | t.ContainerValueMapping
        ]
        type LdifRecord = Mapping[
            str,
            t.ContainerValue | t.StrSequence | t.ContainerValueMapping,
        ]
        type LdifFileConfig = Mapping[str, t.Scalar | t.ContainerValueMapping]
        type LdifFormatting = Mapping[str, t.Scalar | t.ContainerValueMapping]
        type LdifValidation = Mapping[str, bool | str | t.ContainerValueMapping]
        type ExportResult = Mapping[
            str, int | str | t.StrSequence | t.ContainerValueMapping
        ]

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = Mapping[str, str | int | t.ContainerValueMapping]
        type StreamWriter = Mapping[str, str | bool | int | t.ContainerValueMapping]
        type FileOutput = Mapping[str, str | t.StrSequence | t.ContainerValueMapping]
        type CompressionConfig = Mapping[
            str, str | bool | int | t.ContainerValueMapping
        ]
        type FileValidation = Mapping[str, bool | str | t.ContainerValueMapping]
        type IOMetrics = Mapping[str, int | float | t.ContainerValueMapping]

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = Mapping[str, str | t.ContainerValueMapping]
        type AttributeMapping = Mapping[
            str, str | t.StrSequence | t.ContainerValueMapping
        ]
        type SchemaTransformation = Mapping[
            str,
            t.ContainerValue | t.ContainerValueMapping,
        ]
        type RecordTransformation = Mapping[
            str,
            t.ContainerValue | t.ContainerValueMapping,
        ]
        type DataNormalization = Mapping[str, bool | str | t.ContainerValueMapping]
        type TransformationRules = Mapping[
            str, str | t.StrSequence | t.ContainerValueMapping
        ]

    class TargetLdifValidation:
        """Validation complex types."""

        type LdifFormatValidation = Mapping[str, bool | str | t.ContainerValueMapping]
        type SingerCompliance = Mapping[str, bool | str | t.ContainerValueMapping]
        type SchemaValidation = Mapping[
            str, bool | t.StrSequence | t.ContainerValueMapping
        ]
        type RecordValidation = Mapping[str, bool | str | t.ContainerValueMapping]
        type FormatCompliance = Mapping[
            str, bool | str | t.StrSequence | t.ContainerValueMapping
        ]
        type ValidationRules = Mapping[str, bool | str | t.ContainerValueMapping]

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = Mapping[
            str,
            t.ContainerValue | t.ContainerValueMapping,
        ]
        type LdifTargetConfig = Mapping[str, t.Scalar | t.ContainerValueMapping]
        type OutputConfiguration = Mapping[str, str | t.ContainerValueMapping]
        type StreamMapping = Mapping[str, str | t.ContainerValueMapping]
        type BatchConfiguration = Mapping[str, int | bool | t.ContainerValueMapping]
        type ErrorHandling = Mapping[str, str | bool | t.ContainerValueMapping]

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = Mapping[str, int | float | t.ContainerValueMapping]
        type OptimizationConfig = Mapping[str, int | bool | t.ContainerValueMapping]
        type BufferConfiguration = Mapping[str, int | str | t.ContainerValueMapping]
        type StreamingConfig = Mapping[str, int | bool | t.ContainerValueMapping]
        type MemoryManagement = Mapping[str, int | bool | t.ContainerValueMapping]
        type IOOptimization = Mapping[str, int | bool | str | t.ContainerValueMapping]

    class Project:
        """FLEXT Target LDIF-specific project types.

        Adds FLEXT Target LDIF Singer target-specific project types.
        Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        type ProjectType = c.ProjectType
        type ErrorTypeLiteral = c.ErrorTypeLiteral
        type FlextTargetLdifSettings = Mapping[str, t.ContainerValue]
        type SingerTargetConfig = Mapping[str, t.Scalar | t.ContainerValueMapping]
        type LdifExportConfig = Mapping[str, t.ContainerValue]
        type TargetPipelineConfig = Mapping[str, bool | str | t.ContainerValueMapping]


t = FlextTargetLdifTypes
__all__ = ["FlextTargetLdifTypes", "t"]
