# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_target": (
            "TestFlextTargetLdif",
            "TestFlextTargetLdifClass",
            "TestFlextTargetLdifSettings",
            "TestIntegration",
        ),
        ".test_writer": (
            "TestFlextTargetLdifWriterBase64Encoding",
            "TestFlextTargetLdifWriterContextManager",
            "TestFlextTargetLdifWriterDnGeneration",
            "TestFlextTargetLdifWriterFileOperations",
            "TestFlextTargetLdifWriterHeaderGeneration",
            "TestFlextTargetLdifWriterInitialization",
            "TestFlextTargetLdifWriterLineWrapping",
            "TestFlextTargetLdifWriterProperties",
            "TestFlextTargetLdifWriterRecordWriting",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
