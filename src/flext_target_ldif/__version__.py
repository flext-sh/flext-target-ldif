"""Version information for flext-target-ldif package.

This module contains version information for the flext-target-ldif package.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

try:
    __version__ = importlib.metadata.version("flext-target-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
