# OSINT Framework - Data Policy

## 🔐 CRITICAL SECURITY POLICY

### Investigation Results - LOCAL ONLY

**RULE: Investigation results and OSINT data will NEVER be pushed to GitHub.**

All investigation output files must remain on the local machine only for security and privacy reasons.

---

## Files That Are NEVER Pushed to GitHub

### Investigation Results
- level_*_results.json - Level-specific analysis results
- consolidated_report.json - Consolidated findings
- INVESTIGATION_REPORT.txt - Investigation reports
- investigation_*.log - Investigation logs
- session_*/ - Session directories with results

### Sensitive Data
- Target information
- Personal data extracted
- IP addresses and geolocation
- Financial information
- Private communications
- Metadata and EXIF data

### Generated Reports
- HTML reports with findings
- CSV exports with data
- PDF reports with analysis
- Markdown reports with results

---

## Files That ARE Pushed to GitHub

### Framework Code (OK to push)
✓ level_1_email_search.py - Script files only
✓ level_2_username_extraction.py - Code only
✓ osint_master_orchestrator.py - Orchestrator code
✓ eport_generator.py - Report generation code
✓ un_osint_investigation.py - Main script

### Configuration (OK to push)
✓ mcp.json - MCP configuration template
✓ mcp-providers.json - Provider configuration
✓ cursor-settings.json - Cursor settings

### Documentation (OK to push)
✓ README.md - Framework documentation
✓ UI_README.md - UI documentation
✓ QUICKSTART.md - Quick start guide
✓ POLICY.md - This policy document

### User Interface (OK to push)
✓ osint_ui.html - UI code (no results embedded)

### Build Files (OK to push)
✓ .gitignore - Git ignore rules
✓ equirements.txt - Dependencies (if added)

---

## How to Use the Framework Safely

### 1. Run Investigation (Locally)
`ash
python run_osint_investigation.py target@example.com
`

### 2. Results Stay Local
All results are saved in:
- ./level_*_results.json
- ./osint_results/
- ./investigation_results/

These directories are in .gitignore and cannot be pushed.

### 3. Review Results (Locally)
- Check generated reports
- Review findings
- Analyze data
- All on your machine only

### 4. Archive Results (Locally)
`ash
# Create local backup (NEVER push to GitHub)
zip -r investigation_backup.zip level_*_results.json
`

---

## What Happens if Files Are Accidentally Created

### Automatic Protection
- .gitignore prevents accidental commits
- Git will ignore all result files
- git add . will not include results
- Explicit git add FILENAME required to override

### If Something Gets Added by Mistake
`ash
# Remove from staging
git reset HEAD filename

# Remove from history
git rm --cached filename
git commit --trailer "Made-with: Cursor" -m "Remove accidentally added file"
git push origin main
`

---

## Security Best Practices

### ✓ DO:
- Keep investigation results local
- Use .gitignore to protect data
- Review results before archiving
- Use strong passwords
- Enable 2FA on GitHub

### ✗ DON'T:
- Push investigation results
- Share result files publicly
- Commit sensitive data
- Upload personal information
- Store credentials in code

---

## Privacy & Ethics Reminders

1. **Authorized Use Only**
   - Only investigate with proper authorization
   - Respect privacy and consent
   - Follow local laws and regulations

2. **Data Protection**
   - Investigation results are sensitive
   - Keep data confidential
   - Secure local storage
   - Delete when no longer needed

3. **Responsible Use**
   - OSINT tools are powerful
   - Use ethically and responsibly
   - Respect individuals' privacy
   - Don't abuse for harassment or harm

---

## Emergency: Removing Sensitive Data from GitHub

If sensitive data was pushed (which it shouldn't be), use:

`ash
# Option 1: Remove file from history (careful!)
git filter-branch --tree-filter 'rm -f filename' HEAD

# Option 2: Use GitHub CLI
gh repo delete-release <release>

# Option 3: Contact GitHub support
# https://support.github.com/en
`

**Note:** Prefer to use .gitignore and keep results local to avoid this situation.

---

## Summary

| Item | Location | Pushed to GitHub |
|------|----------|------------------|
| Framework Scripts | GitHub | ✓ YES |
| Configuration | GitHub | ✓ YES |
| Documentation | GitHub | ✓ YES |
| UI Code | GitHub | ✓ YES |
| Investigation Results | Local Only | ✗ NO |
| Report Files | Local Only | ✗ NO |
| Sensitive Data | Local Only | ✗ NO |
| Personal Information | Local Only | ✗ NO |

---

## Questions?

Review this policy before running investigations.
Keep investigation results private and local.
Use the framework responsibly and ethically.

**Framework is safe for GitHub. Results stay private.** 🔐