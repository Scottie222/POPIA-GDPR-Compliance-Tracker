from tracker.checks import (
    POPIA_CHECKS, GDPR_CHECKS,
    run_checks, calculate_score, get_compliance_level
)


def run_assessment(company_name, popia_responses, gdpr_responses):
    print("")
    print("POPIA AND GDPR COMPLIANCE ASSESSMENT")
    print("Organisation: " + company_name)
    print("")
    popia_results = run_checks(popia_responses, POPIA_CHECKS)
    gdpr_results = run_checks(gdpr_responses, GDPR_CHECKS)
    popia_score, popia_passed, popia_total = calculate_score(popia_results)
    gdpr_score, gdpr_passed, gdpr_total = calculate_score(gdpr_results)
    print("POPIA RESULTS")
    print("----------------------------------------")
    for r in popia_results:
        print("  " + r["status"] + " | " + r["id"] + " | " + r["article"] + " | " + r["requirement"])
    print("")
    print("POPIA Score: " + str(popia_passed) + " out of " + str(popia_total) + " (" + str(popia_score) + " percent)")
    print("POPIA Status: " + get_compliance_level(popia_score))
    print("")
    print("GDPR RESULTS")
    print("----------------------------------------")
    for r in gdpr_results:
        print("  " + r["status"] + " | " + r["id"] + " | " + r["article"] + " | " + r["requirement"])
    print("")
    print("GDPR Score: " + str(gdpr_passed) + " out of " + str(gdpr_total) + " (" + str(gdpr_score) + " percent)")
    print("GDPR Status: " + get_compliance_level(gdpr_score))
    print("")
    overall = round((popia_score + gdpr_score) / 2, 1)
    print("OVERALL COMPLIANCE SCORE: " + str(overall) + " percent")
    print("OVERALL STATUS: " + get_compliance_level(overall))
    print("")
    print("GAP ANALYSIS - Failed Controls")
    print("----------------------------------------")
    all_results = popia_results + gdpr_results
    failures = [r for r in all_results if not r["passed"]]
    if failures:
        for f in failures:
            print("  FAIL | " + f["id"] + " | " + f["article"] + " | " + f["requirement"])
    else:
        print("  No gaps found - fully compliant")
    return {
        "company": company_name,
        "popia_score": popia_score,
        "gdpr_score": gdpr_score,
        "overall_score": overall,
        "popia_status": get_compliance_level(popia_score),
        "gdpr_status": get_compliance_level(gdpr_score),
        "failures": failures
    }


if __name__ == "__main__":
    print("SCENARIO 1 - Demo Organisation")
    popia_responses = {
        "POPIA-1": "yes", "POPIA-2": "yes", "POPIA-3": "yes",
        "POPIA-4": "no",  "POPIA-5": "yes", "POPIA-6": "no",
        "POPIA-7": "no",  "POPIA-8": "yes"
    }
    gdpr_responses = {
        "GDPR-1": "yes", "GDPR-2": "yes", "GDPR-3": "yes",
        "GDPR-4": "no",  "GDPR-5": "yes", "GDPR-6": "no",
        "GDPR-7": "yes", "GDPR-8": "no",  "GDPR-9": "no",
        "GDPR-10": "yes"
    }
    run_assessment("Demo Organisation", popia_responses, gdpr_responses)
    print("")
    print("SCENARIO 2 - WhatsApp LLC 2024 POPIA Enforcement Simulation")
    whatsapp_popia = {
        "POPIA-1": "no",  "POPIA-2": "no",  "POPIA-3": "no",
        "POPIA-4": "no",  "POPIA-5": "yes", "POPIA-6": "yes",
        "POPIA-7": "no",  "POPIA-8": "no"
    }
    whatsapp_gdpr = {
        "GDPR-1": "yes", "GDPR-2": "yes", "GDPR-3": "no",
        "GDPR-4": "no",  "GDPR-5": "yes", "GDPR-6": "no",
        "GDPR-7": "no",  "GDPR-8": "no",  "GDPR-9": "no",
        "GDPR-10": "no"
    }
    run_assessment(
        "WhatsApp LLC SA operations 2024 enforcement simulation",
        whatsapp_popia,
        whatsapp_gdpr
    )
