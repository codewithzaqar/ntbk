import argparse
from journal.journal import Journal

def main():
    parser = argparse.ArgumentParser(description="Simple Journal CLI")
    parser.add_argument("action", choices=["add", "list", "search", "delete", "edit", "export"], help="Action to perform")
    parser.add_argument("--title", help="Title of the journal entry (for add/delete action)")
    parser.add_argument("--new-title", help="New title for editing an entry")
    parser.add_argument("--content", help="Content of the journal entry (for add action)")
    parser.add_argument("--new-content", help="New content for editing an entry")
    parser.add_argument("--keyword", help="Keyword to search in journal entries (for search action)")
    parser.add_argument("--format", choices=["txt", "json"], default="txt", help="Export format (txt or json)")
    parser.add_argument("--filename", help="Custom filename for export (optional)")

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
            return
        results = journal.search_entries(args.keyword)
        for entry in results:
            print(entry)
    
    elif args.action == "edit":
        if not args.title:
            print("Title is required to edit an entry")
        else:
            journal.edit_entry(args.title, args.new_title, args.new_content)

    elif args.action == "export":
        journal.export_entries(file_format=args.format, filename=args.filename if args.filename else "journal_export")

if __name__ == "__main__":
    main()