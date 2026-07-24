"""Runtime settings for flext-target-ldif tests."""

from __future__ import annotations

from flext_target_ldif import FlextTargetLdifSettings
from flext_tests import FlextTestsSettings


class TestsFlextTargetLdifSettings(FlextTargetLdifSettings, FlextTestsSettings):
    """Target LDIF settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTargetLdifSettings"]
