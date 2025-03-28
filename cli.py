import argparse
from journal.journal import Journal

def main():
    parser = argparse.ArgumentParser(description="Simple Journal CLI")
    parser.add_argument("action", choices=["add", "list", "search", "delete", "edit", "export", "import", "count"], help="Action to perform")
    parser.add_argument("--title", help="Title of the journal entry (for add/delete action)")
    parser.add_argument("--new-title", help="New title for editing an entry")
    parser.add_argument("--content", help="Content of the journal entry (for add action)")
    parser.add_argument("--new-content", help="New content for editing an entry")
    parser.add_argument("--keyword", help="Keyword to search in journal entries (for search action)")
    parser.add_argument("--format", choices=["txt", "json"], default="txt", help="Export format (txt or json)")
    parser.add_argument("--filename", help="Custom filename for export (optional)")
    parser.add_argument("--import-format", choices=["txt", "json"], default="json", help="Import format (txt or json)")
    parser.add_argument("--import-filename", help="Custom filename for import (optional)")

    args = parser.parse_args()
    journal = Journal()

    if args.action == "add":
        if not args.title or not args.content:
            print("Title and content are required to add an entry.")
            return
        entry = journal.add_entry(args.title, args.content)
        print(f"Entry added:\n{entry}")

    elif args.action == "list":
        entries = journal.list_entries()
        for entry in entries:
            print(entry)

    elif args.action == "delete":
        if not args.title:
            print("Title is required to delete an entry.")
        else:
            journal.delete_entry(args.title)

    elif args.action == "search":
        if not args.keyword:
            print("Keyword is required for search.")
        else:
            journal.search_entries(args.keyword)
    
    elif args.action == "edit":
        if not args.title:
            print("Title is required to edit an entry")
        else:
            journal.edit_entry(args.title, args.new_title, args.new_content)

    elif args.action == "export":
        journal.export_entries(file_format=args.format, filename=args.filename if args.filename else "journal_export")

    elif args.action == "import":
        journal.import_entries(file_format=args.import_format, filename=args.import_filename
    if args.import_filename else "journal_import")
        
    elif args.action == "count":
        journal.count_entries()

if __name__ == "__main__":
    main()