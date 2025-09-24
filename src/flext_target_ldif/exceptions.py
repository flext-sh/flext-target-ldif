"""LDIF target exception hierarchy using flext-core DRY patterns.

Domain-specific exceptions using factory pattern to eliminate code duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel

from flext_core import FlextExceptions, FlextResult, FlextTypes


class FlextTargetLdifError(FlextExceptions.Error):
    """Base exception for FLEXT Target LDIF errors."""

    def __init__(
        self,
        message: str = "Target LDIF operation failed",
        **kwargs: object,
    ) -> None:
        """Initialize Target LDIF error with context."""
        super().__init__(f"Target LDIF: {message}", **kwargs)


class FlextTargetLdifTransformationError(FlextExceptions.ProcessingError):
    """Data transformation errors."""

    def __init__(
        self,
        message: str = "LDIF target transformation failed",
        record_data: FlextTypes.Core.Dict | None = None,
        transformation_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target transformation error with context."""
        context = kwargs.copy()
        if record_data is not None:
            # Include minimal record info for debugging
            context["record_keys"] = list(record_data.keys())
        if transformation_stage is not None:
            context["transformation_stage"] = transformation_stage

        super().__init__(f"LDIF target transformation: {message}")


class FlextTargetLdifInfrastructureError(FlextTargetLdifError):
    """Infrastructure and dependency injection errors."""

    def __init__(
        self,
        message: str = "LDIF target infrastructure error",
        component: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target infrastructure error with context."""
        context = kwargs.copy()
        if component is not None:
            context["component"] = component

        super().__init__(f"LDIF target infrastructure: {message}", **context)


class FlextTargetLdifWriterError(FlextTargetLdifError):
    """LDIF writer-specific errors."""

    def __init__(
        self,
        message: str = "LDIF writer error",
        output_file: str | None = None,
        line_number: int | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF writer error with context."""
        context = kwargs.copy()
        if output_file is not None:
            context["output_file"] = output_file
        if line_number is not None:
            context["line_number"] = line_number

        super().__init__(f"LDIF writer: {message}", **context)


class FlextTargetLdifFileError(FlextTargetLdifError):
    """File-related errors."""

    def __init__(
        self,
        message: str = "LDIF target file error",
        file_path: str | None = None,
        operation: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target file error with context."""
        context = kwargs.copy()
        if file_path is not None:
            context["file_path"] = file_path
        if operation is not None:
            context["operation"] = operation

        super().__init__(f"LDIF target file: {message}", **context)


class FlextTargetLdifSchemaError(Exception):
    """Schema validation errors."""

    def __init__(
        self,
        message: str = "LDIF target schema validation failed",
        schema_name: str | None = None,
        field: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target schema error with context."""
        self.message = message
        self.schema_name = schema_name
        self.field = field
        self.context = kwargs
        super().__init__(f"LDIF target schema: {message}")


class FlextTargetLdifErrorDetails(BaseModel):
    """Structured error details using flext-core patterns."""

    error_code: str
    error_type: str
    context: FlextTypes.Core.Dict
    timestamp: str
    source_component: str

    def validate_domain_rules(self: object) -> FlextResult[None]:
        """Validate domain-specific business rules."""
        try:
            # Validate error code format
            if not self.error_code or not self.error_code.startswith("LDIF"):
                return FlextResult[None].fail("Error code must start with 'LDIF'")

            # Validate error type is not empty
            if not self.error_type:
                return FlextResult[None].fail("Error type cannot be empty")

            # Validate source component is valid
            valid_components = [
                "writer",
                "sinks",
                "target",
                "infrastructure",
                "validation",
            ]
            if self.source_component not in valid_components:
                return FlextResult[None].fail(
                    f"Invalid source component: {self.source_component}",
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Domain validation failed: {e}")
