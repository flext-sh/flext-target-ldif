# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_target_ldif._utilities.service_runtime as _flext_target_ldif__utilities_service_runtime

    service_runtime = _flext_target_ldif__utilities_service_runtime
    from flext_target_ldif._utilities.service_runtime import (
        FlextTargetLdifServiceRuntime,
    )
_LAZY_IMPORTS = {
    "FlextTargetLdifServiceRuntime": "flext_target_ldif._utilities.service_runtime",
    "service_runtime": "flext_target_ldif._utilities.service_runtime",
}

__all__ = [
    "FlextTargetLdifServiceRuntime",
    "service_runtime",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
