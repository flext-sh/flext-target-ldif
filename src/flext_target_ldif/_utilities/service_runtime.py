"""Internal runtime helpers for the target-ldif service facade."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import override

from flext_meltano import FlextMeltanoSingerSinkBase, FlextMeltanoSingerTargetBase

from flext_target_ldif import u
from flext_target_ldif.models import FlextTargetLdifModels
from flext_target_ldif.target import FlextTargetLdif
from flext_target_ldif.typings import t


class FlextTargetLdifServiceRuntime:
    """Service-runtime helpers used by the target-ldif facade."""

    class Target(FlextMeltanoSingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = "target-ldif"

    class Sink(FlextMeltanoSingerSinkBase):
        """Singer sink adapter delegating to the LDIF runtime sink."""

        name = "target-ldif-sink"

        def __init__(
            self,
            *,
            runtime_sink: FlextTargetLdifModels.TargetLdif.Sink,
            target: FlextMeltanoSingerTargetBase,
            stream_name: str,
            schema: dict[str, t.ContainerValue],
            key_properties: t.StrSequence,
        ) -> None:
            """Initialize the adapter and keep the LDIF runtime sink."""
            super().__init__(
                target=target,
                stream_name=stream_name,
                schema=schema,
                key_properties=key_properties,
            )
            self._runtime_sink = runtime_sink

        @override
        def process_batch(
            self,
            context: Mapping[str, t.NormalizedValue],
        ) -> None:
            """Singer batch hook is handled by the LDIF runtime sink."""
            self._runtime_sink.process_batch(
                FlextTargetLdifServiceRuntime.normalize_singer_mapping(context),
            )

        @override
        def process_record(
            self,
            record: Mapping[str, t.NormalizedValue],
            context: Mapping[str, t.NormalizedValue],
        ) -> None:
            """Delegate Singer record handling to the LDIF runtime sink."""
            self._runtime_sink.process_record(
                FlextTargetLdifServiceRuntime.normalize_singer_mapping(record),
                FlextTargetLdifServiceRuntime.normalize_singer_mapping(context),
            )

    @classmethod
    def create_sink(
        cls,
        *,
        stream_name: str,
        schema: t.FlatContainerMapping,
        target_config: t.ContainerMapping,
    ) -> FlextMeltanoSingerSinkBase:
        """Create the LDIF runtime sink for the service facade."""
        normalized_target_config = cls.normalize_singer_mapping(target_config)
        runtime_target = FlextTargetLdif(
            config=normalized_target_config,
            validate_config=False,
        )
        normalized_schema = cls.normalize_schema(schema)
        runtime_sink = runtime_target.get_sink(
            stream_name=stream_name,
            schema=normalized_schema,
        )
        return cls.Sink(
            runtime_sink=runtime_sink,
            target=cls.Target(config=normalized_target_config, validate_config=False),
            stream_name=stream_name,
            schema=dict(normalized_schema),
            key_properties=[],
        )

    @classmethod
    def normalize_singer_mapping(
        cls,
        source: Mapping[str, t.NormalizedValue],
    ) -> dict[str, t.ContainerValue]:
        """Normalize a Singer payload mapping to the LDIF runtime contract."""
        normalized: dict[str, t.ContainerValue] = {}
        for key, value in source.items():
            normalized_value = cls.normalize_singer_value(value)
            if normalized_value is not None:
                normalized[str(key)] = normalized_value
        return normalized

    @classmethod
    def normalize_singer_value(
        cls,
        value: t.NormalizedValue,
    ) -> t.ContainerValue | None:
        """Normalize a Singer payload value to the LDIF runtime contract."""
        if value is None:
            return None
        if isinstance(value, Path):
            return str(value)
        if u.is_scalar(value):
            return value
        if u.is_mapping(value):
            return cls.normalize_singer_mapping(value)
        normalized_sequence: list[t.ContainerValue] = []
        for item in value:
            normalized_item = cls.normalize_singer_value(item)
            if normalized_item is not None:
                normalized_sequence.append(normalized_item)
        return normalized_sequence

    @staticmethod
    def normalize_schema(
        source: t.FlatContainerMapping,
    ) -> dict[str, t.ContainerValue]:
        """Normalize a flat Singer schema to the LDIF runtime contract."""
        return {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in source.items()
        }


__all__ = ["FlextTargetLdifServiceRuntime"]
