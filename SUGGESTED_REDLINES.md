# Suggested Redlines and Safe-Wording (for legal review)

This file contains proposed wording changes (redlines) to reduce defamation and
PDPL risk. Have UAE counsel review before applying.

A. CODE_OF_CONDUCT.md — key redlines

1) Enforcement / Public statements (insert under Enforcement Guidelines)

- CURRENT (risk): "Community leaders have the right and responsibility to
  remove, edit, or reject comments, commits, code... and will communicate
  reasons for moderation decisions when appropriate."

- SUGGESTED (safer): "Community leaders may remove, edit, or reject
  contributions that are not aligned with this Code of Conduct. The project
  will, where appropriate and lawful, explain moderation decisions privately to
  the parties involved. The project will avoid public disclosure of detailed
  allegations or unproven statements; any public summaries will be
  anonymised and reviewed by legal counsel when there is a risk of defamation
  or criminal exposure."

Rationale: Avoids public naming and unverified allegations that could trigger
UAE criminal defamation or cybercrime exposure.

2) Reporting contact (clarify confidentiality & access)

- Add: "Reports are received confidentially. Access to raw reports is limited
  to the enforcement team and legal counsel. For continuity, consider using a
  project-managed alias rather than a personal account."

Rationale: Limits surprise exposure of personal mailbox and documents chain.

3) Applicability & Local Law (strengthen legal caution)

- Add: "In case of allegations that may amount to a criminal offence under
  applicable law, maintainers will seek legal advice before taking public
  action. The project does not provide legal advice to reporters or
  respondents; individuals should seek independent legal counsel if needed."

B. REPORTING_PRIVACY_NOTICE.md & FULL_REPORTING_PRIVACY_NOTICE.md — redlines

1) Lawful basis clarification
- Add a line documenting the primary lawful basis used for processing ("legitimate
  interests of the controller to protect the project community") and when
  consent is used (e.g., for optional anonymised learning case studies).

2) Transfers & processors
- Add required note: "GitHub and other processors may store data outside the
  UAE. We will document transfers and the contractual safeguards relied upon."

3) Retention exception clarity
- Add: "Legal holds: where required by law, data may be retained beyond the
  stated retention period. This will be documented in the case file."

C. MODERATOR_SOP.md — procedural safety redlines

1) Two‑person signoff and legal review requirement
- Add a mandatory two‑moderator + legal signoff for any public disclosure,
  naming, or content removal that could give rise to defamation claims.

2) Limit public content edits
- Edit policy: do not post unredacted screenshots or verbatim allegations in
  public issues; always redact personal identifiers before posting.

3) Escalation timing
- For high‑risk cases, pause public removal until legal counsel is engaged (or
  a short hold of 48 hours while counsel is consulted), unless immediate
  safety concerns require emergency action.

D. Recommended metadata & audit entries

- For every case, capture: CaseID, intake timestamp, triage level, persons
  with access (usernames), retention period, legal basis for processing,
  disposition, and deletion timestamp (if deleted). This supports PDPL and
  defensibility.


Note: Apply these changes by redlining the repository files; I can prepare a
pull request with the redlines if you want (requires confirming you're OK with
committing the suggested language).