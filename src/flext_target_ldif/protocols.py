"""Singer LDIF target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextResult


class FlextTargetLdifProtocols:
    """Singer Target LDIF protocols with explicit re-exports from p foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TargetLdif namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    # ============================================================================
    # SINGER TARGET LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TargetLdif:
        """Singer Target LDIF domain protocols for LDIF file generation."""

        @runtime_checkable
        class LdifGenerationProtocol(Protocol):
            """Protocol for LDIF file generation."""

            def generate_ldif(
                self, records: list[dict[str, object]]
            ) -> FlextResult[str]:
                """Generate LDIF content from records."""

        @runtime_checkable
        class DataTransformationProtocol(Protocol):
            """Protocol for Singer to LDIF transformation."""

            def transform_to_ldif(self, record: dict[str, object]) -> FlextResult[str]:
                """Transform Singer record to LDIF format."""

        @runtime_checkable
        class FileManagementProtocol(Protocol):
            """Protocol for LDIF file management."""

            def write_ldif_file(
                self, file_path: str, content: str
            ) -> FlextResult[None]:
                """Write LDIF content to file."""

        @runtime_checkable
        class ValidationProtocol(Protocol):
            """Protocol for LDIF validation."""

            def validate_ldif(self, ldif_content: str) -> FlextResult[bool]:
                """Validate LDIF content."""

        @runtime_checkable
        class PerformanceProtocol(Protocol):
            """Protocol for LDIF generation performance."""

            def optimize_batch(self, batch_size: int) -> FlextResult[int]:
                """Optimize batch size for performance."""
                msg = "Subclasses must implement optimize_batch"
                raise NotImplementedError(msg)

        @runtime_checkable
        class MonitoringProtocol(Protocol):
            """Protocol for LDIF generation monitoring."""

            def track_progress(self, records: int) -> FlextResult[None]:
                """Track progress of LDIF generation."""
                msg = "Subclasses must implement track_progress"
                raise NotImplementedError(msg)

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
