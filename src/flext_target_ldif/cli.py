"""CLI entry point for FlextTargetLdif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_target_ldif import FlextTargetLdifService, t


class FlextTargetLdifCli:
    """CLI wrapper bound to the target-ldif service facade."""

    @classmethod
    def run(cls, args: t.StrSequence | None = None) -> int:
        """Execute the canonical target-ldif CLI entry point."""
        _ = cls
        return FlextTargetLdifService.get_instance().cli_main(args)


def main(args: t.StrSequence | None = None) -> int:
    """Provide CLI entry point."""
    return FlextTargetLdifCli.run(args)


__all__: list[str] = ["FlextTargetLdifCli", "main"]
