# Full Reporting Privacy Notice (PDPL-focused)

This document expands the repository's Reporting Privacy Notice to include PDPL
requirements and more detailed operational guidance for handling personal data
received through conduct reports and investigations. It is intended to assist
project maintainers and legal counsel in preparing a PDPL-compliant processing
record.

Authoritative references
- UAE Personal Data Protection Law (Federal Decree-Law No. 45 of 2021):
  https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws
- UAE Data Office: https://dataoffice.gov.ae/
- Contributor Covenant FAQ: https://www.contributor-covenant.org/faq/

1. Data controller and contact
- Data controller: Repository maintainers (almiccy-source).
- Enquiries and data subject requests: almiccy@gmail.com (enforcement contact).
- If you appoint a dedicated DPO or privacy contact, include their details here.

2. Categories of personal data processed
- Identification data: name, username, email address, affiliation.
- Contact data: telephone number (if provided), mailing address (if provided).
- Case data: messages, issue/PR references, screenshots, attachments,
  timestamps, and other evidence submitted by reporter or collected during the
  investigation.
- Special categories: avoid collecting any ‘‘sensitive personal data’‘ (e.g.,
  health data, political opinions, religious beliefs) unless strictly necessary
  and lawful; if collected, document the legal justification and additional
  safeguards.
- Technical/metadata: IP addresses, device metadata, and system logs where
  necessary for security or abuse investigations.

3. Purposes and lawful basis under PDPL
- Purposes:
  - Investigate alleged breaches of the Code of Conduct.
  - Take corrective actions (warnings, suspensions, bans) and maintain a safe
    project environment.
  - Fulfil legal obligations (e.g., responses to lawful requests from
    authorities).
- Lawful basis:
  - Legitimate interests of the controller in protecting the community’s safety
    and project integrity.
  - Compliance with legal obligations when required by law or court order.
  - Consent where appropriate for optional processing (e.g., sharing
    anonymised case studies for community training).
- Document each processing activity and the selected lawful basis in the
  controller’s processing register.

4. Data minimisation and purpose limitation
- Collect the minimum data necessary for the specific investigation.
- Do not use reporting data for unrelated profiling or commercial purposes.
- If you plan to reuse anonymised case summaries for training, ensure true
  anonymisation and document the anonymisation methods.

5. Retention and deletion
- Retention: case files retained for up to 24 months by default from case
  closure. Legal holds may require longer retention (e.g., for litigation).
- Deletion: provide an operational workflow to delete or anonymise data after
  retention period expiry. Record deletion actions in an audit log.

6. Data subject rights and handling requests
- PDPL rights include access, correction, objection, and deletion subject to
  legal exceptions. Establish procedures and templates for responding to
  requests within PDPL timelines.
- Verify identity before releasing case material; redact third-party PII where
  appropriate.

7. Security and access control
- Access: limit to enforcement team members and legal counsel.
- Authentication: use strong authentication for accounts with access to case
  data (MFA recommended).
- Storage: prefer project-controlled secure storage (private repositories or
  approved third-party services with contractual safeguards). Encrypt data at
  rest and in transit where supported by the provider.
- Logging: keep an access audit trail recording who accessed case files and
  why.

8. Cross-border transfers and processors
- GitHub and other processing services may store data outside the UAE. PDPL may
  restrict or require safeguards for transfers. Document any transfers and the
  safeguards relied upon (e.g., contractual terms, standard contractual
  clauses, adequacy decisions if any).
- When using third-party processors, have written contracts specifying
  processing limits, security measures, and subprocessors.

9. Data breach response
- Define a breach response plan: containment, assessment, notification to
  supervisory authority (if required by PDPL), and notification to affected
  individuals where necessary.
- Keep breach records and lessons learned.

10. Law enforcement and legal disclosures
- Establish a process to verify lawful requests (court orders, warrants) and to
  involve legal counsel before disclosing case materials to third parties or
  authorities.

11. Privacy notices and transparency
- Provide a short public notice (REPORTING_PRIVACY_NOTICE.md) and a full
  processing record for legal review. Ensure contributors are informed at the
  point of reporting about what is processed and why.

12. Data Protection Impact Assessment (DPIA)
- For high-risk processing (e.g., large-scale processing, special category
  data, or profiling), perform a DPIA and document risk mitigation measures.

13. Recordkeeping
- Maintain a processing register that includes: purpose, categories of personal
  data, recipients, retention periods, legal basis, transfer mechanisms, and
  security measures.

14. Templates (suggested)
- Intake acknowledgement template
- Data subject access request (DSAR) response template
- Deletion/retention action log template

15. Further steps
- Have this notice and the processing register reviewed by UAE-qualified
  counsel and, if applicable, appoint or register a DPO per organizational
  needs.


