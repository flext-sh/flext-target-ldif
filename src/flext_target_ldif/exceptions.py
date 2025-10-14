"""LDIF target exception hierarchy using flext-core DRY patterns.

Domain-specific exceptions using factory pattern to eliminate code duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import override

from flext_core import FlextCore
from pydantic import BaseModel


class FlextTargetLdifError(FlextCore.Exceptions.Error):
    """Base exception for FLEXT Target LDIF errors."""

    @override
    def __init__(
        self,
        message: str = "Target LDIF operation failed",
        **kwargs: object,
    ) -> None:
        """Initialize Target LDIF error with context."""
        super().__init__(f"Target LDIF: {message}", **kwargs)


class FlextTargetLdifTransformationError(FlextCore.Exceptions.ProcessingError):
    """Data transformation errors."""

    @override
    def __init__(
        self,
        message: str = "LDIF target transformation failed",
        *,
        record_data: FlextCore.Types.Dict | None = None,
        transformation_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target transformation error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.record_data = record_data
        self.transformation_stage = transformation_stage

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with transformation-specific fields
        context = self._build_context(
            base_context,
            record_keys=list(record_data.keys()) if record_data is not None else None,
            transformation_stage=transformation_stage,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF target transformation: {message}",
            code=error_code or "TARGET_LDIF_TRANSFORMATION_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetLdifInfrastructureError(FlextTargetLdifError):
    """Infrastructure and dependency injection errors."""

    @override
    def __init__(
        self,
        message: str = "LDIF target infrastructure error",
        *,
        component: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target infrastructure error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.component = component

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with infrastructure-specific fields
        context = self._build_context(
            base_context,
            component=component,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF target infrastructure: {message}",
            code=error_code or "TARGET_LDIF_INFRASTRUCTURE_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetLdifWriterError(FlextTargetLdifError):
    """LDIF writer-specific errors."""

    @override
    def __init__(
        self,
        message: str = "LDIF writer error",
        *,
        output_file: str | None = None,
        line_number: int | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF writer error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.output_file = output_file
        self.line_number = line_number

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with writer-specific fields
        context = self._build_context(
            base_context,
            output_file=output_file,
            line_number=line_number,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF writer: {message}",
            code=error_code or "TARGET_LDIF_WRITER_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetLdifFileError(FlextTargetLdifError):
    """File-related errors."""

    @override
    def __init__(
        self,
        message: str = "LDIF target file error",
        *,
        file_path: str | None = None,
        operation: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target file error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.file_path = file_path
        self.operation = operation

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with file-specific fields
        context = self._build_context(
            base_context,
            file_path=file_path,
            operation=operation,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF target file: {message}",
            code=error_code or "TARGET_LDIF_FILE_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetLdifSchemaError(FlextCore.Exceptions.BaseError):
    """Schema validation errors."""

    @override
    def __init__(
        self,
        message: str = "LDIF target schema validation failed",
        *,
        schema_name: str | None = None,
        field: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF target schema error with context."""
        # Store domain-specific attributes before extracting common kwargs
        self.schema_name = schema_name
        self.field = field

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with schema-specific fields
        context = self._build_context(
            base_context,
            schema_name=schema_name,
            field=field,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF target schema: {message}",
            code=error_code or "TARGET_LDIF_SCHEMA_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTargetLdifErrorDetails(BaseModel):
    """Structured error details using flext-core patterns."""

    error_code: str
    error_type: str
    context: FlextCore.Types.Dict
    timestamp: str
    source_component: str

    def validate_domain_rules(self: object) -> FlextCore.Result[None]:
        """Validate domain-specific business rules."""
        try:
            # Validate error code format
            if not self.error_code or not self.error_code.startswith("LDIF"):
                return FlextCore.Result[None].fail("Error code must start with 'LDIF'")

            # Validate error type is not empty
            if not self.error_type:
                return FlextCore.Result[None].fail("Error type cannot be empty")

            # Validate source component is valid
            valid_components = [
                "writer",
                "sinks",
                "target",
                "infrastructure",
                "validation",
            ]
            if self.source_component not in valid_components:
                return FlextCore.Result[None].fail(
                    f"Invalid source component: {self.source_component}",
                )

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Domain validation failed: {e}")
