"""Package version and metadata information.

Provides version information and package metadata for the flext-target-ldif package
using standard library metadata extraction.

Copyright (c) 2025 Flext Telecom. Todos os direitos reservados.
SPDX-License-Identifier: Proprietary
"""

from __future__ import annotations

from importlib.metadata import PackageMetadata, PackageNotFoundError, metadata


class FlextTargetLdifVersion:
    """Package version and metadata information.

    Provides version information and package metadata using standard library
    metadata extraction with graceful fallback handling.
    """

    _metadata: PackageMetadata | dict[str, str]
    try:
        _metadata = metadata("flext-target-ldif")
    except PackageNotFoundError:
        _metadata = {
            "Version": "0.12.0-dev",
            "Name": "flext-target-ldif",
            "Summary": "FLEXT Target LDIF (metadata fallback)",
            "Author": "",
            "Author-Email": "",
            "License": "",
            "Home-Page": "",
        }

    version = _metadata["Version"]
    version_info = tuple(
        int(part) if part.isdigit() else part for part in version.split(".")
    )

    __title__ = _metadata["Name"]
    __description__ = _metadata.get("Summary", "")
    __author__ = _metadata.get("Author", "")
    __author_email__ = _metadata.get("Author-Email", "")
    __license__ = _metadata.get("License", "")
    __url__ = _metadata.get("Home-Page", "")


__version__ = FlextTargetLdifVersion.version
__version_info__ = FlextTargetLdifVersion.version_info
__title__ = FlextTargetLdifVersion.__title__
__description__ = FlextTargetLdifVersion.__description__
__author__ = FlextTargetLdifVersion.__author__
__author_email__ = FlextTargetLdifVersion.__author_email__
__license__ = FlextTargetLdifVersion.__license__
__url__ = FlextTargetLdifVersion.__url__

__all__ = [
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
