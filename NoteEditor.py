from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QDialog, QTextEdit

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
        self.setStyleSheet("""
                    QWidget {
                        background-color: #ffffff;
                    }

                    QTextEdit {
                        background-color: #f9f9f9;
                        border: 1px solid black;
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                        border-radius: 5px;
                        padding: 10px;
                    }

                    QPushButton {
                        background-color: black;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        padding: 10px;
                        font-size: 16px;
                    }

                    QPushButton:hover {
                        background-color: grey;
                    }

                    QPushButton:pressed {
                        background-color: #2b2b2b;
                    }
                """)

        # Подключение сигналов
        self.save_button.clicked.connect(self.accept)  # Закрыть диалог с результатом "Сохранить"
        self.cancel_button.clicked.connect(self.reject)  # Закрыть диалог без сохранения