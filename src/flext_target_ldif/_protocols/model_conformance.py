# AUTO-GENERATED FILE — Regenerate with: make gen
"""Static instance-to-protocol evidence required by candidate admission.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_ldif/_protocols/model_conformance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flext_target_ldif import FlextTargetLdifModels, FlextTargetLdifProtocols

    def model_protocol_1(
        value: (FlextTargetLdifModels.ConfigRoot),
    ) -> FlextTargetLdifProtocols.ConfigRoot:
        return value

    def model_protocol_2(
        value: (FlextTargetLdifModels.ConfigRoot.ConfigNamespace),
    ) -> FlextTargetLdifProtocols.ConfigRootConfigNamespace:
        return value
