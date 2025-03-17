from datetime import datetime

class JournalEntry:
    def __init__(self, title, content, date=None):
        self.title = title
        self.content = content
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {"title": self.title, "content": self.content, "date": self.date}
    
    def __str__(self):
        return f"[{self.date}] {self.title}\n{self.content}\n"