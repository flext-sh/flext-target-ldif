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

from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes


class FlextTargetLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """FLEXT Target LDIF-specific type definitions extending t.

    Domain-specific type system for Singer protocol LDIF file export operations.
    Contains ONLY complex Singer target and LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TargetLdif:
        """Singer protocol complex types."""

        type SingerMessage = dict[str, object | dict[str, object]]
        type SingerSchema = dict[str, object | list[dict[str, object]]]
        type SingerRecord = dict[str, object | dict[str, object]]
        type SingerState = dict[str, object | dict[str, object]]
        type StreamConfiguration = dict[str, str | bool | dict[str, object]]
        type TargetConfiguration = dict[str, object | dict[str, object]]
        type MessageProcessing = dict[str, int | str | dict[str, object]]

    class LdifExport:
        """LDIF export complex types."""

        type LdifEntry = dict[str, str | list[str] | dict[str, object]]
        type Attributes = dict[str, str | list[str] | bytes | dict[str, object]]
        type LdifRecord = dict[str, object | list[str] | dict[str, object]]
        type LdifFileConfig = dict[str, str | int | bool | dict[str, object]]
        type LdifFormatting = dict[str, str | int | bool | dict[str, object]]
        type LdifValidation = dict[str, bool | str | dict[str, object]]
        type ExportResult = dict[str, int | str | list[str] | dict[str, object]]

    class FileProcessing:
        """File processing complex types."""

        type FileConfiguration = dict[str, str | int | dict[str, object]]
        type StreamWriter = dict[str, str | bool | int | dict[str, object]]
        type FileOutput = dict[str, str | list[str] | dict[str, object]]
        type CompressionConfig = dict[str, str | bool | int | dict[str, object]]
        type FileValidation = dict[str, bool | str | dict[str, object]]
        type IOMetrics = dict[str, int | float | dict[str, object]]

    class DataTransformation:
        """Data transformation complex types."""

        type SingerToLdifMapping = dict[str, str | dict[str, object]]
        type AttributeMapping = dict[str, str | list[str] | dict[str, object]]
        type SchemaTransformation = dict[str, object | dict[str, object]]
        type RecordTransformation = dict[str, object | dict[str, object]]
        type DataNormalization = dict[str, bool | str | dict[str, object]]
        type TransformationRules = dict[str, str | list[str] | dict[str, object]]

    class TargetLdifValidation:
        """Validation complex types."""

        type LdifFormatValidation = dict[str, bool | str | dict[str, object]]
        type SingerCompliance = dict[str, bool | str | dict[str, object]]
        type SchemaValidation = dict[str, bool | list[str] | dict[str, object]]
        type RecordValidation = dict[str, bool | str | dict[str, object]]
        type FormatCompliance = dict[str, bool | str | list[str] | dict[str, object]]
        type ValidationRules = dict[str, bool | str | dict[str, object]]

    class TargetConfiguration:
        """Target configuration complex types."""

        type TargetSettings = dict[str, object | dict[str, object]]
        type LdifTargetConfig = dict[str, str | int | bool | dict[str, object]]
        type OutputConfiguration = dict[str, str | dict[str, object]]
        type StreamMapping = dict[str, str | dict[str, object]]
        type BatchConfiguration = dict[str, int | bool | dict[str, object]]
        type ErrorHandling = dict[str, str | bool | dict[str, object]]

    class Performance:
        """Performance complex types."""

        type PerformanceMetrics = dict[str, int | float | dict[str, object]]
        type OptimizationConfig = dict[str, int | bool | dict[str, object]]
        type BufferConfiguration = dict[str, int | str | dict[str, object]]
        type StreamingConfig = dict[str, int | bool | dict[str, object]]
        type MemoryManagement = dict[str, int | bool | dict[str, object]]
        type IOOptimization = dict[str, int | bool | str | dict[str, object]]

    class Project:
        """FLEXT Target LDIF-specific project types.

        Adds FLEXT Target LDIF Singer target-specific project types.
        Follows domain separation principle:
        FLEXT Target LDIF domain owns Singer LDIF target and LDIF export-specific types.
        """

        type ProjectType = Literal[
            "library",
            "application",
            "service",
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
        type FlextTargetLdifSettings = dict[str, object]
        type SingerTargetConfig = dict[str, str | int | bool | dict[str, object]]
        type LdifExportConfig = dict[str, object]
        type TargetPipelineConfig = dict[str, bool | str | dict[str, object]]


t = FlextTargetLdifTypes
__all__ = ["FlextTargetLdifTypes", "t"]
