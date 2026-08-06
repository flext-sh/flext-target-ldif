# Triagem SonarCloud — flext-sh/flext-target-ldif

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.21`

## Resumo

**7 issues** — BLOCKER 0, CRITICAL 2, MAJOR 4, MINOR 1
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 3

| regra | issues |
|---|---|
| `githubactions:S8233` | 2 |
| `python:S1192` | 1 |
| `python:S3776` | 1 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_target_ldif/target.py` | 32 | |
| 2 | CRITICAL | CODE_SMELL | `python:S3776` | `src/flext_target_ldif/utilities.py` | 70 | |
| 3 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 4 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 5 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 6 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 7 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-target-ldif.json`

