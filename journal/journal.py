import json
import os
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
        return self.entries
    
    def search_entries(self, keyword):
        return [entry for entry in self.entries if keyword.lower() in entry.content.lower()]
    
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