# Triagem SonarCloud — flext-sh/flext-target-ldif

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.21`

## Resumo

**7 issues** — BLOCKER 0, CRITICAL 2, MAJOR 4, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 3 · **Debt total: 37min**

| regra | issues |
|---|---|
| `githubactions:S8233` | 2 |
| `python:S1192` | 1 |
| `python:S3776` | 1 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🟠 CRITICAL · CODE_SMELL · `python:S1192`
**Local**: `src/flext_target_ldif/target.py:32` · **Effort**: 6min

> Define a constant instead of duplicating this literal "./output" 3 times.

```python
       28          """Initialize the LDIF target."""
       29          defaults: t.JsonMapping = {
       30              "file_naming_pattern": "{stream_name}_{timestamp}.ldif",
       31              "dn_template": "uid={uid},ou=users,dc=example,dc=com",
>>>    32              "output_path": "./output",
       33          }
       34          # NOTE (multi-agent): mro-rn88 — persist the merged config on the instance so
       35          # get_sink/validate_config read self._config (was an undefined bare `settings`).
       36          self._config: t.JsonMapping = {**defaults, **(settings or {})}
```

**Decisão**: pendente

### 2 · 🟠 CRITICAL · CODE_SMELL · `python:S3776`
**Local**: `src/flext_target_ldif/utilities.py:70` · **Effort**: 6min

> Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed.

```python
       66                  except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
       67                      return r[str].fail(f"Error building DN: {exc}")
       68  
       69              @staticmethod
>>>    70              def convert_record_to_ldif_entry(
       71                  record: t.JsonMapping,
       72                  dn: str,
       73                  object_classes: t.StrSequence | None = None,
       74                  attribute_mapping: t.StrMapping | None = None,
```

**Decisão**: pendente

### 3 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: pendente

### 4 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: pendente

### 5 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: pendente

### 6 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.

**Decisão**: pendente

### 7 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: pendente
