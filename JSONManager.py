import json
import os

class NoteManager:
    def __init__(self):
        # Имя файла JSON
        self.filename = "notes.json"
        # Словарь заметок
        self.notes = {}
        # Загружаем заметки из файла при инициализации
        self.load_notes()

    def load_notes(self):
        """Загружает заметки из JSON-файла."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    self.notes = json.load(file)
                except json.JSONDecodeError:
                    self.notes = {}
        else:
            self.save_notes(self.notes)

    def save_notes(self, notes):
        """Сохраняет заметки в JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)

    def add_note(self, title, content):
        """Добавляет новую заметку."""
        self.notes[title] = content
        self.save_notes()

    def delete_note(self, title):
        """Удаляет заметку."""
        if title in self.notes:
            del self.notes[title]
            self.save_notes()
