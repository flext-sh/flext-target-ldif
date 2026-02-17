# FLEXT-Target-LDIF

[![Singer SDK](https://img.shields.io/badge/singer--sdk-compliant-brightgreen.svg)](https://sdk.meltano.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-Target-LDIF** allows you to export Singer streams directly to LDIF (LDAP Data Interchange Format) files. It serves as a bridge for scenarios requiring offline data loading or migrations to LDAP-compliant systems.

Part of the [FLEXT](https://github.com/flext/flext) ecosystem.

## 🚀 Key Features

- **LDIF Generation**: Produces strictly compliant LDIF files suitable for `ldapadd` and `ldapmodify` tools.
- **Flexible Output**: Supports rotation, compression (gzip), and custom file naming patterns.
- **Schema Transformation**: Maps relational data streams to hierarchical LDAP structures.
- **High Performance**: Buffered writing and batching options for handling large datasets efficiently.
- **Format Options**: Configurable line wrapping, base64 encoding rules, and operational comments.

## 📦 Installation

Install via Poetry:

```bash
poetry add flext-target-ldif
```

## 🛠️ Usage

### Usage with Meltano

Configure the target in your `meltano.yml`:

```yaml
loaders:
  - name: target-ldif
    pip_url: flext-target-ldif
    config:
      output_path: ./exports
      file_naming_pattern: "{stream_name}_{date}.ldif"
      dn_template: "uid={id},ou=people,dc=example,dc=com"
```

### CLI Execution

Pipe streams to generate LDIF files:

```bash
tap-postgres --config pg_config.json | target-ldif --config ldif_config.json
```

### Configuration Example

Control every aspect of the output:

```json
{
  "output_path": "/data/exports",
  "compression": "gzip",
  "ldif_options": {
      "line_length": 78,
      "base64_encode": false,
      "sort_attributes": true
  },
  "stream_maps": {
      "users": {
          "attribute_mapping": {
              "id": "uid",
              "full_name": "cn"
          },
          "object_classes": ["inetOrgPerson"]
      }
  }
}
```

## 🏗️ Architecture

Built on the Singer SDK, ensuring standard compliance:

- **File Writer**: Efficient, configurable engine for writing structured text files.
- **Transformation Layer**: Applies complex rules to reshaping flat records into LDAP entries.
- **Validation**: Built-in checks ensure generated LDIFs are syntactically correct.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on adding new format options.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
