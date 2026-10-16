<div align="center">

# hospital-admission-eval

**Procurement admission decision support: license checks (registration/production/business) + health-economics rough estimate. Zero-dependency Python CLI.** · 采购准入评估：证照校验（注册证/生产/经营）+ 卫生经济学粗算。零依赖 Python CLI。

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Scorecard](https://api.scorecard.dev/projects/github.com/stevenzhao07/hospital-admission-eval/badge)](https://scorecard.dev)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![Zero-Dep](https://img.shields.io/badge/dependencies-zero-green.svg)](module.json)

*Part of the MedXpert medical-device value-chain toolkit · segment: hospital*
*MedXpert 医械全产业链工具链 · hospital 模块*

</div>

---

## Positioning · 定位

**Hospital-side full-lifecycle · zero-dependency · AI-readable contract**

Part of the **33-module MedXpert medical-device value-chain toolkit** — the only
hospital-side suite combining full-lifecycle coverage, zero runtime dependencies,
and an AI-readable layer (`module.json` / `AGENTS.md` / `llms.txt`).

医院端全生命周期 × 零依赖 × AI 可读层：33 模块 MedXpert 医械全产业链工具链的医院端模块，
唯一同时具备全生命周期覆盖、零运行时依赖与 AI 可读契约（module.json / AGENTS.md / llms.txt）的套件。


## Overview · 总览

License validation (3 certs + expiry), per-patient-year cost with high-cost threshold, combined admission verdict.

本工具零依赖（纯标准库）、自带自测与演示，输出机器可读 JSON 与人读报告。

## Quick start · 快速上手

```bash
python hospital_admission_eval.py --selftest
python hospital_admission_eval.py --demo
```

| Command | Description |
|---|---|
| `selftest` | python hospital_admission_eval.py --selftest |
| `demo` | python hospital_admission_eval.py --demo |
| `check` | python hospital_admission_eval.py --check --json '<licenses>' |
| `heco` | python hospital_admission_eval.py --heco --json '<economics>' |
| `verdict` | python hospital_admission_eval.py --verdict --json '<both>' |

## AI-readable contract · AI 可读契约
| Artifact | What it gives an AI agent / 给 AI 什么 |
|---|---|
| `module.json` | lgd-skeleton module contract: scope, commands, exit codes, A1/A2/A3 flags |
| `AGENTS.md` | when to use, command contract, data model, privacy, interop |
| `llms.txt` | one-screen LLM summary + protocol + commands |

Every decision record carries A1 authority scope / A2 human-oversight flag / A3 accountability id (LGD convention).

## Security & quality · 安全与质量
- OpenSSF Scorecard supply-chain scoring (weekly CI + per push)
- CodeQL SAST · Dependabot weekly updates · SECURITY.md private-advisory policy
- `--selftest` guards regressions with negative controls

## License · 许可
[Apache-2.0](LICENSE)
