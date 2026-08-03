# AGENTS.md — flext-target-ldif

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_target_ldif` · deps: `flext-core`, `flext-ldif`, `flext-meltano`, `flext-observability`

## Overview

Singer **target** (loader) writing LDIF output. Thin driver over `flext-meltano` (ADR-006), delegating serialization to `flext-ldif`.

## Structure

```text
src/flext_target_ldif/
├── api.py            # FlextTargetLdifService(FlextMeltanoTargetServiceBase)
├── target.py         # FlextTargetLdif — config merge, output-dir creation, sink selection
├── writer.py         # LDIF writer (serialization)
├── cli.py errors.py
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
└── _utilities/
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextTargetLdifService` | class | `api.py` | `FlextMeltanoTargetServiceBase` |
| `FlextTargetLdif` | class | `target.py` | config merge + sink selection |
| writer | module | `writer.py` | LDIF serialization (delegates to `flext-ldif`) |

## Anti-Patterns / Gotchas

- `target.py` persists merged settings in `self._config`; **sink/config code must not read an unbound bare `settings`** (a known settings-fallout bug pattern).

## Commands

```bash
make check PROJECT=flext-target-ldif
make test  PROJECT=flext-target-ldif       # tests/unit
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
