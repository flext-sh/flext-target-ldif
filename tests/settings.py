"""Runtime settings for flext-target-ldif tests."""

from __future__ import annotations

from typing import ClassVar

from flext_tests import FlextTestsSettings

from flext_target_ldif import FlextTargetLdifSettings, m


class TestsFlextTargetLdifSettings(FlextTargetLdifSettings, FlextTestsSettings):
    """Target LDIF settings extended with the shared test namespace."""

    model_config: ClassVar[m.SettingsConfigDict]


__all__: list[str] = ["TestsFlextTargetLdifSettings"]
