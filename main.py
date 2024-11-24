import sys

from PyQt6.QtWidgets import QApplication

from NoteApp import NoteApp
from JSONManager import NoteManager

# Запуск приложения
app = QApplication(sys.argv)
manager = NoteManager()
window = NoteApp(manager.notes)
window.show()
sys.exit(app.exec())
