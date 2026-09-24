---
name: eagle
description: Control Eagle application for digital asset management - search, organize, tag items, manage folders and tag groups. Use when user wants to interact with their Eagle library, search for images, manage tags or folders.
allowed-tools: Bash(node *)
---

# Eagle API Skill

Control the local Eagle application through CLI commands. Eagle is a digital asset management tool for organizing images, videos, fonts, and design files.

## Prerequisites

- Eagle application must be running
- Eagle MCP plugin must be enabled (provides the local API server on port 41596)

## CLI Usage

The CLI script is located at `scripts/eagle-api-cli.js` relative to this skill directory.

```bash
# Call a tool with JSON parameters
node scripts/eagle-api-cli.js call <tool_name> --json '{"key": "value"}'

# Call a tool with individual parameters
node scripts/eagle-api-cli.js call <tool_name> --param1 value1 --param2 value2

# List all available tools
node scripts/eagle-api-cli.js list

# Get help for a specific tool
node scripts/eagle-api-cli.js help <tool_name>
```

Array and object values are auto-parsed from JSON:
```bash
node scripts/eagle-api-cli.js call item_get --tags '["photo","landscape"]' --limit 10
```

## Tool Categories

Choose the relevant reference file for detailed tool documentation:

- **App** — Get Eagle app info (version, platform, locale). See [references/app-tools.md](references/app-tools.md)
- **Item** — Search, filter, add, update, tag, and organize library items. See [references/item-tools.md](references/item-tools.md)
- **Folder** — Create, query, and update folder hierarchy. See [references/folder-tools.md](references/folder-tools.md)
- **Tag** — Query, count, rename, and merge tags. See [references/tag-tools.md](references/tag-tools.md)
- **Tag Group** — Manage tag groups and tag associations. See [references/tag-group-tools.md](references/tag-group-tools.md)
- **Smart Folder** — Create and manage smart folders with filter conditions. See [references/smart-folder-tools.md](references/smart-folder-tools.md)
- **AI Search** — Semantic search by text or similar items (requires AI Search plugin). See [references/ai-search-tools.md](references/ai-search-tools.md)

## Common Workflows

### Search for items
```bash
# Text search
node scripts/eagle-api-cli.js call item_query --query "sunset landscape"

# Filter by tags and extension
node scripts/eagle-api-cli.js call item_get --tags '["photo"]' --ext "jpg" --limit 20

# Get selected items in Eagle
node scripts/eagle-api-cli.js call item_get_selected
```

### Curation or writes

Before classifying, organizing, or changing items, folders, or tags, read [curation policy](references/curation-policy.md) plus the relevant API reference. Ordinary search and mother-template selection are read-only and do not require the curation policy.
