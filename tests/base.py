"""Service base for flext-target-ldif tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_target_ldif import m
from tests.settings import TestsFlextTargetLdifSettings


class TestsFlextTargetLdifServiceBase(tests_s):
    """Target LDIF test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextTargetLdifSettings:
        """Return the typed Target LDIF+Tests settings singleton."""
        return TestsFlextTargetLdifSettings.fetch_global()

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextTargetLdifSettings)


s = TestsFlextTargetLdifServiceBase

__all__: list[str] = ["TestsFlextTargetLdifServiceBase", "s"]
