### Compliance overview — POPIA vs GDPR vs Overall
![Compliance Overview](https://raw.githubusercontent.com/Scottie222/POPIA-GDPR-Compliance-Tracker/main/outputs/chart-compliance-overview.png)

### Control-by-control breakdown
![Control Breakdown](https://raw.githubusercontent.com/Scottie222/POPIA-GDPR-Compliance-Tracker/main/outputs/chart-control-breakdown.png)

### Gap analysis, all failed controls
![Gap Analysis](https://raw.githubusercontent.com/Scottie222/POPIA-GDPR-Compliance-Tracker/main/outputs/chart-gap-analysis.png)

---

## The real incident

In September 2024, South Africa's Information Regulator issued a formal enforcement notice against WhatsApp for violating POPIA. The core finding was that WhatsApp applied full GDPR protections to European users but gave South African users a materially weaker standard despite both laws requiring equivalent protection for personal information.

WhatsApp collected more data than necessary, failed to obtain proper consent, had no documented lawful basis for processing, and provided no meaningful transparency to South African users about how their data was used or shared with Meta entities.

This was the first major tech enforcement action under POPIA and set a direct precedent for how multinational platforms will be treated by the Information Regulator going forward.

### What WhatsApp failed on

| POPIA Section | Requirement | Finding |
|---|---|---|
| Section 8 | Accountability responsible party must ensure compliance | No lawful basis for processing demonstrated |
| Section 9 | Processing limitation only necessary data collected | Collected significantly more data than necessary |
| Section 11 | Consent must be voluntary, specific and informed | Consent bundled into terms of service not freely given |
| Section 13 | Purpose specification purpose must be clear and documented | Purpose of data collection not clearly stated to users |
| Section 15 | Further processing limitation new use requires permission | Data used for new purposes without user permission |
| Section 17 | Information officer documentation of processing required | No documentation of processing activities maintained |
| Section 19 | Security safeguards appropriate measures required | Inadequate technical and organisational security measures |

### Penalty exposure

| Penalty type | Maximum |
|---|---|
| Administrative fine | R10 million |
| Criminal imprisonment | 10 years |
| Mandatory remediation | Personal Information Impact Assessment required |
| Regulatory action | Enforcement notice, cease and desist processing |

### WhatsApp scored through this tracker

| Framework | Checks | Passed | Score | Status |
|---|---|---|---|---|
| POPIA | 8 | 2 | 25% | Non-Compliant Critical Risk |
| GDPR | 10 | 3 | 30% | Non-Compliant Critical Risk |
| Overall | 18 | 5 | 27.5% | Non-Compliant Critical Risk |

---

## How the tool works

### Step 1 Define your responses

The tool takes a dictionary of yes/no responses to 18 compliance questions, 8 for POPIA and 10 for GDPR. Each question maps directly to a specific legal obligation:

```python
POPIA_RESPONSES = {
    "POPIA-1": "yes",   # Section 9  only necessary data collected?
    "POPIA-2": "no",    # Section 11 consent freely given and informed?
    "POPIA-3": "no",    # Section 19 appropriate security safeguards?
    "POPIA-4": "no",    # Section 22 breach notification process in place?
    "POPIA-5": "yes",   # Section 23 data subjects can access their data?
    "POPIA-6": "yes",   # Section 24 data subjects can correct their data?
    "POPIA-7": "no",    # Section 72 cross-border transfers restricted?
    "POPIA-8": "no",    # Section 55 Information Officer designated?
}
```

### Step 2 — Scoring

Each passed check contributes equally to the framework score. Scores are calculated as:
Score = (passed checks / total checks) × 100

| Score | Rating |
|---|---|
| 90–100% | Compliant |
| 70–89% | Partially compliant |
| 50–69% | Non-compliant high risk |
| 0–49% | Non-compliant critical risk |

### Step 3 — Gap analysis

Every failed control is listed with its specific section or article number and the exact legal requirement it maps to, giving the compliance team a direct remediation roadmap rather than a generic recommendation.

### Step 4 — Visualisation

Three PNG charts are generated automatically:

| Chart | Description |
|---|---|
| `chart-compliance-overview.png` | Donut charts showing POPIA score, GDPR score and overall score side by side |
| `chart-control-breakdown.png` | Pass/fail status for every individual control across both frameworks |
| `chart-gap-analysis.png` | All failed controls listed with their legal reference and requirement |

---

## What the tool assesses

### POPIA checks — 8 controls

| Check | Section | Requirement |
|---|---|---|
| POPIA-1 | Section 9 | Personal information collected for a specific lawful purpose |
| POPIA-2 | Section 11 | Processing of personal information requires valid consent |
| POPIA-3 | Section 19 | Appropriate security measures to protect personal information |
| POPIA-4 | Section 22 | Notify regulator and data subjects of security breaches |
| POPIA-5 | Section 23 | Data subjects can access their personal information |
| POPIA-6 | Section 24 | Data subjects can request correction of their information |
| POPIA-7 | Section 72 | Cross-border transfer of personal information is restricted |
| POPIA-8 | Section 55 | Information Officer must be designated |

### GDPR checks — 10 controls

| Check | Article | Requirement |
|---|---|---|
| GDPR-1 | Article 5 | Personal data processed lawfully, fairly and transparently |
| GDPR-2 | Article 6 | Lawful basis for processing personal data is established |
| GDPR-3 | Article 7 | Consent must be freely given, specific and informed |
| GDPR-4 | Article 13 | Data subjects informed at point of collection |
| GDPR-5 | Article 17 | Right to erasure implemented |
| GDPR-6 | Article 25 | Data protection by design and by default |
| GDPR-7 | Article 32 | Appropriate technical and organisational security measures |
| GDPR-8 | Article 33 | Breach notification to supervisory authority within 72 hours |
| GDPR-9 | Article 35 | Data Protection Impact Assessment for high-risk processing |
| GDPR-10 | Article 37 | Data Protection Officer appointed where required |

---

## How to run

```bash
git clone https://github.com/Scottie222/POPIA-GDPR-Compliance-Tracker.git
cd POPIA-GDPR-Compliance-Tracker
pip install -r requirements.txt
python run_assessment.py
```

This runs the full WhatsApp case study assessment and generates all 3 charts in `outputs/`.

To run the text-only assessment without charts:

```bash
python -m tracker.report
```

To assess a different organisation, edit the response dictionaries in `run_assessment.py` — change any `"no"` to `"yes"` to reflect implemented controls.

---

## Project structure
POPIA-GDPR-Compliance-Tracker/
├── tracker/
│   ├── checks.py       
│   ├── report.py       
│   └── visualise.py    
├── tests/              
├── outputs/            
├── run_assessment.py   
├── CASE-STUDY.md      
├── requirements.txt
└── README.md

---

## References

1. Information Regulator enforcement notice https://inforegulator.org.za
2. WhatsApp enforcement analysis https://www.michalsons.com/blog/whatsapp-enforcement-notice-popia-breaches/77829
3. POPIA Act 4 of 2013 https://www.justice.gov.za/inforeg/docs/InfoRegSA-POPIA-act4of2013.pdf
4. GDPR https://gdpr.eu/what-is-gdpr/
5. ISO/IEC 27001:2022 https://www.iso.org/standard/82875.html

---

## Related GRC portfolio projects

| Project | Domain | Real incident |
|---|---|---|
| [StandardBank-Risk-Assessment](https://github.com/Scottie222/StandardBank-Risk-Assessment) | Risk Assessment | Experian SA 2020 — 24M records. [Live demo](https://scottie222.github.io/StandardBank-Risk-Assessment/) |
| [CloudSec-Assessment-SA](https://github.com/Scottie222/CloudSec-Assessment-SA) | Cloud Security | Dis-Chem 2022, Experian SA 2020 |
| [GRC-Controls-Lab](https://github.com/Scottie222/GRC-Controls-Lab) | Controls Lab | Capital One 2019 |
| [RetailCo-Security-Awareness](https://github.com/Scottie222/RetailCo-Security-Awareness) | Security Awareness | R200M SA phishing losses 2023 |
| [VendorRisk-SA](https://github.com/Scottie222/VendorRisk-SA) | Third-Party Risk | Experian, Dis-Chem, MTN, TransUnion |
| [LifeHealthcare-BCP](https://github.com/Scottie222/LifeHealthcare-BCP) | BCP/DR | Life Healthcare ransomware 2020 |
| [MTN-ISMS-Audit](https://github.com/Scottie222/MTN-ISMS-Audit) | Internal Audit | MTN SA breach April 2025 |
