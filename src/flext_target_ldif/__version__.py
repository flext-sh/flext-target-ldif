# AUTO-GENERATED FILE — Regenerate with: make gen
"""Package version and metadata for flext-target-ldif.

Subclass of ``FlextVersion`` — overrides only ``_metadata``.
All derived attributes (``__version__``, ``__title__``, etc.) are
computed automatically via ``FlextVersion.__init_subclass__``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from importlib.metadata import PackageMetadata, metadata

from flext_core.__version__ import FlextVersion


class FlextTargetLdifVersion(FlextVersion):
    """flext-target-ldif version — MRO-derived from FlextVersion."""

    _metadata: PackageMetadata = metadata("flext-target-ldif")


__version__ = FlextTargetLdifVersion.__version__
__version_info__ = FlextTargetLdifVersion.__version_info__
__title__ = FlextTargetLdifVersion.__title__
__description__ = FlextTargetLdifVersion.__description__
__author__ = FlextTargetLdifVersion.__author__
__author_email__ = FlextTargetLdifVersion.__author_email__
__license__ = FlextTargetLdifVersion.__license__
__url__ = FlextTargetLdifVersion.__url__
__all__: list[str] = [
    "FlextTargetLdifVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
]
