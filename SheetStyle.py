style = """
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
            QPushButton:pressed {
                        background-color: #2b2b2b;
                    }
        """