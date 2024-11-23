import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QDialog, QTextEdit, QWidget


class NoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f7f7;
                font-family: Arial;
                font-size: 14px;
                border-radius: 4px;
                
            }
            QListWidget {
                background-color: white;
                border: 1px solid #000000;
                padding: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border: 1px solid #000000;
                border-radius: 4px;
            }
            QListWidget::item:selected {
                background-color: #545252;
                color: white;
            }
            QLineEdit {
                border: 1px solid #000000;
                padding: 5px;
                border-radius: 4px;
            }
            QPushButton {
                background-color: black;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: grey;
            }
        """)

        self.setWindowTitle("Менеджер заметок")
        self.setGeometry(100, 100, 400, 600)

        # Компоновка
        self.layout = QVBoxLayout(self)

        # Список заметок
        self.note_list = QListWidget(self)
        self.layout.addWidget(self.note_list)

        # Поле для добавления заметки
        self.add_field = QLineEdit(self)
        self.add_field.setPlaceholderText("Введите название новой заметки")
        self.layout.addWidget(self.add_field)

        # Кнопка для добавления
        self.add_button = QPushButton("Добавить заметку", self)
        self.layout.addWidget(self.add_button)

        # Хранение заметок
        self.notes = {}

        # Подключение сигналов
        self.add_button.clicked.connect(self.add_note)
        self.note_list.itemClicked.connect(self.open_note)

    def add_note(self):
        """Добавление новой заметки"""
        title = self.add_field.text()
        if title and title not in self.notes:
            self.notes[title] = ""  # Пустой текст заметки
            self.note_list.addItem(title)
            self.add_field.clear()

    def open_note(self, item):
        """Открытие окна для редактирования заметки"""
        title = item.text()
        content = self.notes.get(title, "")
        dialog = NoteEditor(title, content)
        if dialog.exec():  # Если нажали "Сохранить"
            self.notes[title] = dialog.text_edit.toPlainText()  # Сохраняем текст


class NoteEditor(QDialog):
    def __init__(self, title, content):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 600, 400)

        # Компоновка
        self.layout = QVBoxLayout(self)

        # Поле редактирования текста
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText(content)
        self.layout.addWidget(self.text_edit)

        # Кнопки "Сохранить" и "Отмена"
        self.save_button = QPushButton("Сохранить", self)
        self.cancel_button = QPushButton("Отмена", self)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.cancel_button)

        # Подключение сигналов
        self.save_button.clicked.connect(self.accept)  # Закрыть диалог с результатом "Сохранить"
        self.cancel_button.clicked.connect(self.reject)  # Закрыть диалог без сохранения


# Запуск приложения
app = QApplication(sys.argv)
window = NoteApp()
window.show()
sys.exit(app.exec())
