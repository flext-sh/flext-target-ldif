"""Singer LDIF target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult, FlextTypes


class FlextTargetLdifProtocols:
    """Singer Target LDIF protocols with explicit re-exports from FlextProtocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TargetLdif namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    Foundation = FlextProtocols.Foundation
    Domain = FlextProtocols.Domain
    Application = FlextProtocols.Application
    Infrastructure = FlextProtocols.Infrastructure
    Extensions = FlextProtocols.Extensions
    Commands = FlextProtocols.Commands

    # ============================================================================
    # SINGER TARGET LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TargetLdif:
        """Singer Target LDIF domain protocols for LDIF file generation."""

        @runtime_checkable
        class LdifGenerationProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF file generation."""

            def generate_ldif(
                self, records: list[FlextTypes.Dict]
            ) -> FlextResult[str]: ...

        @runtime_checkable
        class DataTransformationProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for Singer to LDIF transformation."""

            def transform_to_ldif(
                self, record: FlextTypes.Dict
            ) -> FlextResult[str]: ...

        @runtime_checkable
        class FileManagementProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF file management."""

            def write_ldif_file(
                self, file_path: str, content: str
            ) -> FlextResult[None]: ...

        @runtime_checkable
        class ValidationProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF validation."""

            def validate_ldif(self, ldif_content: str) -> FlextResult[bool]: ...

        @runtime_checkable
        class PerformanceProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF generation performance."""

            def optimize_batch(self, batch_size: int) -> FlextResult[int]: ...

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF generation monitoring."""

            def track_progress(self, records: int) -> FlextResult[None]: ...

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    LdifGenerationProtocol = TargetLdif.LdifGenerationProtocol
    DataTransformationProtocol = TargetLdif.DataTransformationProtocol
    FileManagementProtocol = TargetLdif.FileManagementProtocol
    ValidationProtocol = TargetLdif.ValidationProtocol
    PerformanceProtocol = TargetLdif.PerformanceProtocol
    MonitoringProtocol = TargetLdif.MonitoringProtocol

    TargetLdifGenerationProtocol = TargetLdif.LdifGenerationProtocol
    TargetLdifDataTransformationProtocol = TargetLdif.DataTransformationProtocol
    TargetLdifFileManagementProtocol = TargetLdif.FileManagementProtocol
    TargetLdifValidationProtocol = TargetLdif.ValidationProtocol
    TargetLdifPerformanceProtocol = TargetLdif.PerformanceProtocol
    TargetLdifMonitoringProtocol = TargetLdif.MonitoringProtocol


__all__ = [
    "FlextTargetLdifProtocols",
]
