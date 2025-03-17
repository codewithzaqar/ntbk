import argparse
from journal.journal import Journal

def main():
    parser = argparse.ArgumentParser(description="Simple Journal CLI")
    parser.add_argument("action", choices=["add", "list", "search"], help="Action to perform")
    parser.add_argument("--title", help="Title of the journal entry (for add action)")
    parser.add_argument("--content", help="Content of the journal entry (for add action)")
    parser.add_argument("--keyword", help="Keyword to search in journal entries (for search action)")

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

    elif args.action == "search":
        if not args.keyword:
            print("Keyword is required for search.")
            return
        results = journal.search_entries(args.keyword)
        for entry in results:
            print(entry)

if __name__ == "__main__":
    main()