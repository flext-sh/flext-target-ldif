"""Internal runtime helpers for the target-ldif service facade."""

from __future__ import annotations

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
            target: p.Meltano.SingerTargetBase,
            stream_name: str,
            schema: t.MutableMappingKV[str, t.JsonValue],
            key_properties: t.StrSequence,
        ) -> FlextTargetLdifServiceRuntime.Sink:
            """Create an adapter sink and attach the LDIF runtime sink."""
            schema_dict = t.json_dict_adapter().validate_python(schema)
            service_sink = cls(
                target=target,
                stream_name=stream_name,
                schema=schema_dict,
                key_properties=key_properties,
            )
            service_sink._runtime_sink = runtime_sink
            return service_sink

        @override
        def process_batch(
            self,
            context: t.JsonMapping,
        ) -> None:
            """Singer batch hook is handled by the LDIF runtime sink."""
            self._runtime_sink.process_batch(
                u.normalize_to_json_mapping(context),
            )

        @override
        def process_record(
            self,
            record: t.JsonMapping,
            context: t.JsonMapping,
        ) -> None:
            """Delegate Singer record handling to the LDIF runtime sink."""
            self._runtime_sink.process_record(
                u.normalize_to_json_mapping(record),
                u.normalize_to_json_mapping(context),
            )

    @classmethod
    def create_sink(
        cls,
        *,
        stream_name: str,
        schema: t.JsonMapping,
        target_config: t.JsonMapping,
    ) -> p.Meltano.SingerDrainSink:
        """Create the LDIF runtime sink for the service facade."""
        normalized_target_config = u.normalize_to_json_mapping(
            target_config,
        )
        normalized_schema = cls.normalize_schema(schema)
        runtime_sink = FlextTargetLdifModels.TargetLdif.Sink(
            target_config=normalized_target_config,
            stream_name=stream_name,
            schema=normalized_schema,
        )
        return cls.Sink.create(
            runtime_sink=runtime_sink,
            target=cls.Target(
                config=t.json_dict_adapter().validate_python(normalized_target_config),
                validate_config=False,
            ),
            stream_name=stream_name,
            schema=t.json_dict_adapter().validate_python(normalized_schema),
            key_properties=[],
        )

    @staticmethod
    def normalize_schema(
        source: t.JsonMapping,
    ) -> t.MutableMappingKV[str, t.JsonValue]:
        """Normalize a flat Singer schema to the LDIF runtime contract."""
        return {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in source.items()
        }


__all__: list[str] = ["FlextTargetLdifServiceRuntime"]
