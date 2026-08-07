# Move / Secure MODERATOR_SOP.md — Recommended steps

MODERATOR_SOP.md contains sensitive operational detail and should be restricted.
Below are actionable options and commands to secure the SOP.

Option A — Move SOP to a private repository (recommended)
1) In GitHub UI, create a new private repository (e.g., "assistant-resident-engineer-private").
   - Settings → Create repository → Set Visibility = Private.
2) In your local environment:
   - git clone https://github.com/almiccy-source/assistant-resident-engineer.git
   - cd assistant-resident-engineer
   - git mv MODERATOR_SOP.md ../assistant-resident-engineer-private/
   - git commit -m "Move MODERATOR_SOP.md to private repo"
   - git push
3) In the private repo, add required maintainers and restrict access via Teams or specific users.

Option B — Make file accessible only to specific collaborators within the same repo
- GitHub does not support per-file permissions. Use a separate private repo or use encrypted secrets or store SOP in a non-repository secure store (e.g., company SharePoint, Google Drive with access control).

Option C — Use a protected branch with limited push access
1) Create a protected branch (e.g., `private`) and put SOP there.
2) Repository Settings → Branches → Add rule: protect `private`, restrict who can push.
3) Move MODERATOR_SOP.md to `private` branch and remove it from `main`.

Commands (example: move file to private branch)
- git checkout -b private
- git rm MODERATOR_SOP.md
- git commit -m "Remove SOP from main"
- git push origin private
- In private branch, re-add SOP and restrict branch pushes in Settings.

Recommendations
- Option A (private repo) is simplest and most secure.
- Keep an audit of access granted and rotate access periodically.
