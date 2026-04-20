"""Internal runtime helpers for the target-ldif service facade."""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from pathlib import Path
from typing import override

from flext_target_ldif import FlextTargetLdifModels, m, p, t, u


class FlextTargetLdifServiceRuntime:
    """Service-runtime helpers used by the target-ldif facade."""

    class Target(m.Meltano.SingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = "target-ldif"

    class Sink(m.Meltano.SingerSinkBase):
        """Singer sink adapter delegating to the LDIF runtime sink."""

        name = "target-ldif-sink"

        _runtime_sink: FlextTargetLdifModels.TargetLdif.Sink

        @classmethod
        def create(
            cls,
            *,
            runtime_sink: FlextTargetLdifModels.TargetLdif.Sink,
            target: m.Meltano.SingerTargetBase,
            stream_name: str,
            schema: t.MutableMappingKV[str, t.Container],
            key_properties: t.StrSequence,
        ) -> FlextTargetLdifServiceRuntime.Sink:
            """Create an adapter sink and attach the LDIF runtime sink."""
            service_sink = cls(
                target=target,
                stream_name=stream_name,
                schema=schema,
                key_properties=key_properties,
            )
            service_sink._runtime_sink = runtime_sink
            return service_sink

        @override
        def process_batch(
            self,
            context: Mapping[str, t.Container],
        ) -> None:
            """Singer batch hook is handled by the LDIF runtime sink."""
            self._runtime_sink.process_batch(
                FlextTargetLdifServiceRuntime.normalize_singer_mapping(context),
            )

        @override
        def process_record(
            self,
            record: Mapping[str, t.Container],
            context: Mapping[str, t.Container],
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
        target_config: Mapping[str, t.Container],
    ) -> p.Meltano.SingerDrainSink:
        """Create the LDIF runtime sink for the service facade."""
        normalized_target_config = cls.normalize_singer_mapping(target_config)
        normalized_schema = cls.normalize_schema(schema)
        runtime_sink = FlextTargetLdifModels.TargetLdif.Sink(
            target_config=normalized_target_config,
            stream_name=stream_name,
            schema=normalized_schema,
        )
        return cls.Sink.create(
            runtime_sink=runtime_sink,
            target=cls.Target(
                config=dict(normalized_target_config),
                validate_config=False,
            ),
            stream_name=stream_name,
            schema=dict(normalized_schema),
            key_properties=[],
        )

    @classmethod
    def normalize_singer_mapping(
        cls,
        source: Mapping[str, t.Container],
    ) -> t.MutableMappingKV[str, t.Container]:
        """Normalize a Singer payload mapping to the LDIF runtime contract."""
        normalized: t.MutableMappingKV[str, t.Container] = {}
        for key, value in source.items():
            normalized_value = cls.normalize_singer_value(value)
            if normalized_value is not None:
                normalized[str(key)] = normalized_value
        return normalized

    @classmethod
    def normalize_singer_value(
        cls,
        value: t.Container,
    ) -> t.Container | None:
        """Normalize a Singer payload value to the LDIF runtime contract."""
        if value is None:
            return None
        if isinstance(value, Path):
            return str(value)
        if u.scalar(value):
            return value
        if u.mapping(value):
            return cls.normalize_singer_mapping(value)
        normalized_sequence: t.MutableSequenceOf[t.Container] = []
        for item in value:
            normalized_item = cls.normalize_singer_value(item)
            if normalized_item is not None:
                normalized_sequence.append(normalized_item)
        return normalized_sequence

    @staticmethod
    def normalize_schema(
        source: t.FlatContainerMapping,
    ) -> t.MutableMappingKV[str, t.Container]:
        """Normalize a flat Singer schema to the LDIF runtime contract."""
        return {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in source.items()
        }


__all__: list[str] = ["FlextTargetLdifServiceRuntime"]
