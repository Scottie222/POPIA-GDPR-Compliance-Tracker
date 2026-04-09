"""
POPIA & GDPR Compliance Tracker — Full Run
Author: Bakithi Scott Ngcampalala
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 65)
print("  POPIA & GDPR COMPLIANCE TRACKER")
print("  WhatsApp SA 2024 | Information Regulator Enforcement")
print("=" * 65)

print("\n[1/2] Running compliance assessment...")
print("-" * 65)
from tracker.report import run_assessment
from tracker.checks import POPIA_CHECKS, GDPR_CHECKS, run_checks

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

run_assessment("WhatsApp South Africa", WHATSAPP_POPIA, WHATSAPP_GDPR)

print("\n[2/2] Generating charts...")
print("-" * 65)
from tracker.visualise import main as vis_main
vis_main()

print("\n" + "=" * 65)
print("  ALL DONE")
print("=" * 65)
print()
print("  outputs/chart-compliance-overview.png")
print("  outputs/chart-control-breakdown.png")
print("  outputs/chart-gap-analysis.png")