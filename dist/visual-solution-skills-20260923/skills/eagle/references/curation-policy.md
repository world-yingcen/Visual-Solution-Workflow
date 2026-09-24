# Eagle curation and write policy

Read before proposing classifications or writing item metadata, folders, or tags. Commands below run from the skill directory; the CLI path is relative to that directory.

### Organize items
```bash
# Add tags to items
node scripts/eagle-api-cli.js call item_add_tags --json '{"ids": ["item1", "item2"], "tags": ["reviewed", "approved"]}'

# Move items to folders
node scripts/eagle-api-cli.js call item_add_to_folders --json '{"ids": ["item1"], "folders": ["folder_id"]}'

# Create a new folder
node scripts/eagle-api-cli.js call folder_create --json '{"folders": [{"name": "My Folder", "iconColor": "blue"}]}'
```

### User organization rules

- Use a review-first workflow for curation. Analyze and propose the exact folders, tags, name, and note before changing Eagle. Write only after the user explicitly approves the proposal, unless the user has already authorized that exact batch and classification.
- When a source URL is available, open and inspect every case before classifying it. Do not classify from the title or thumbnail alone. Inspect the relevant page, overall visual system, layout, and observable motion; use screenshots only as supporting evidence or when the live page is unavailable.
- Preserve a useful note for every accepted reference. The note should explain the visible design, transferable design methods, why it is worth collecting, and where it can be reused. Record implementation technology such as `GSAP` only when verified or confirmed by the user.
- For ordinary references, add every folder and tag that has clear, independent retrieval value. Do not add weak associations merely to maximize metadata.
- If an item is classified as `整站參考`, do not also assign page or section folders by default. Add a section folder only when the user is intentionally collecting that section as a separate reference target.
- Use `創意` when the reusable value is the concept or unexpected design solution itself, not merely because the page looks unusual.
- Do not use `CSS` or `JavaScript` as tags for ordinary website references because they do not narrow retrieval. Keep a specific technology such as `GSAP` only when it is meaningfully relevant and confirmed.
- Treat highly specific page sections with little reuse value as a single-entry category; do not create redundant discovery paths through extra folders or tags.
- Footer references should normally belong only to the `頁尾 Footer` folder. Preserve their analysis notes, but remove unrelated folders and all tags.
- Exception: when a footer contains a clearly reusable cross-context pattern, add only the relevant secondary reference folder. The confirmed exception is a footer integrated with a map, which may also belong to `地圖參考`.
- Do not apply the exception merely because a footer has a distinctive visual style, industry, layout, or implementation technique. Add a secondary entry only when that feature is useful outside footer design.

### Tag management
```bash
# List all tags
node scripts/eagle-api-cli.js call tag_get

# Merge duplicate tags
node scripts/eagle-api-cli.js call tag_merge --json '{"sourceTags": ["photo", "photograph"], "targetTag": "photo"}'
```
