# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_target_ldif.tests.unit.test_target import (
        TestsFlextTargetLdifTarget as TestsFlextTargetLdifTarget,
    )
    from flext_target_ldif.tests.unit.test_writer import (
        TestsFlextTargetLdifWriter as TestsFlextTargetLdifWriter,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_target": ("TestsFlextTargetLdifTarget",),
        ".test_writer": ("TestsFlextTargetLdifWriter",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
