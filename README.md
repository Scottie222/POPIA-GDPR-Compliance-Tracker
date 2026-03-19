# POPIA and GDPR Compliance Tracker

A Python tool that scores an organisation against POPIA and GDPR
and identifies which controls are failing and why.

Built around the 2024 WhatsApp enforcement action by South Africa's
Information Regulator, the first major tech enforcement under POPIA.

---

## Real-World Case Study

In September 2024, South Africa's Information Regulator issued a
formal enforcement notice against WhatsApp for violating POPIA.

The core finding was that WhatsApp applied full GDPR protections
to European users but gave South African users a weaker standard
under POPIA despite both laws requiring the same level of protection.

This tool is designed to detect exactly that kind of gap.

### What WhatsApp failed on

| POPIA Section | Violation |
|--------------|-----------|
| Section 8 | No lawful basis for processing demonstrated |
| Section 9 | Collected more personal data than necessary |
| Section 11 | Consent was not voluntary or informed |
| Section 13 | Purpose of data collection not clearly stated |
| Section 15 | Data used for new purposes without permission |
| Section 17 | No documentation of processing activities |
| Section 19 | Inadequate security safeguards |

### Penalty risk

- Fine up to R10 million
- Imprisonment up to 10 years
- Mandatory Personal Information Impact Assessment required

### WhatsApp scored through this tracker

| Framework | Score | Rating |
|-----------|-------|--------|
| POPIA | 25 percent | Non-Compliant Critical Risk |
| GDPR | 30 percent | Non-Compliant Critical Risk |
| Overall | 27.5 percent | Non-Compliant Critical Risk |

---

## What This Tool Does

Runs 8 POPIA checks and 10 GDPR checks against real law references.
Scores each framework separately and gives an overall compliance rating.
Lists every failed control with the specific section or article number.

---

## Compliance Score Guide

| Score | Rating |
|-------|--------|
| 90 to 100 percent | Compliant |
| 70 to 89 percent | Partially Compliant |
| 50 to 69 percent | Non-Compliant High Risk |
| 0 to 49 percent | Non-Compliant Critical Risk |

---

## Frameworks Covered

| Framework | Checks | Law Reference |
|-----------|--------|---------------|
| POPIA | 8 checks | Sections 9, 11, 19, 22, 23, 24, 55, 72 |
| GDPR | 10 checks | Articles 5, 6, 7, 13, 17, 25, 32, 33, 35, 37 |

---

## How to Run

pip install -r requirements.txt

python tracker/report.py

---

## Official References

POPIA Full Text
https://www.justice.gov.za/inforeg/docs/InfoRegSA-POPIA-act4of2013.pdf

Information Regulator South Africa
https://inforegulator.org.za

WhatsApp Enforcement Notice Analysis
https://www.michalsons.com/blog/whatsapp-enforcement-notice-popia-breaches/77829

GDPR Overview
https://gdpr.eu/what-is-gdpr/

Related Project GRC Controls Lab
https://github.com/Scottie222/GRC-Controls-Lab
