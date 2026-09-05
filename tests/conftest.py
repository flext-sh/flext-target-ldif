"""Pytest configuration for FLEXT Target LDIF tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Generator
from typing import TYPE_CHECKING

import pytest

from flext_tests import u

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture(autouse=True)
def isolate_working_directory(tmp_path: Path) -> Generator[None]:
    """Run every test from a temporary working directory.

    The writer resolves its default ``output.ldif`` relative to the working
    directory, and ``close()`` flushes even when ``open()`` was never called.
    Without this isolation a plain ``FlextTargetLdifWriter()`` drops
    ``output.ldif`` into the repository root, leaving the worktree dirty and
    breaking every gate that requires a clean tree.

    The shared test scope restores the original directory during teardown.
    """
    with u.Tests.Matchers.scope(cwd=tmp_path):
        yield
