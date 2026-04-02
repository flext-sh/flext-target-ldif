# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Internal utilities subpackage."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_target_ldif._utilities import service_runtime
    from flext_target_ldif._utilities.service_runtime import (
        FlextTargetLdifServiceRuntime,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTargetLdifServiceRuntime": "flext_target_ldif._utilities.service_runtime",
    "service_runtime": "flext_target_ldif._utilities.service_runtime",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
