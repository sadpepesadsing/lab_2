from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QDialog, QTextEdit

import NoteEditorStyle

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
        self.setStyleSheet(NoteEditorStyle.style)

        # Подключение сигналов
        self.save_button.clicked.connect(self.accept)  # Закрыть диалог с результатом "Сохранить"
        self.cancel_button.clicked.connect(self.reject)  # Закрыть диалог без сохранения