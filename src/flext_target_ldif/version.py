"""Project metadata for flext target ldif."""

from __future__ import annotations

from typing import Final, cast

from flext_core.metadata import (
    FlextProjectVersion,
    build_metadata_exports,
)

_metadata = build_metadata_exports(__file__)
globals().update(_metadata)
_metadata_obj = cast("FlextProjectMetadata", _metadata["__flext_metadata__"])


class FlextTargetLdifVersion(FlextProjectVersion):
    """Structured metadata for the flext target ldif distribution."""

    @classmethod
    def current(cls) -> FlextTargetLdifVersion:
        """Return canonical metadata loaded from pyproject.toml."""
        return cls.from_metadata(_metadata_obj)


VERSION: Final[FlextTargetLdifVersion] = FlextTargetLdifVersion.current()
__version__: Final[str] = VERSION.version
__version_info__: Final[tuple[int | str, ...]] = VERSION.version_info

for _name in tuple(_metadata):
    if _name not in {"__version__", "__version_info__"}:
        globals().pop(_name, None)

__all__ = ["VERSION", "FlextTargetLdifVersion", "__version__", "__version_info__"]
