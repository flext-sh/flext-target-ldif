# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_TARGET_LDIF_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._utilities": ("_utilities",),
        ".api": (
            "FlextTargetLdifService",
            "target_ldif",
        ),
        ".cli": (
            "FlextTargetLdifCli",
            "main",
        ),
        ".constants": (
            "FlextTargetLdifConstants",
            "c",
        ),
        ".models": (
            "FlextTargetLdifModels",
            "m",
        ),
        ".protocols": (
            "FlextTargetLdifProtocols",
            "p",
        ),
        ".settings": ("FlextTargetLdifSettings",),
        ".typings": (
            "FlextTargetLdifTypes",
            "t",
        ),
        ".utilities": (
            "FlextTargetLdifUtilities",
            "u",
        ),
        "flext_core._root_typing_parts": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)

__all__: list[str] = ["FLEXT_TARGET_LDIF_LAZY_IMPORTS_PART_01"]
