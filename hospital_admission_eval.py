#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hospital-admission-eval — Procurement admission decision support: license check + health economics.
医院采购准入评估：证照校验 + 卫生经济学粗算。Zero-dependency."""
import argparse, hashlib, json, sys
from datetime import date

TOOL_VERSION = "0.1.0"

def license_check(reg_cert, prod_license, biz_license, reg_expiry, today=None):
    exp = date.fromisoformat(reg_expiry)
    today = date.fromisoformat(today) if today else date.today()
    problems = []
    if not reg_cert:
        problems.append("registration certificate missing")
    if not prod_license:
        problems.append("production license missing")
    if not biz_license:
        problems.append("business license missing")
    if (exp - today).days < 0:
        problems.append("registration expired")
    return {"ok": len(problems) == 0, "problems": problems,
            "decision_id": "adm-" + hashlib.sha256((reg_cert or "x").encode()).hexdigest()[:10]}

def heco_rough(price_cny, annual_volume, expected_life_years, reoperation_rate):
    if price_cny < 0 or annual_volume < 0 or expected_life_years <= 0 or not 0 <= reoperation_rate <= 1:
        return {"ok": False, "error": "invalid economics inputs"}
    total = price_cny * annual_volume
    cost_per_patient_year = price_cny / expected_life_years
    reop_cost = total * reoperation_rate
    return {"ok": True, "annual_total_cny": round(total, 2),
            "cost_per_patient_year_cny": round(cost_per_patient_year, 2),
            "reoperation_cost_cny": round(reop_cost, 2),
            "verdict": "high-cost" if cost_per_patient_year > 5000 else "acceptable"}

def admission_verdict(license_result, heco_result):
    if not license_result.get("ok"):
        return {"admit": False, "reason": "license check failed"}
    if heco_result.get("verdict") == "high-cost":
        return {"admit": "conditional", "reason": "high cost per patient-year — require budget approval"}
    return {"admit": True, "reason": "license valid, economics acceptable"}

def run_selftest():
    checks = []
    r = license_check("NMPA-2024-001", "P-01", "B-01", "2027-12-31")
    c1 = r["ok"] is True
    checks.append(("positive: complete valid licenses", c1))
    r2 = license_check("", "P-01", "B-01", "2027-12-31")
    c2 = r2["ok"] is False and "registration certificate missing" in r2["problems"]
    checks.append(("negative: missing registration rejected", c2))
    c3 = heco_rough(-1, 10, 5, 0.1)["ok"] is False
    checks.append(("negative: negative price rejected", c3))
    c4 = heco_rough(100000, 10, 5, 0.1)["verdict"] == "high-cost"
    checks.append(("positive: 100k/5y > 5k threshold flags high-cost", c4))
    for name, ok in checks:
        print("[selftest] %s PASS" % name if ok else "[selftest] %s FAIL" % name)
    return 0 if all(ok for _, ok in checks) else 1

def run_demo():
    print("=== hospital-admission-eval demo (v%s) ===" % TOOL_VERSION)
    lc = license_check("NMPA-2024-001", "P-01", "B-01", "2027-12-31")
    print("[LICENSE] " + json.dumps(lc, ensure_ascii=False))
    he = heco_rough(50000, 20, 5, 0.05)
    print("[HECO]    " + json.dumps(he, ensure_ascii=False))
    print("[VERDICT] " + json.dumps(admission_verdict(lc, he), ensure_ascii=False))
    return 0

def main():
    ap = argparse.ArgumentParser(description="Procurement admission evaluation (license + health economics)")
    ap.add_argument("--check", action="store_true", help="license check")
    ap.add_argument("--heco", action="store_true", help="health-economics rough estimate")
    ap.add_argument("--verdict", action="store_true", help="combined admission verdict")
    ap.add_argument("--json", metavar="PAYLOAD", help="JSON payload")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(run_selftest())
    if args.demo:
        sys.exit(run_demo())
    if not args.json:
        print("requires --json payload", file=sys.stderr); sys.exit(2)
    d = json.loads(args.json)
    if args.check:
        print(json.dumps(license_check(d["reg_cert"], d["prod_license"], d["biz_license"], d["reg_expiry"], d.get("today")), ensure_ascii=False)); sys.exit(0)
    if args.heco:
        print(json.dumps(heco_rough(d["price_cny"], d["annual_volume"], d["expected_life_years"], d["reoperation_rate"]), ensure_ascii=False)); sys.exit(0)
    if args.verdict:
        lc = license_check(d["reg_cert"], d["prod_license"], d["biz_license"], d["reg_expiry"], d.get("today"))
        he = heco_rough(d["price_cny"], d["annual_volume"], d["expected_life_years"], d["reoperation_rate"])
        print(json.dumps(admission_verdict(lc, he), ensure_ascii=False)); sys.exit(0)
    ap.print_help(); sys.exit(2)

if __name__ == "__main__":
    main()
