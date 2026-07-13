"""Comprehensive tests for FlextTargetLdif main target class.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from flext_target_ldif import (
    FlextTargetLdifModels,
    FlextTargetLdifSettings,
    t,
)
from flext_target_ldif.target import FlextTargetLdif
from tests import c


class TestsFlextTargetLdifTarget:
    """Test FlextTargetLdifSettings value object."""

    # NOTE (multi-agent): mro-rn88 — settings project fields are namespaced under
    # TargetLdif.*; domain validation now fires as a model_validator at construction.
    def test_config_creation_with_defaults(self) -> None:
        """Test creating settings with default values."""
        settings = FlextTargetLdifSettings(TargetLdif={"output_file": "test.ldif"})
        target_ldif = settings.TargetLdif
        assert target_ldif.output_file == "test.ldif"
        assert target_ldif.schema_validation
        assert target_ldif.dn_template == "uid={uid},ou=users,dc=example,dc=com"
        assert target_ldif.line_length == 78
        assert not target_ldif.base64_encode

    def test_config_creation_with_custom_values(self) -> None:
        """Test creating settings with custom values."""
        with tempfile.TemporaryDirectory() as temp_dir:
            custom_file = f"{temp_dir}/custom.ldif"
            settings = FlextTargetLdifSettings(
                TargetLdif={
                    "output_file": custom_file,
                    "schema_validation": False,
                    "dn_template": "cn={name},ou=people,dc=test,dc=com",
                    "line_length": 100,
                    "base64_encode": True,
                    "attribute_mapping": {"email": "mail"},
                },
            )
            target_ldif = settings.TargetLdif
            assert target_ldif.output_file == custom_file
            assert not target_ldif.schema_validation
            assert target_ldif.dn_template == "cn={name},ou=people,dc=test,dc=com"
            assert target_ldif.line_length == 100
            assert target_ldif.base64_encode
            assert target_ldif.attribute_mapping == {"email": "mail"}

    def test_config_validation_empty_output_file(self) -> None:
        """Empty output file is rejected at construction by the domain validator."""
        with pytest.raises(c.ValidationError, match="Output file cannot be empty"):
            FlextTargetLdifSettings(TargetLdif={"output_file": ""})

    def test_config_validation_empty_dn_template(self) -> None:
        """Empty DN template is rejected at construction by the domain validator."""
        with pytest.raises(c.ValidationError, match="DN template cannot be empty"):
            FlextTargetLdifSettings(
                TargetLdif={"output_file": "test.ldif", "dn_template": ""},
            )

    def test_config_validation_invalid_line_length(self) -> None:
        """Test validation with invalid line length."""
        with pytest.raises(c.ValidationError):
            FlextTargetLdifSettings(
                TargetLdif={"output_file": "test.ldif", "line_length": 0},
            )

    def test_config_validation_valid_config(self) -> None:
        """A fully valid namespaced construction is accepted."""
        settings = FlextTargetLdifSettings(
            TargetLdif={
                "output_file": "test.ldif",
                "dn_template": "uid={uid},ou=users,dc=example,dc=com",
                "line_length": 78,
            },
        )
        assert settings.TargetLdif.output_file == "test.ldif"

    def test_target_inheritance(self) -> None:
        """Test that FlextTargetLdif is properly instantiated."""
        target = FlextTargetLdif()
        assert isinstance(target, FlextTargetLdif)

    def test_target_creation_with_defaults(self) -> None:
        """Test creating target with default configuration."""
        FlextTargetLdif()

    # NOTE (multi-agent): no-mock rewrite — these exercise the REAL public flow
    # (FlextTargetLdif.get_sink → Sink.process_record → Sink.clean_up) against real
    # LDIF files under tmp_path; the old test patched __init__ and asserted nothing
    # about behavior, which the workspace no-mock rule forbids.
    def test_end_to_end_sink_writes_real_ldif_file(self, tmp_path: Path) -> None:
        """A record through the public sink lands as a real LDIF file on disk."""
        target = FlextTargetLdif(settings={"output_path": str(tmp_path)})
        sink = target.get_sink(
            "users",
            schema={"type": "object", "properties": {}},
        )
        sink.process_record(
            {"uid": "jdoe", "cn": "John Doe", "mail": "jdoe@example.com"},
            {},
        )
        assert sink.ldif_writer.record_count == 1
        sink.clean_up()
        content = (tmp_path / "users.ldif").read_text(encoding="utf-8")
        assert content.startswith("version: 1\n")
        assert "dn: uid=jdoe,ou=users,dc=example,dc=com\n" in content
        assert "cn: John Doe\n" in content
        assert "mail: jdoe@example.com\n" in content

    def test_end_to_end_attribute_mapping_is_applied(self, tmp_path: Path) -> None:
        """Attribute mapping from settings renames attributes in the real output."""
        target = FlextTargetLdif(
            settings={
                "output_path": str(tmp_path),
                "attribute_mapping": {"email": "mail"},
            },
        )
        sink = target.get_sink(
            "people",
            schema={"type": "object", "properties": {}},
        )
        sink.process_record(
            {"uid": "jsmith", "email": "jsmith@example.com"},
            {},
        )
        sink.clean_up()
        content = (tmp_path / "people.ldif").read_text(encoding="utf-8")
        assert "dn: uid=jsmith,ou=users,dc=example,dc=com\n" in content
        assert "mail: jsmith@example.com\n" in content
        assert "email:" not in content

    def test_target_initialization_exposes_real_state(self, tmp_path: Path) -> None:
        """Real initialization creates the output directory and merges defaults."""
        target = FlextTargetLdif(settings={"output_path": str(tmp_path)})
        assert target.name == "target-ldif"
        assert target.settings["output_path"] == str(tmp_path)
        assert target.settings["dn_template"] == "uid={uid},ou=users,dc=example,dc=com"

    def test_target_validate_config_success(self) -> None:
        """Test successful settings validation."""
        target = FlextTargetLdif()
        target._test_config = {
            "output_file": "test.ldif",
            "schema_validation": True,
            "dn_template": "uid={uid},ou=users,dc=example,dc=com",
            "line_length": 78,
            "base64_encode": False,
        }
        target.validate_config()

    def test_target_validate_config_missing_output_file(self) -> None:
        """Test settings validation with missing output file."""
        target = FlextTargetLdif()
        target._test_config = {"schema_validation": True}
        with pytest.raises(ValueError) as exc_info:
            target.validate_config()
        if "Output file is required" not in str(exc_info.value):
            raise AssertionError(
                f"Expected {'Output file is required'} in {exc_info.value!s}",
            )

    def test_target_validate_config_invalid_output_file(self) -> None:
        """Test settings validation with invalid output file."""
        target = FlextTargetLdif()
        target._test_config = {"output_file": "", "schema_validation": True}
        with pytest.raises(ValueError) as exc_info:
            target.validate_config()
        if "Output file cannot be empty" not in str(exc_info.value):
            raise AssertionError(
                f"Expected {'Output file cannot be empty'} in {exc_info.value!s}",
            )

    def test_target_validate_config_invalid_dn_template(self) -> None:
        """Test settings validation with invalid DN template."""
        target = FlextTargetLdif()
        target._test_config = {
            "output_file": "test.ldif",
            "dn_template": "",
            "schema_validation": True,
        }
        with pytest.raises(ValueError) as exc_info:
            target.validate_config()
        if "DN template cannot be empty" not in str(exc_info.value):
            raise AssertionError(
                f"Expected {'DN template cannot be empty'} in {exc_info.value!s}",
            )

    def test_target_ldif_creation(self) -> None:
        """Test creating FlextTargetLdif instance."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            settings = {"output_path": tmp_dir}
            target = FlextTargetLdif(settings=settings)
            assert isinstance(target, FlextTargetLdif)

    def test_target_ldif_name_property(self) -> None:
        """Test target name property."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            settings = {"output_path": tmp_dir}
            target = FlextTargetLdif(settings=settings)
            if target.name != "target-ldif":
                raise AssertionError(f"Expected {'target-ldif'}, got {target.name}")

    def test_target_ldif_config_schema(self) -> None:
        """Test target settings schema is properly defined."""
        target = FlextTargetLdif()
        assert isinstance(target.config_jsonschema, dict)
        # NOTE (multi-agent): mro-rn88 — project fields live in the nested TargetLdif
        # schema definition ($defs._TargetLdif), not at the top level. Each level is
        # re-validated through t.json_mapping_adapter because JsonMapping values are
        # JsonValue unions, so raw chained .get() is not type-safe.
        schema_defs = t.json_mapping_adapter().validate_python(
            target.config_jsonschema.get("$defs", {}),
        )
        target_ldif_def = t.json_mapping_adapter().validate_python(
            schema_defs.get("_TargetLdif", {}),
        )
        target_ldif_props = t.json_mapping_adapter().validate_python(
            target_ldif_def.get("properties", {}),
        )
        assert "output_path" in target_ldif_props
        assert "file_naming_pattern" in target_ldif_props
        assert "dn_template" in target_ldif_props

    def test_target_ldif_default_sink_class(self) -> None:
        """Test target has proper default sink class."""
        target = FlextTargetLdif()
        if target.default_sink_class != FlextTargetLdifModels.TargetLdif.Sink:
            raise AssertionError(
                f"Expected {FlextTargetLdifModels.TargetLdif.Sink}, got {target.default_sink_class}",
            )

    def test_target_ldif_output_directory_creation(self) -> None:
        """Test target creates output directory."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "new_directory"
            settings = {"output_path": str(output_path)}
            assert not output_path.exists()
            FlextTargetLdif(settings=settings)
            assert output_path.exists()
            assert output_path.is_dir()

    def test_target_ldif_cli_method(self) -> None:
        """Test CLI method exists."""
        target = FlextTargetLdif()
        assert callable(target.cli)

    def test_target_ldif_config_dict_access(self) -> None:
        """Test settings t.JsonMapping access."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            settings = {
                "output_path": tmp_dir,
                "dn_template": "cn={name},ou=people,dc=test,dc=com",
            }
            target = FlextTargetLdif(settings=settings)
            if target.settings["output_path"] != tmp_dir:
                raise AssertionError(
                    f"Expected {tmp_dir}, got {target.settings['output_path']}",
                )
            assert (
                target.settings["dn_template"] == "cn={name},ou=people,dc=test,dc=com"
            )

    def test_target_ldif_default_config_values(self) -> None:
        """Test default configuration values."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            settings = {"output_path": tmp_dir}
            target = FlextTargetLdif(settings=settings)
            assert (
                target.settings["file_naming_pattern"]
                == "{stream_name}_{timestamp}.ldif"
            )
            assert (
                target.settings["dn_template"] == "uid={uid},ou=users,dc=example,dc=com"
            )

    def test_end_to_end_ldif_generation(self) -> None:
        """Test end-to-end LDIF generation."""
        with tempfile.NamedTemporaryFile(
            encoding="utf-8",
            mode="w+",
            delete=False,
            suffix=".ldif",
        ) as tmp:
            tmp_path = Path(tmp.name)
        settings = FlextTargetLdifSettings(
            TargetLdif={
                "output_file": str(tmp_path),
                "schema_validation": True,
                "dn_template": "uid={uid},ou=users,dc=example,dc=com",
            },
        )
        assert settings.TargetLdif.output_file == str(tmp_path)
        target = FlextTargetLdif()
        target._test_config = {
            "output_file": str(tmp_path),
            "schema_validation": True,
            "dn_template": "uid={uid},ou=users,dc=example,dc=com",
            "line_length": 78,
            "base64_encode": False,
        }
        target.validate_config()
        tmp_path.unlink()

    def test_target_ldif_alias_compatibility(self) -> None:
        """Test that FlextTargetLdif maintains compatibility."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            settings = {"output_path": tmp_dir}
            original_target = FlextTargetLdif(settings=settings)
            target = FlextTargetLdif()
            assert isinstance(original_target, FlextTargetLdif)
            assert isinstance(target, FlextTargetLdif)

    def test_config_to_dict_conversion(self) -> None:
        """Test settings can be converted to t.JsonMapping for Singer SDK."""
        settings = FlextTargetLdifSettings(
            TargetLdif={
                "output_file": "test.ldif",
                "schema_validation": True,
                "dn_template": "uid={uid},ou=users,dc=example,dc=com",
                "line_length": 100,
                "base64_encode": True,
                "attribute_mapping": {"email": "mail", "name": "cn"},
            },
        )
        config_dict = settings.model_dump()["TargetLdif"]
        assert config_dict["output_file"] == "test.ldif"
        assert config_dict["schema_validation"]
        assert config_dict["dn_template"] == "uid={uid},ou=users,dc=example,dc=com"
        assert config_dict["line_length"] == 100
        assert config_dict["base64_encode"]
        assert config_dict["attribute_mapping"] == {"email": "mail", "name": "cn"}

    def test_error_handling_integration(self) -> None:
        """Test error handling across the system."""
        with pytest.raises(c.ValidationError, match="Output file cannot be empty"):
            FlextTargetLdifSettings(TargetLdif={"output_file": ""})
        target = FlextTargetLdif()
        target._test_config = {"output_file": ""}
        with pytest.raises(ValueError):
            target.validate_config()

    def test_singer_sdk_compatibility(self) -> None:
        """Test compatibility with Singer SDK patterns."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            settings = {
                "output_path": tmp_dir,
                "dn_template": "uid={uid},ou=users,dc=example,dc=com",
                "file_naming_pattern": "{stream_name}.ldif",
            }
            target = FlextTargetLdif(settings=settings, validate_config=True)
            if target.settings["output_path"] != tmp_dir:
                raise AssertionError(
                    f"Expected {tmp_dir}, got {target.settings['output_path']}",
                )
            assert (
                target.settings["dn_template"] == "uid={uid},ou=users,dc=example,dc=com"
            )
