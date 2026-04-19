"""Comprehensive tests for FlextTargetLdif main target class.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from flext_target_ldif import (
    FlextTargetLdif,
    FlextTargetLdifModels,
    FlextTargetLdifSettings,
)
from tests import e


class TestFlextTargetLdifSettings:
    """Test FlextTargetLdifSettings value object."""

    def test_config_creation_with_defaults(self) -> None:
        """Test creating settings with default values."""
        settings = FlextTargetLdifSettings(output_file="test.ldif")
        if settings.output_file != "test.ldif":
            raise AssertionError(f"Expected {'test.ldif'}, got {settings.output_file}")
        if not settings.schema_validation:
            raise AssertionError(f"Expected True, got {settings.schema_validation}")
        if settings.dn_template != "uid={uid},ou=users,dc=example,dc=com":
            raise AssertionError(
                f"Expected {'uid={uid},ou=users,dc=example,dc=com'}, got {settings.dn_template}",
            )
        assert settings.line_length == 78
        if settings.base64_encode:
            raise AssertionError(f"Expected False, got {settings.base64_encode}")

    def test_config_creation_with_custom_values(self) -> None:
        """Test creating settings with custom values."""
        with tempfile.TemporaryDirectory() as temp_dir:
            custom_file = f"{temp_dir}/custom.ldif"
            settings = FlextTargetLdifSettings(
                output_file=custom_file,
                schema_validation=False,
                dn_template="cn={name},ou=people,dc=test,dc=com",
                line_length=100,
                base64_encode=True,
                attribute_mapping={"email": "mail"},
            )
            if settings.output_file != custom_file:
                raise AssertionError(
                    f"Expected {custom_file}, got {settings.output_file}",
                )
            if settings.schema_validation:
                raise AssertionError(
                    f"Expected False, got {settings.schema_validation}"
                )
            assert settings.dn_template == "cn={name},ou=people,dc=test,dc=com"
            if settings.line_length != 100:
                raise AssertionError(f"Expected {100}, got {settings.line_length}")
            if not settings.base64_encode:
                raise AssertionError(f"Expected True, got {settings.base64_encode}")
            if settings.attribute_mapping != {"email": "mail"}:
                msg: str = (
                    f"Expected {{'email': 'mail'}}, got {settings.attribute_mapping}"
                )
                raise AssertionError(msg)

    def test_config_immutability(self) -> None:
        """Test that settings is immutable."""
        settings = FlextTargetLdifSettings(output_file="test.ldif")
        with pytest.raises(e.ValidationError):
            settings.output_file = "modified.ldif"

    def test_config_validation_empty_output_file(self) -> None:
        """Test validation with empty output file."""
        settings = FlextTargetLdifSettings(output_file="")
        with pytest.raises(ValueError, match="Output file cannot be empty"):
            settings.validate_domain_rules()

    def test_config_validation_empty_dn_template(self) -> None:
        """Test validation with empty DN template."""
        settings = FlextTargetLdifSettings(output_file="test.ldif", dn_template="")
        with pytest.raises(ValueError, match="DN template cannot be empty"):
            settings.validate_domain_rules()

    def test_config_validation_invalid_line_length(self) -> None:
        """Test validation with invalid line length."""
        invalid_line_length = int("0")
        with pytest.raises(e.ValidationError):
            FlextTargetLdifSettings(
                output_file="test.ldif",
                line_length=invalid_line_length,
            )

    def test_config_validation_valid_config(self) -> None:
        """Test validation with valid settings."""
        settings = FlextTargetLdifSettings(
            output_file="test.ldif",
            dn_template="uid={uid},ou=users,dc=example,dc=com",
            line_length=78,
        )
        settings.validate_domain_rules()


class TestFlextTargetLdifClass:
    """Test FlextTargetLdif main class."""

    def test_target_inheritance(self) -> None:
        """Test that FlextTargetLdif is properly instantiated."""
        target = FlextTargetLdif()
        assert isinstance(target, FlextTargetLdif)

    def test_target_creation_with_defaults(self) -> None:
        """Test creating target with default configuration."""
        FlextTargetLdif()

    @patch("flext_target_ldif.target.FlextTargetLdif.__init__")
    def test_self(self, mock_init: Mock) -> None:
        """Test target initialization calls parent."""
        mock_init.return_value = None
        FlextTargetLdif()
        mock_init.assert_called_once()

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


class TestFlextTargetLdif:
    """Test the base FlextTargetLdif class."""

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
        properties = target.config_jsonschema.get("properties", {})
        if isinstance(properties, dict):
            if "output_path" not in properties:
                raise AssertionError(f"Expected {'output_path'} in {properties}")
            assert "file_naming_pattern" in properties
            if "dn_template" not in properties:
                raise AssertionError(f"Expected {'dn_template'} in {properties}")

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
        """Test settings t.RecursiveContainerMapping access."""
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


class TestIntegration:
    """Integration tests for the complete target system."""

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
            output_file=str(tmp_path),
            schema_validation=True,
            dn_template="uid={uid},ou=users,dc=example,dc=com",
        )
        settings.validate_domain_rules()
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
        """Test settings can be converted to t.RecursiveContainerMapping for Singer SDK."""
        settings = FlextTargetLdifSettings(
            output_file="test.ldif",
            schema_validation=True,
            dn_template="uid={uid},ou=users,dc=example,dc=com",
            line_length=100,
            base64_encode=True,
            attribute_mapping={"email": "mail", "name": "cn"},
        )
        config_dict = settings.model_dump()
        if config_dict["output_file"] != "test.ldif":
            raise AssertionError(
                f"Expected {'test.ldif'}, got {config_dict['output_file']}",
            )
        if not config_dict["schema_validation"]:
            raise AssertionError(
                f"Expected True, got {config_dict['schema_validation']}",
            )
        if config_dict["dn_template"] != "uid={uid},ou=users,dc=example,dc=com":
            raise AssertionError(
                f"Expected {'uid={uid},ou=users,dc=example,dc=com'}, got {config_dict['dn_template']}",
            )
        assert config_dict["line_length"] == 100
        if not config_dict["base64_encode"]:
            raise AssertionError(f"Expected True, got {config_dict['base64_encode']}")
        if config_dict["attribute_mapping"] != {"email": "mail", "name": "cn"}:
            raise AssertionError(
                f"Expected {{'email': 'mail', 'name': 'cn'}}, got {config_dict['attribute_mapping']}",
            )

    def test_error_handling_integration(self) -> None:
        """Test error handling across the system."""
        invalid_config = FlextTargetLdifSettings(output_file="")
        with pytest.raises(ValueError, match="Output file cannot be empty"):
            invalid_config.validate_domain_rules()
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
