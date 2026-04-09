"""
POPIA & GDPR Compliance Tracker — Visualisation
Generates PNG charts from assessment results
Author: Bakithi Scott Ngcampalala
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from tracker.checks import (
    POPIA_CHECKS, GDPR_CHECKS,
    run_checks, calculate_score, get_compliance_level
)

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

WHATSAPP_POPIA = {
    "POPIA-1": "no", "POPIA-2": "no", "POPIA-3": "no",
    "POPIA-4": "no", "POPIA-5": "yes", "POPIA-6": "yes",
    "POPIA-7": "no", "POPIA-8": "no"
}
WHATSAPP_GDPR = {
    "GDPR-1": "yes", "GDPR-2": "yes", "GDPR-3": "no",
    "GDPR-4": "no", "GDPR-5": "yes", "GDPR-6": "no",
    "GDPR-7": "no", "GDPR-8": "no", "GDPR-9": "no", "GDPR-10": "no"
}

def chart_compliance_overview():
    popia_results = run_checks(WHATSAPP_POPIA, POPIA_CHECKS)
    gdpr_results = run_checks(WHATSAPP_GDPR, GDPR_CHECKS)
    popia_score, popia_pass, popia_total = calculate_score(popia_results)
    gdpr_score, gdpr_pass, gdpr_total = calculate_score(gdpr_results)
    overall = round((popia_score + gdpr_score) / 2, 1)

    fig, axes = plt.subplots(1, 3, figsize=(13, 5))
    fig.patch.set_facecolor("#ffffff")

    for ax, label, score, passed, total, color in [
        (axes[0], "POPIA", popia_score, popia_pass, popia_total, "#E24B4A"),
        (axes[1], "GDPR", gdpr_score, gdpr_pass, gdpr_total, "#EF9F27"),
        (axes[2], "Overall", overall, None, None, "#378ADD"),
    ]:
        theta = np.linspace(0, 2 * np.pi, 100)
        ax.set_facecolor("#f8f7f2")
        ax.pie(
            [score, 100 - score],
            colors=[color, "#e0dfd8"],
            startangle=90,
            wedgeprops={"width": 0.4, "edgecolor": "white"}
        )
        ax.text(0, 0, f"{score}%", ha="center", va="center",
                fontsize=18, fontweight="bold", color=color)
        ax.set_title(label, fontsize=13, fontweight="bold", pad=12)
        level = get_compliance_level(score)
        ax.text(0, -1.35, level, ha="center", fontsize=9,
                color="#888780", wrap=True)
        if passed is not None:
            ax.text(0, 1.25, f"{passed}/{total} passed", ha="center",
                    fontsize=9, color="#5F5E5A")

    plt.suptitle("POPIA & GDPR Compliance — WhatsApp SA 2024",
                 fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "chart-compliance-overview.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {path}")

def chart_control_breakdown():
    popia_results = run_checks(WHATSAPP_POPIA, POPIA_CHECKS)
    gdpr_results = run_checks(WHATSAPP_GDPR, GDPR_CHECKS)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor("#ffffff")

    for ax, results, title, color in [
        (axes[0], popia_results, "POPIA Controls", "#E24B4A"),
        (axes[1], gdpr_results, "GDPR Controls", "#EF9F27"),
    ]:
        labels = [r["id"] for r in results]
        values = [1 if r["passed"] else 0 for r in results]
        colors = [color if v else "#e0dfd8" for v in values]

        bars = ax.barh(labels, [1] * len(labels), color=colors,
                       edgecolor="white", height=0.6)
        for i, r in enumerate(results):
            status = "PASS" if r["passed"] else "FAIL"
            ax.text(0.02, i, f"{r['article']} — {r['requirement'][:45]}",
                    va="center", fontsize=8, color="#2c2c2a")
            ax.text(0.97, i, status, va="center", ha="right",
                    fontsize=8, fontweight="bold",
                    color="white" if r["passed"] else "#888780")

        ax.set_xlim(0, 1)
        ax.set_facecolor("#f8f7f2")
        ax.set_title(title, fontsize=12, fontweight="bold", pad=10)
        ax.axis("off")
        passed = sum(values)
        ax.text(0.5, -0.8, f"{passed}/{len(results)} controls passed",
                ha="center", fontsize=10, color="#5F5E5A",
                transform=ax.transAxes)

    plt.suptitle("Control-by-Control Assessment — WhatsApp SA 2024",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "chart-control-breakdown.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {path}")

def chart_gap_analysis():
    popia_results = run_checks(WHATSAPP_POPIA, POPIA_CHECKS)
    gdpr_results = run_checks(WHATSAPP_GDPR, GDPR_CHECKS)
    all_results = popia_results + gdpr_results
    failed = [r for r in all_results if not r["passed"]]

    fig, ax = plt.subplots(figsize=(12, max(5, len(failed) * 0.55 + 1)))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#f8f7f2")

    labels = [f"{r['id']} — {r['article']}" for r in failed]
    colors = ["#E24B4A" if r["id"].startswith("POPIA") else "#EF9F27"
              for r in failed]

    ax.barh(labels, [1] * len(failed), color=colors,
            edgecolor="white", height=0.6, alpha=0.85)
    for i, r in enumerate(failed):
        ax.text(0.02, i, r["requirement"][:70],
                va="center", fontsize=8, color="#2c2c2a")

    ax.set_xlim(0, 1.3)
    ax.axis("off")
    ax.set_title(f"Gap Analysis — {len(failed)} Failed Controls",
                 fontsize=13, fontweight="bold", pad=12)

    legend = [
        mpatches.Patch(color="#E24B4A", label="POPIA failures"),
        mpatches.Patch(color="#EF9F27", label="GDPR failures"),
    ]
    ax.legend(handles=legend, fontsize=9, loc="lower right")
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "chart-gap-analysis.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {path}")

def main():
    print("=" * 65)
    print("  POPIA & GDPR COMPLIANCE TRACKER — VISUALISATION")
    print("  WhatsApp SA 2024 Enforcement Case Study")
    print("=" * 65)
    print("\n  Generating charts...")
    chart_compliance_overview()
    chart_control_breakdown()
    chart_gap_analysis()
    print(f"\n  All charts saved to outputs/")

if __name__ == "__main__":
    main()