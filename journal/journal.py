import json
import os
import re
from .entry import JournalEntry

JOURNAL_FILE = "journal.json"

class Journal:
    def __init__(self):
        self.entries = []
        self.load_entries()

    def load_entries(self):
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, "r") as f:
                data = json.load(f)
                self.entries = [JournalEntry(**entry) for entry in data]

    def save_entries(self):
        with open(JOURNAL_FILE, "w") as f:
            json.dump([entry.to_dict() for entry in self.entries], f, indent=4)

    def add_entry(self, title, content):
        entry = JournalEntry(title, content)
        self.entries.append(entry)
        self.save_entries()
        return entry
    
    def list_entries(self):
        """Lists all journal entries sorted by date (newest first)."""
        sorted_entries = sorted(self.entries, key=lambda e: e.date, reverse=True)
        for entry in sorted_entries:
            print(entry)
    
    def search_entries(self, keyword):
        """Searches for journal entries containing the keyword and highlights matches."""
        keyword_lower = keyword.lower()
        results = []

        for entry in self.entries:
            if keyword_lower in entry.content.lower():
                highlighted_content = re.sub(f"({keyword})", r"\033[1;32m\1\033[0m", entry.content, flags=re.IGNORECASE)
                highlighted_entry = f"[{entry.date}] {entry.title}\n{highlighted_content}\n"
                results.append(highlighted_entry)

            if results:
                for result in results:
                    print(result)
            else:
                print("No matching entries found.")
    
    def delete_entry(self, title):
        """Deletes a journal entry by title."""
        self.entries = [entry for entry in self.entries if entry.title.lower() != title.lower()]
        self.save_entries()
        print(f"Entry '{title}' deleted successfully.")

    def edit_entry(self, title, new_title=None, new_content=None):
        """Edits an existing journal entry by title."""
        for entry in self.entries:
            if entry.title.lower() == title.lower():
                if new_title:
                    entry.title = new_title
                if new_content:
                    entry.content = new_content
                self.save_entries()
                print(f"Entry '{title}' updated successfully.")
                return print(f"Entry '{title}' not found.")
            
    def export_entries(self, file_format="txt", filename="journal_export"):
        """Exports journal entries to a .txt or .json file."""
        if file_format == "json":
            filename = f"{filename}.json"
            with open(filename, "w") as f:
                json.dump([entry.to_dict() for entry in self.entries], f, indent=4)
        else:  # Default to text format
            filename = f"{filename}.txt"
            with open(filename, "w") as f:
                for entry in self.entries:
                    f.write(str(entry) + "\n---\n")
            print(f"Entries exported to {filename}")

    def import_entries(self, file_format="json", filename="journal_import"):
        """Imports journal entries from a .json or .txt file."""
        filename = f"{filename}.{filename}"

        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return
        
        if file_format == "json":
            with open(filename, "r") as f:
                data = json.load(f)
                for entry in data:
                    self.entries.append(JournalEntry(**entry))
        else:  # Import from .txt format
            with open(filename, "r") as f:
                content = f.read().strip().split("\n---\n")
                for entry_text in content:
                    lines = entry_text.strip().split("\n", 1)
                    if len(lines) < 2:
                        continue
                    date_title = lines[0].strip("[]").split(" ", 1)
                    if len(date_title) < 2:
                        continue
                    entry_date, entry_title = date_title
                    entry_content = lines[1].strip()
                    self.entries.append(JournalEntry(entry_title, entry_content, entry_date))

        self.save_entries()
        print(f"Entries imported successfully from {filename}")

    def count_entries(self):
        """Returns the total number of journal entries"""
        print(f"Total journal entries: {len(self.entries)}")