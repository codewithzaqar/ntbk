# Trek - A Simle Journey CLI

`trek` is a simple command-line journaling application written is Python. It allows users to add, list, and search journal entries.

| Command | Arguments   | Description |
| ------- | ----------- | ----------- |
| `add`     | `--title`, `--content`| Add a new journal entry    |
| `list`    | None | Display all journal entries |
| `search`  | `--keyword` | Search for journal entries by keyword |
| `delete` | `--title` | Delete a journal entry by title |
| `edit` | `--title`, `--new-title`, `--new-content` | Edit an existing journal entry |
| `export` | `--format [txt/json]`, `--filename [optional]` | Export journal entries to a file |
| `import` | `--import-format [txt/json]`, `--import-filename [optional]` | Import journal entries from a file |
| `count` | None | Display the total number of journal entries |