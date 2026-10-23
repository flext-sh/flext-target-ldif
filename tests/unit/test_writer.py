"""Comprehensive tests for FlextTargetLdifWriter implementation.

REFACTORED: Complete writer system with 100% coverage and validation.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
import tempfile
from pathlib import Path
from typing import Final

import pytest

from flext_target_ldif.errors import FlextTargetLdifWriterError
from flext_target_ldif.writer import FlextTargetLdifWriter
from tests import c, tm

EXPECTED_WRAPPED_LINE_LENGTH: Final[int] = 20
CUSTOM_LINE_LENGTH: Final[int] = 100


@pytest.mark.usefixtures("isolate_working_directory")
class TestsFlextTargetLdifWriter:
    """Test FlextTargetLdifWriter initialization."""

    @staticmethod
    def test_init_with_string_path() -> None:
        """Test initialization with string path."""
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = f"{temp_dir}/test.ldif"
            writer = FlextTargetLdifWriter(output_file=test_file)
            if writer.output_file != Path(test_file):
                msg = f"Expected {Path(test_file)}, got {writer.output_file}"
                tm.reject(msg)

    @staticmethod
    def test_open_success(tmp_path: Path) -> None:
        """Test successful file opening."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        result = writer.open()
        tm.ok(result)
        close_result = writer.close()
        tm.ok(close_result)

    @staticmethod
    def test_open_failure() -> None:
        """Test file opening failure."""
        invalid_path = Path("/nonexistent/directory/test.ldif")
        writer = FlextTargetLdifWriter(output_file=invalid_path)
        result = writer.open()
        tm.fail(result)
        if result.error is not None and "Failed to open LDIF file" not in result.error:
            msg = f"Expected {'Failed to open LDIF file'} in {result.error}"
            tm.reject(msg)

    @staticmethod
    def test_close_success(tmp_path: Path) -> None:
        """Test successful file closing."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        writer.open()
        result = writer.close()
        tm.ok(result)

    @staticmethod
    def test_close_when_not_open() -> None:
        """Test closing when file is not open."""
        writer = FlextTargetLdifWriter()
        result = writer.close()
        tm.ok(result)

    # NOTE (multi-agent): no-mock rewrite — close() failure is exercised through a
    # REAL filesystem failure (output directory made unwritable) instead of the old
    # patched pathlib.Path.open returning a Mock whose close() raised.
    @staticmethod
    def test_close_failure_when_output_directory_unwritable(
        tmp_path: Path,
    ) -> None:
        """close() reports failure when the output directory is not writable."""
        readonly_dir = tmp_path / "readonly"
        readonly_dir.mkdir()
        writer = FlextTargetLdifWriter(output_file=readonly_dir / "out.ldif")
        readonly_dir.chmod(0o555)
        try:
            result = writer.close()
        finally:
            readonly_dir.chmod(0o755)
        tm.fail(result)
        if result.error is not None and "Failed to close LDIF file" not in result.error:
            msg = f"Expected {'Failed to close LDIF file'} in {result.error}"
            tm.reject(msg)

    @staticmethod
    def test_custom_dn_template() -> None:
        """Test custom DN template."""
        writer = FlextTargetLdifWriter(dn_template="cn={name},ou=people,dc=test,dc=org")
        record = {"name": "John Doe"}
        dn = writer.generate_dn(record)
        if dn != "cn=John Doe,ou=people,dc=test,dc=org":
            msg = f"Expected {'cn=John Doe,ou=people,dc=test,dc=org'}, got {dn}"
            tm.reject(msg)

    @staticmethod
    def test_context_manager_usage(tmp_path: Path) -> None:
        """Test using FlextTargetLdifWriter as context manager."""
        output_file = tmp_path / "test.ldif"
        record = {"uid": "jdoe", "cn": "John Doe"}
        with FlextTargetLdifWriter(output_file=output_file) as writer:
            result = writer.write_record(record)
            tm.ok(result)
            tm.that(writer.record_count, eq=1)
        tm.that(writer.record_count, eq=1)
        content = output_file.read_text(encoding="utf-8")
        if "dn: uid=jdoe,ou=users,dc=example,dc=com" not in content:
            msg: str = (
                f"Expected {'dn: uid=jdoe,ou=users,dc=example,dc=com'} in {content}"
            )
            tm.reject(msg)

    @staticmethod
    def test_context_manager_exception_handling(tmp_path: Path) -> None:
        """Test context manager properly closes file on exception."""
        output_file = tmp_path / "test.ldif"

        def _raise_test_exception() -> None:
            msg = "Test exception"
            raise ValueError(msg)

        writer_holder: list[FlextTargetLdifWriter] = []

        def _write_then_raise() -> None:
            with FlextTargetLdifWriter(output_file=output_file) as ctx_writer:
                writer_holder.append(ctx_writer)
                ctx_writer.write_record({"uid": "jdoe", "cn": "John Doe"})
                _raise_test_exception()

        with pytest.raises(ValueError, match="Test exception"):
            _write_then_raise()
        writer = writer_holder[0]
        tm.that(writer.record_count, eq=1)
        tm.that(output_file.read_text(encoding="utf-8"), has="uid: jdoe")

    @staticmethod
    def test_record_count_property(tmp_path: Path) -> None:
        """Test record_count property."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        tm.that(writer.record_count, eq=0)
        writer.write_record({"uid": "user1", "cn": "User One"})
        tm.that(writer.record_count, eq=1)
        writer.write_record({"uid": "user2", "cn": "User Two"})
        tm.that(writer.record_count, eq=c.TargetLdif.Tests.EXPECTED_BULK_SIZE)
        writer.close()

    @staticmethod
    def test_record_count_after_close(tmp_path: Path) -> None:
        """Test record_count persists after close."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        writer.write_record({"uid": "user1", "cn": "User One"})
        writer.close()
        if writer.record_count != 1:
            msg = f"Expected {1}, got {writer.record_count}"
            tm.reject(msg)


@pytest.mark.usefixtures("isolate_working_directory")
class TestsFlextTargetLdifWriterOutput:
    """Writer output formatting tests: DN generation, folding, and encoding."""

    @staticmethod
    def test_init_with_defaults() -> None:
        """Test initialization with default values."""
        writer = FlextTargetLdifWriter()
        if writer.output_file != Path("output.ldif"):
            msg = f"Expected {Path('output.ldif')}, got {writer.output_file}"
            tm.reject(msg)
        tm.that(writer.ldif_options, eq={})
        expected_dn = "uid={uid},ou=users,dc=example,dc=com"
        if writer.dn_template != expected_dn:
            msg = f"Expected {expected_dn!r}, got {writer.dn_template}"
            tm.reject(msg)
        tm.that(writer.attribute_mapping, eq={})
        if writer.schema != {}:
            msg = f"Expected {{}}, got {writer.schema}"
            tm.reject(msg)
        tm.that(writer.line_length, eq=78)
        if writer.base64_encode:
            msg = f"Expected False, got {writer.base64_encode}"
            tm.reject(msg)
        if not writer.include_timestamps:
            msg = f"Expected True, got {writer.include_timestamps}"
            tm.reject(msg)

    @staticmethod
    def test_init_with_custom_values() -> None:
        """Test initialization with custom values."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "custom.ldif"
            ldif_options = {
                "line_length": 100,
                "base64_encode": True,
                "include_timestamps": False,
            }
            dn_template = "cn={name},ou=people,dc=test,dc=com"
            attribute_mapping = {"email": "mail", "name": "cn"}
            schema = {"objectClass": ["person", "organizationalPerson"]}
            writer = FlextTargetLdifWriter(
                output_file=output_file,
                ldif_options=ldif_options,
                dn_template=dn_template,
                attribute_mapping=attribute_mapping,
                schema=schema,
            )
            if writer.output_file != output_file:
                msg = f"Expected {output_file}, got {writer.output_file}"
                tm.reject(msg)
            tm.that(writer.ldif_options, eq=ldif_options)
            if writer.dn_template != dn_template:
                msg = f"Expected {dn_template}, got {writer.dn_template}"
                tm.reject(msg)
            tm.that(writer.attribute_mapping, eq=attribute_mapping)
            if writer.schema != schema:
                msg = f"Expected {schema}, got {writer.schema}"
                tm.reject(msg)
            tm.that(writer.line_length, eq=100)
            if not writer.base64_encode:
                msg = f"Expected True, got {writer.base64_encode}"
                tm.reject(msg)
            if writer.include_timestamps:
                msg = f"Expected False, got {writer.include_timestamps}"
                tm.reject(msg)

    @staticmethod
    def test_write_simple_record(tmp_path: Path) -> None:
        """Test writing a simple record."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        record = {"uid": "jdoe", "cn": "John Doe", "mail": "john@example.com"}
        result = writer.write_record(record)
        tm.ok(result)
        if writer.record_count != 1:
            msg = f"Expected {1}, got {writer.record_count}"
            tm.reject(msg)
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        if "version: 1" not in content:
            msg = f"Expected {'version: 1'} in {content}"
            tm.reject(msg)
        tm.that(content, has="dn: uid=jdoe,ou=users,dc=example,dc=com")
        if "uid: jdoe" not in content:
            msg = f"Expected {'uid: jdoe'} in {content}"
            tm.reject(msg)
        tm.that(content, has="cn: John Doe")
        if "mail: john@example.com" not in content:
            msg = f"Expected {'mail: john@example.com'} in {content}"
            tm.reject(msg)

    @staticmethod
    def test_write_record_with_attribute_mapping(tmp_path: Path) -> None:
        """Test writing record with attribute mapping."""
        attribute_mapping = {"email": "mail", "name": "cn"}
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(
            output_file=output_file,
            attribute_mapping=attribute_mapping,
        )
        record = {"uid": "jdoe", "name": "John Doe", "email": "john@example.com"}
        writer.write_record(record)
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        if "cn: John Doe" not in content:
            msg = f"Expected {'cn: John Doe'} in {content}"
            tm.reject(msg)
        tm.that(content, has="mail: john@example.com")

    @staticmethod
    def test_write_record_auto_open(tmp_path: Path) -> None:
        """Test that write_record automatically opens file if not open."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        record = {"uid": "jdoe", "cn": "John Doe"}
        result = writer.write_record(record)
        tm.ok(result)
        tm.that(writer.record_count, eq=1)
        writer.close()

    @staticmethod
    def test_write_record_missing_dn_field() -> None:
        """Test writing record with missing DN field."""
        writer = FlextTargetLdifWriter(
            dn_template="uid={uid},ou=users,dc=example,dc=com",
        )
        record = {"cn": "John Doe", "mail": "john@example.com"}
        result = writer.write_record(record)
        tm.fail(result)
        if result.error is not None and "Failed to write record" not in result.error:
            msg = f"Expected {'Failed to write record'} in {result.error}"
            tm.reject(msg)

    @staticmethod
    def test_write_multiple_records(tmp_path: Path) -> None:
        """Test writing multiple records."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        records = [
            {"uid": "jdoe", "cn": "John Doe"},
            {"uid": "jsmith", "cn": "Jane Smith"},
            {"uid": "bob", "cn": "Bob Wilson"},
        ]
        for record in records:
            result = writer.write_record(record)
            tm.ok(result)
        if writer.record_count != c.TargetLdif.Tests.EXPECTED_DATA_COUNT:
            msg = f"Expected {3}, got {writer.record_count}"
            tm.reject(msg)
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        if "dn: uid=jdoe,ou=users,dc=example,dc=com" not in content:
            msg = f"Expected {'dn: uid=jdoe,ou=users,dc=example,dc=com'} in {content}"
            tm.reject(msg)
        tm.that(content, has="dn: uid=jsmith,ou=users,dc=example,dc=com")
        if "dn: uid=bob,ou=users,dc=example,dc=com" not in content:
            msg = f"Expected {'dn: uid=bob,ou=users,dc=example,dc=com'} in {content}"
            tm.reject(msg)

    @staticmethod
    def testneeds_base64_encoding_space_start() -> None:
        """Test detection of values that start with space."""
        writer = FlextTargetLdifWriter()
        tm.that(writer.needs_base64_encoding(" starts with space"))

    @staticmethod
    def testneeds_base64_encoding_colon_start() -> None:
        """Test detection of values that start with colon."""
        writer = FlextTargetLdifWriter()
        tm.that(writer.needs_base64_encoding(":starts with colon"))

    @staticmethod
    def testneeds_base64_encoding_non_ascii() -> None:
        """Test detection of non-ASCII values."""
        writer = FlextTargetLdifWriter()
        tm.that(writer.needs_base64_encoding("José"))
        tm.that(writer.needs_base64_encoding("中文"))

    @staticmethod
    def testneeds_base64_encoding_newlines() -> None:
        """Test detection of values with newlines."""
        writer = FlextTargetLdifWriter()
        tm.that(writer.needs_base64_encoding("line1\nline2"))
        tm.that(writer.needs_base64_encoding("line1\rline2"))

    @staticmethod
    def testneeds_base64_encoding_normal_value() -> None:
        """Test normal ASCII values don't need encoding."""
        writer = FlextTargetLdifWriter()
        tm.that(writer.needs_base64_encoding("normal ascii value"), eq=False)
        tm.that(writer.needs_base64_encoding("john@example.com"), eq=False)

    @staticmethod
    def test_write_base64_encoded_attribute(tmp_path: Path) -> None:
        """Test writing base64 encoded attributes."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        writer.open()
        writer.write_attribute("description", " starts with space")
        writer.write_attribute("cn", "José")
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        if "description:: " not in content:
            msg = f"Expected {'description:: '} in {content}"
            tm.reject(msg)
        tm.that(content, has="cn:: ")
        for line in content.split("\n"):
            if line.startswith("description:: "):
                encoded = line.split(":: ")[1]
                decoded = base64.b64decode(encoded).decode("utf-8")
                if decoded != " starts with space":
                    msg = f"Expected {' starts with space'}, got {decoded}"
                    tm.reject(msg)
            elif line.startswith("cn:: "):
                encoded = line.split(":: ")[1]
                decoded = base64.b64decode(encoded).decode("utf-8")
                if decoded != "José":
                    msg = f"Expected {'José'}, got {decoded}"
                    tm.reject(msg)

    @staticmethod
    def test_force_base64_encoding(tmp_path: Path) -> None:
        """Test forcing base64 encoding via options."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(
            output_file=output_file,
            ldif_options={"base64_encode": True},
        )
        record = {"uid": "jdoe", "cn": "John Doe"}
        writer.write_record(record)
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        if "uid:: " not in content:
            msg = f"Expected {'uid:: '} in {content}"
            tm.reject(msg)
        tm.that(content, has="cn:: ")

    @staticmethod
    def test_short_line_no_wrapping(tmp_path: Path) -> None:
        """Test short lines are not wrapped."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(output_file=output_file)
        writer.open()
        writer.write_line("short line")
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        lines = content.strip().split("\n")
        if "short line" not in lines:
            msg = f"Expected {'short line'} in {lines}"
            tm.reject(msg)

    @staticmethod
    def test_long_line_wrapping(tmp_path: Path) -> None:
        """Test long lines are properly wrapped."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(
            output_file=output_file,
            ldif_options={"line_length": 20},
        )
        writer.open()
        long_line = (
            "this is a very long line that should be wrapped and exceed "
            "the 20 character limit"
        )
        writer.write_line(long_line)
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        lines = content.strip().split("\n")
        wrapped_lines = [
            line
            for line in lines
            if not line.startswith("version:") and (not line.startswith("# Generated"))
        ]
        wrapped_lines = [line for line in wrapped_lines if line.strip()]
        if wrapped_lines:
            expected_len = EXPECTED_WRAPPED_LINE_LENGTH
            if len(wrapped_lines[0]) != expected_len:
                msg = f"Expected {expected_len}, got {len(wrapped_lines[0])}"
                tm.reject(msg)
            for line in wrapped_lines[1:]:
                if line:
                    tm.that(line.startswith(" "))

    @staticmethod
    def test_custom_line_length() -> None:
        """Test custom line length setting."""
        writer = FlextTargetLdifWriter(ldif_options={"line_length": CUSTOM_LINE_LENGTH})
        expected_len = CUSTOM_LINE_LENGTH
        if writer.line_length != expected_len:
            msg = f"Expected {expected_len}, got {writer.line_length}"
            tm.reject(msg)

    @staticmethod
    def test_header_with_timestamps(tmp_path: Path) -> None:
        """Test header generation with timestamps."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(
            output_file=output_file,
            ldif_options={"include_timestamps": True},
        )
        writer.open()
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        if "version: 1" not in content:
            msg = f"Expected {'version: 1'} in {content}"
            tm.reject(msg)
        tm.that(content, has="# Generated on:")

    @staticmethod
    def test_header_without_timestamps(tmp_path: Path) -> None:
        """Test header generation without timestamps."""
        output_file = tmp_path / "test.ldif"
        writer = FlextTargetLdifWriter(
            output_file=output_file,
            ldif_options={"include_timestamps": False},
        )
        writer.open()
        writer.close()
        content = output_file.read_text(encoding="utf-8")
        if "version: 1" not in content:
            msg = f"Expected {'version: 1'} in {content}"
            tm.reject(msg)
        tm.that(content, lacks="# Generated on:")


@pytest.mark.usefixtures("isolate_working_directory")
class TestsFlextTargetLdifWriterDn:
    """DN generation tests for the LDIF writer."""

    @staticmethod
    def testgenerate_dn_success() -> None:
        """Test successful DN generation."""
        writer = FlextTargetLdifWriter(
            dn_template="uid={uid},ou={department},dc=example,dc=com",
        )
        record = {"uid": "jdoe", "department": "engineering"}
        dn = writer.generate_dn(record)
        if dn != "uid=jdoe,ou=engineering,dc=example,dc=com":
            msg: str = (
                f"Expected {'uid=jdoe,ou=engineering,dc=example,dc=com'}, got {dn}"
            )
            tm.reject(msg)

    @staticmethod
    def testgenerate_dn_missing_field() -> None:
        """Test DN generation with missing field."""
        writer = FlextTargetLdifWriter(
            dn_template="uid={uid},ou={department},dc=example,dc=com",
        )
        record = {"uid": "jdoe"}
        with pytest.raises(FlextTargetLdifWriterError) as exc_info:
            writer.generate_dn(record)
        if "Missing required field for DN generation" not in str(exc_info.value):
            expected = "Missing required field for DN generation"
            msg = f"Expected {expected!r} in {exc_info.value!s}"
            tm.reject(msg)
