POPIA_CHECKS = [
    {
        "id": "POPIA-1",
        "article": "Section 9",
        "requirement": "Personal information collected for a specific lawful purpose",
        "question": "Do you collect personal information for a specific defined purpose?"
    },
    {
        "id": "POPIA-2",
        "article": "Section 11",
        "requirement": "Processing of personal information requires consent",
        "question": "Do you obtain consent before processing personal information?"
    },
    {
        "id": "POPIA-3",
        "article": "Section 19",
        "requirement": "Appropriate security measures to protect personal information",
        "question": "Do you have security measures in place to protect personal data?"
    },
    {
        "id": "POPIA-4",
        "article": "Section 22",
        "requirement": "Notify regulator and data subjects of security breaches",
        "question": "Do you have a breach notification process in place?"
    },
    {
        "id": "POPIA-5",
        "article": "Section 23",
        "requirement": "Data subject access to their personal information",
        "question": "Can individuals request access to their personal data?"
    },
    {
        "id": "POPIA-6",
        "article": "Section 24",
        "requirement": "Data subject can request correction of their information",
        "question": "Can individuals request correction of their personal data?"
    },
    {
        "id": "POPIA-7",
        "article": "Section 72",
        "requirement": "Cross-border transfer of personal information is restricted",
        "question": "Do you restrict transfer of personal data outside South Africa?"
    },
    {
        "id": "POPIA-8",
        "article": "Section 55",
        "requirement": "Information Officer must be designated",
        "question": "Have you appointed an Information Officer?"
    }
]

GDPR_CHECKS = [
    {
        "id": "GDPR-1",
        "article": "Article 5",
        "requirement": "Personal data processed lawfully fairly and transparently",
        "question": "Do you process personal data lawfully and transparently?"
    },
    {
        "id": "GDPR-2",
        "article": "Article 6",
        "requirement": "Lawful basis for processing personal data is established",
        "question": "Have you identified a lawful basis for all data processing?"
    },
    {
        "id": "GDPR-3",
        "article": "Article 7",
        "requirement": "Consent must be freely given specific and informed",
        "question": "Is your consent mechanism freely given specific and documented?"
    },
    {
        "id": "GDPR-4",
        "article": "Article 13",
        "requirement": "Data subjects informed at point of collection",
        "question": "Do you provide a privacy notice at the point of data collection?"
    },
    {
        "id": "GDPR-5",
        "article": "Article 17",
        "requirement": "Right to erasure",
        "question": "Can individuals request deletion of their personal data?"
    },
    {
        "id": "GDPR-6",
        "article": "Article 25",
        "requirement": "Data protection by design and by default",
        "question": "Is data protection built into your systems by design?"
    },
    {
        "id": "GDPR-7",
        "article": "Article 32",
        "requirement": "Appropriate technical and organisational security measures",
        "question": "Do you have technical security measures protecting personal data?"
    },
    {
        "id": "GDPR-8",
        "article": "Article 33",
        "requirement": "Breach notification to supervisory authority within 72 hours",
        "question": "Can you notify authorities of a breach within 72 hours?"
    },
    {
        "id": "GDPR-9",
        "article": "Article 35",
        "requirement": "Data Protection Impact Assessment for high-risk processing",
        "question": "Do you conduct DPIAs for high-risk data processing activities?"
    },
    {
        "id": "GDPR-10",
        "article": "Article 37",
        "requirement": "Data Protection Officer appointed where required",
        "question": "Have you appointed a Data Protection Officer?"
    }
]


def run_checks(responses, checks):
    results = []
    for check in checks:
        check_id = check["id"]
        response = responses.get(check_id, "no")
        passed = response.strip().lower() == "yes"
        results.append({
            "id": check_id,
            "article": check["article"],
            "requirement": check["requirement"],
            "passed": passed,
            "status": "PASS" if passed else "FAIL"
        })
    return results


def calculate_score(results):
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    score = round((passed / total) * 100, 1) if total > 0 else 0
    return score, passed, total


def get_compliance_level(score):
    if score >= 90:
        return "COMPLIANT"
    elif score >= 70:
        return "PARTIALLY COMPLIANT"
    elif score >= 50:
        return "NON-COMPLIANT HIGH RISK"
    else:
        return "NON-COMPLIANT CRITICAL RISK"
