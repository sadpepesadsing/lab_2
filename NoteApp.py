from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QListWidget, QWidget, QMenu

from NoteEditor import NoteEditor
from JSONManager import NoteManager
import ContextMenuStyle
import SheetStyle


class NoteApp(QWidget):
    def __init__(self, notes: dict = {}):
        super().__init__()
        self.setStyleSheet(SheetStyle.style)

        self.setWindowTitle("Менеджер заметок")
        self.setGeometry(100, 100, 400, 600)

        # Компоновка
        self.layout = QVBoxLayout(self)

        # Список заметок
        self.note_list = QListWidget(self)
        self.note_list.setSpacing(3)
        self.layout.addWidget(self.note_list)

        self.note_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.note_list.customContextMenuRequested.connect(self.show_context_menu)

        # Поле для добавления заметки
        self.add_field = QLineEdit(self)
        self.add_field.setPlaceholderText("Введите название новой заметки")
        self.layout.addWidget(self.add_field)

        # Кнопка для добавления
        self.add_button = QPushButton("Добавить заметку", self)
        self.layout.addWidget(self.add_button)

        # Хранение заметок
        self.notes = notes
        for title in notes:
            self.note_list.addItem(title)

        # Подключение сигналов
        self.add_button.clicked.connect(self.add_note)
        self.note_list.itemClicked.connect(self.open_note)

    def show_context_menu(self, pos):
        # Получаем элемент списка, на котором был клик
        item = self.note_list.itemAt(pos)
        if not item:
            return

        context_menu = QMenu(self)

        # Действие для удаления заметки
        delete_action = QAction("Удалить", self)
        delete_action.triggered.connect(lambda: self.delete_note(item))
        context_menu.addAction(delete_action)

        context_menu.setStyleSheet(ContextMenuStyle.style)

        # Показываем меню
        context_menu.exec(self.note_list.mapToGlobal(pos))

    def delete_note(self, item):
        # Удаляем выбранную заметку из списка
        self.note_list.takeItem(self.note_list.row(item))
        self.notes.pop(item.text())
        NoteManager().save_notes(self.notes) #Сохранение

    def add_note(self):
        """Добавление новой заметки"""
        title = self.add_field.text()
        if title and title not in self.notes:
            self.notes[title] = ""  # Пустой текст заметки
            self.note_list.addItem(title)
            self.add_field.clear()
            NoteManager().save_notes(self.notes)

    def open_note(self, item):
        """Открытие окна для редактирования заметки"""
        title = item.text()
        content = self.notes.get(title, "")
        dialog = NoteEditor(title, content)
        if dialog.exec():  # Если нажали "Сохранить"
            self.notes[title] = dialog.text_edit.toPlainText()  # Сохраняем текст
            NoteManager().save_notes(self.notes)