"""Singer LDIF target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_ldif.protocols import p as p_ldif
from flext_meltano.protocols import p as p_meltano


class FlextTargetLdifProtocols(p_meltano, p_ldif):
    """Singer Target LDIF protocols extending LDIF and Meltano protocols.

    Extends both FlextLdifProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all LDIF protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextLdifProtocols (inherits .Ldif.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: Target LDIF-specific protocols in Target.Ldif namespace
    - PROVIDES: Root-level alias `p` for convenient access

    Usage:
        from flext_target_ldif.protocols import p

        # Foundation protocols (inherited)
        result: p.Result[str]
        service: p.Service[str]

        # LDIF protocols (inherited)
        entry: p.Models.EntryProtocol

        # Meltano protocols (inherited)
        target: p.Meltano.TargetProtocol

        # Target LDIF-specific protocols
        ldif_generation: p.Target.Ldif.LdifGenerationProtocol
    """

    class Target:
        """Singer Target domain protocols."""

        class Ldif:
            """Singer Target LDIF domain protocols for LDIF file generation.

            Provides protocol definitions for LDIF file generation, data transformation,
            file management, validation, performance optimization, and monitoring.
            """

            @runtime_checkable
            class LdifGenerationProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF file generation.

                Defines the interface for generating LDIF content from records.
                """

                def generate_ldif(
                    self,
                    records: list[dict[str, object]],
                ) -> p_meltano.Result[str]:
                    """Generate LDIF content from records.

                    Args:
                        records: List of records to convert to LDIF format.

                    Returns:
                        Result containing the generated LDIF content as a string.

                    """

            @runtime_checkable
            class DataTransformationProtocol(p_ldif.Service[object], Protocol):
                """Protocol for Singer to LDIF transformation.

                Defines the interface for transforming Singer records to LDIF format.
                """

                def transform_to_ldif(
                    self,
                    record: dict[str, object],
                ) -> p_meltano.Result[str]:
                    """Transform Singer record to LDIF format.

                    Args:
                        record: Singer record to transform.

                    Returns:
                        Result containing the transformed LDIF content as a string.

                    """

            @runtime_checkable
            class FileManagementProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF file management.

                Defines the interface for managing LDIF files, including writing content.
                """

                def write_ldif_file(
                    self,
                    file_path: str,
                    content: str,
                ) -> p_meltano.Result[bool]:
                    """Write LDIF content to file.

                    Args:
                        file_path: Path to the file to write.
                        content: LDIF content to write.

                    Returns:
                        Result indicating success or failure of the write operation.

                    """

            @runtime_checkable
            class ValidationProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF validation.

                Defines the interface for validating LDIF content.
                """

                def validate_ldif(
                    self,
                    ldif_content: str,
                ) -> p_meltano.Result[bool]:
                    """Validate LDIF content.

                    Args:
                        ldif_content: LDIF content to validate.

                    Returns:
                        Result indicating whether the content is valid.

                    """

            @runtime_checkable
            class PerformanceProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF generation performance.

                Defines the interface for optimizing LDIF generation performance.
                """

                def optimize_batch(
                    self,
                    batch_size: int,
                ) -> p_meltano.Result[int]:
                    """Optimize batch size for performance.

                    Args:
                        batch_size: Current batch size.

                    Returns:
                        Result containing the optimized batch size.

                    """

            @runtime_checkable
            class MonitoringProtocol(p_ldif.Service[object], Protocol):
                """Protocol for LDIF generation monitoring.

                Defines the interface for monitoring LDIF generation progress.
                """

                def track_progress(
                    self,
                    records: int,
                ) -> p_meltano.Result[bool]:
                    """Track progress of LDIF generation.

                    Args:
                        records: Number of records processed.

                    Returns:
                        Result indicating success or failure of tracking.

                    """


# Runtime alias for simplified usage
p = FlextTargetLdifProtocols
__all__ = [
    "FlextTargetLdifProtocols",
    "p",
]
