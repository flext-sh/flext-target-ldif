"""Service base for flext-target-ldif tests."""

from __future__ import annotations

from typing import override

from flext_tests import s

from flext_target_ldif import m
from tests import TestsFlextTargetLdifSettings, p


class TestsFlextTargetLdifServiceBase(s):
    """Target LDIF test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type.
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> p.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextTargetLdifSettings)


s = TestsFlextTargetLdifServiceBase

__all__: list[str] = ["TestsFlextTargetLdifServiceBase", "s"]
