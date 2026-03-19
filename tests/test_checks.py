from tracker.checks import (
    run_checks, calculate_score,
    get_compliance_level, POPIA_CHECKS, GDPR_CHECKS
)


def test_all_pass():
    responses = {c["id"]: "yes" for c in POPIA_CHECKS}
    results = run_checks(responses, POPIA_CHECKS)
    assert all(r["passed"] for r in results)


def test_all_fail():
    responses = {c["id"]: "no" for c in POPIA_CHECKS}
    results = run_checks(responses, POPIA_CHECKS)
    assert all(not r["passed"] for r in results)


def test_score_full():
    responses = {c["id"]: "yes" for c in POPIA_CHECKS}
    results = run_checks(responses, POPIA_CHECKS)
    score, passed, total = calculate_score(results)
    assert score == 100.0


def test_score_zero():
    responses = {c["id"]: "no" for c in POPIA_CHECKS}
    results = run_checks(responses, POPIA_CHECKS)
    score, passed, total = calculate_score(results)
    assert score == 0.0


def test_compliant_rating():
    assert get_compliance_level(95) == "COMPLIANT"


def test_partial_rating():
    assert get_compliance_level(75) == "PARTIALLY COMPLIANT"


def test_high_risk_rating():
    assert get_compliance_level(55) == "NON-COMPLIANT HIGH RISK"


def test_critical_rating():
    assert get_compliance_level(30) == "NON-COMPLIANT CRITICAL RISK"


def test_popia_check_count():
    assert len(POPIA_CHECKS) == 8


def test_gdpr_check_count():
    assert len(GDPR_CHECKS) == 10


def test_whatsapp_scores_critical():
    whatsapp_popia = {
        "POPIA-1": "no",  "POPIA-2": "no",  "POPIA-3": "no",
        "POPIA-4": "no",  "POPIA-5": "yes", "POPIA-6": "yes",
        "POPIA-7": "no",  "POPIA-8": "no"
    }
    results = run_checks(whatsapp_popia, POPIA_CHECKS)
    score, passed, total = calculate_score(results)
    assert score < 50
    assert get_compliance_level(score) == "NON-COMPLIANT CRITICAL RISK"
