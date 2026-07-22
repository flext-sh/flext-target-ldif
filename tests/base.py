"""Service base for flext-target-ldif tests."""

from __future__ import annotations

from typing import override

from flext_target_ldif import m
from flext_tests import s as tests_s
from tests.settings import TestsFlextTargetLdifSettings


class TestsFlextTargetLdifServiceBase(tests_s):
    """Target LDIF test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type.
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextTargetLdifSettings)


s = TestsFlextTargetLdifServiceBase

__all__: list[str] = ["TestsFlextTargetLdifServiceBase", "s"]
