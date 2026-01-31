# WordPress Export/Import Workflow Notes (WP All Export + WP All Import)

## Goal
Update the **"Home - Buddy Update"** page content in a WordPress site using a CSV export/import workflow and avoid duplicate pages or no‑content imports.

---

## Source Files Used
- Full export (edited): `docs/Pages-Export-2026-January-31-1741-buddy-updated.csv`
- Single‑row export for clean import: `docs/Pages-Export-Home-Buddy-Update-only.csv`

The single‑row file is preferred for testing to avoid touching other pages.

---

## Key Concepts (Why imports failed)
1. **Unique Identifier mismatch**
   - When importing into a *different* WordPress site, IDs rarely match.
   - Use **Slug** as the Unique Identifier (e.g., `home-2`) to update the correct page.

2. **Title not mapped = "No Title" pages**
   - If the Title field isn’t mapped, WP All Import creates a **No Title** page.
   - This looks like “nothing happened,” but a blank page is created.

3. **Skipped record = no matching existing post AND new posts disabled**
   - Log message: `SKIPPED: The option 'Create new posts...' is disabled`
   - This means WP All Import could not find a match and was not allowed to create one.

---

## Recommended Import Settings (WP All Import)
### 1) Basic mapping
- **Post Type:** Page
- **Title:** map to CSV `Title`
- **Content:** map to CSV `Content`
- **Slug:** map to CSV `Slug`

### 2) Unique Identifier
- Set **Unique Identifier** to `Slug` (for this workflow)

### 3) Create vs Update
- **If record exists:** Update existing items
- **If record doesn’t exist:** Create new posts (at least for the first run)

---

## Troubleshooting by Log Message

### A) "Skipped 1 records"
Log example:
```
SKIPPED: The option 'Create new posts from records newly present in this import file' is disabled
```
**Fix:**
- Either allow creating new posts, or
- Ensure the Unique Identifier actually matches an existing page

---

### B) "Title is empty"
Log example:
```
WARNING: title is empty.
```
**Fix:**
- Map CSV `Title` to WordPress Title field
- Delete the resulting "No Title" page that was created

---

## Known Working Values (from this project)
- Page title: **Home - Buddy Update**
- Slug: **home-2**
- Permalink: `/home-2/`

---

## Process Used in This Repo
1. Edited `docs/Pages-Export-2026-January-31-1741.csv` to replace all cooking/lorem ipsum content for the **Home - Buddy Update** row.
2. Saved full renamed file: `docs/Pages-Export-2026-January-31-1741-buddy-updated.csv`.
3. Exported a single‑row file for clean import: `docs/Pages-Export-Home-Buddy-Update-only.csv`.
4. Imported with WP All Import using **Slug** as Unique Identifier and proper mappings for Title/Content/Slug.

---

## Minimal Checklist (paste into WP All Import)
- [ ] Post Type = Page
- [ ] Title → `Title`
- [ ] Content → `Content`
- [ ] Slug → `Slug`
- [ ] Unique Identifier = `Slug`
- [ ] If record exists → Update
- [ ] If record doesn’t exist → Create (first run)

---

## Notes
- If you see a new “No Title” page, mapping is wrong.
- If you see “Skipped 1 records,” it didn’t match any existing page and wasn’t allowed to create one.
- When importing into a new WordPress install, always prefer **Slug** over **ID**.
