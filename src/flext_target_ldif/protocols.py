"""Singer LDIF target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextTargetLdifProtocols:
    """Singer Target LDIF protocols with explicit re-exports from FlextCore.Protocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TargetLdif namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # SINGER TARGET LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TargetLdif:
        """Singer Target LDIF domain protocols for LDIF file generation."""

        @runtime_checkable
        class LdifGenerationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF file generation."""

            def generate_ldif(
                self, records: list[FlextCore.Types.Dict]
            ) -> FlextCore.Result[str]: ...

        @runtime_checkable
        class DataTransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Singer to LDIF transformation."""

            def transform_to_ldif(
                self, record: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]: ...

        @runtime_checkable
        class FileManagementProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF file management."""

            def write_ldif_file(
                self, file_path: str, content: str
            ) -> FlextCore.Result[None]: ...

        @runtime_checkable
        class ValidationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF validation."""

            def validate_ldif(self, ldif_content: str) -> FlextCore.Result[bool]: ...

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF generation performance."""

            def optimize_batch(self, batch_size: int) -> FlextCore.Result[int]: ...

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF generation monitoring."""

            def track_progress(self, records: int) -> FlextCore.Result[None]: ...

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
