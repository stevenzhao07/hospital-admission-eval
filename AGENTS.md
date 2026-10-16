# AGENTS.md — Instructions for AI agents / AI 智能体使用指南

## What this repo is / 这是什么
`hospital-admission-eval` — 采购准入评估：证照校验（注册证/生产/经营）+ 卫生经济学粗算。零依赖 Python CLI。
Part of the MedXpert medical-device value-chain toolkit (owner: stevenzhao07),
segment: **hospital**. Zero-dependency Python CLI.

## When to use / 何时使用
License validation (3 certs + expiry), per-patient-year cost with high-cost threshold, combined admission verdict.

## Command contract / 命令契约
| Command | Purpose |
|---|---|
| `selftest` | python hospital_admission_eval.py --selftest |
| `demo` | python hospital_admission_eval.py --demo |
| `check` | python hospital_admission_eval.py --check --json '<licenses>' |
| `heco` | python hospital_admission_eval.py --heco --json '<economics>' |
| `verdict` | python hospital_admission_eval.py --verdict --json '<both>' |

## A1/A2/A3 convention (LGD decision-record) / 决策记录约定
- A1 authority scope: `check, heco, verdict`
- A2 human oversight: flag on write paths
- A3 accountability: deterministic decision ids + actor field

## Build / test / demo / 构建测试演示
```bash
python hospital_admission_eval.py --selftest   # >=4 assertions incl. negative controls, exit 0 = green
python hospital_admission_eval.py --demo       # end-to-end, machine + human readable
```
Zero dependencies (stdlib only). No install step.
