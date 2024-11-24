style = """
            QMenu {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            QMenu::item {
                padding: 10px;
                color: #c43131;
                background-color: white;
                font-size: 14px;
            }

            QMenu::item:selected {
                background-color: #c43131;
                color: white;
            }

            QMenu::item:disabled {
                color: #ccc;
            }

            QMenu::separator {
                height: 1px;
                background-color: #ccc;
            }
        """