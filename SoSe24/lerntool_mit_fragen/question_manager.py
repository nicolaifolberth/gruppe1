import os
import json
import sys
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox,
    QHBoxLayout, QLineEdit, QLabel, QTextEdit, QCheckBox, QGridLayout
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPalette

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class QuestionManager(QDialog):
    closed = pyqtSignal()  # Signal to be emitted when the dialog is closed

    def __init__(self, parent, project_name, is_dark_mode):
        super().__init__(parent)
        self.parent = parent
        self.project_name = project_name
        self.is_dark_mode = is_dark_mode
        self.current_question_index = None
        self.questions = []
        self.load_questions()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f"Fragen Manager - {self.project_name}")
        self.setMinimumSize(1200, 800)

        self.question_list = QListWidget(self)
        self.question_list.setMinimumWidth(400)
        self.question_list.currentRowChanged.connect(self.on_question_change)

        self.add_question_button = QPushButton("+", self)
        self.add_question_button.clicked.connect(self.add_question)

        question_list_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_question_button)
        question_list_layout.addLayout(button_layout)
        question_list_layout.addWidget(self.question_list)

        self.question_text = QLineEdit(self)
        self.question_text.setPlaceholderText("Frage eingeben...")
        self.question_text.textChanged.connect(self.update_question_title)

        self.answer_texts = [QTextEdit(self) for _ in range(4)]
        self.correct_checkboxes = [QCheckBox("Richtig", self) for _ in range(4)]
        self.code_snippet_text = QTextEdit(self)

        layout = QGridLayout()
        layout.addWidget(QLabel("Frage:"), 0, 0)
        layout.addWidget(self.question_text, 0, 1, 1, 3)
        layout.addWidget(QLabel("Code Schnipsel (optional):"), 1, 0)
        layout.addWidget(self.code_snippet_text, 1, 1, 1, 3)
        for i in range(4):
            layout.addWidget(QLabel(f"Antwort {i + 1}:"), i + 2, 0)
            layout.addWidget(self.answer_texts[i], i + 2, 1)
            layout.addWidget(self.correct_checkboxes[i], i + 2, 2)

        control_layout = QVBoxLayout()
        control_layout.addStretch()

        main_layout = QHBoxLayout()
        main_layout.addLayout(question_list_layout, 2)
        main_layout.addLayout(layout, 5)
        main_layout.addLayout(control_layout)

        self.setLayout(main_layout)
        self.load_question_list()
        self.apply_theme()

    def load_questions(self):
        project_file = resource_path(os.path.join('projects', f'{self.project_name}.json'))
        if os.path.exists(project_file):
            try:
                with open(project_file, 'r') as f:
                    self.questions = json.load(f)
            except json.JSONDecodeError as e:
                QMessageBox.critical(self, 'Fehler', f'Fehler beim Laden der Daten: {str(e)}')

            for question in self.questions:
                if 'antworten' not in question:
                    question['antworten'] = [
                        {"text": "Antwort 1", "korrekt": False},
                        {"text": "Antwort 2", "korrekt": False},
                        {"text": "Antwort 3", "korrekt": False},
                        {"text": "Antwort 4", "korrekt": False}
                    ]

    def save_questions(self):
        project_file = resource_path(os.path.join('projects', f'{self.project_name}.json'))
        try:
            with open(project_file, 'w') as f:
                json.dump(self.questions, f, ensure_ascii=False, indent=4)
        except IOError as e:
            QMessageBox.critical(self, 'Fehler', f'Fehler beim Speichern der Daten: {str(e)}')

    def load_question_list(self):
        self.question_list.clear()
        for question in self.questions:
            self.question_list.addItem(question['frage'])
        if not self.questions:
            self.clear_question_display()

    def display_question(self, index):
        if index == -1 or index >= len(self.questions):
            self.clear_question_display()
            return

        self.current_question_index = index
        question = self.questions[index]
        self.question_text.setText(question['frage'])
        self.code_snippet_text.setText(question.get('code_snippet', ''))
        for i in range(4):
            if i < len(question['antworten']):
                self.answer_texts[i].setText(question['antworten'][i]['text'])
                self.correct_checkboxes[i].setChecked(question['antworten'][i]['korrekt'])
            else:
                self.answer_texts[i].clear()
                self.correct_checkboxes[i].setChecked(False)

    def clear_question_display(self):
        self.current_question_index = None
        self.question_text.clear()
        self.code_snippet_text.clear()
        for i in range(4):
            self.answer_texts[i].clear()
            self.correct_checkboxes[i].setChecked(False)

    def add_question(self):
        question_text, ok = QInputDialog.getText(self, 'Frage hinzufügen', 'Frage eingeben:')
        if ok and question_text:
            new_question = {
                "frage": question_text,
                "antworten": [
                    {"text": "Antwort 1", "korrekt": False},
                    {"text": "Antwort 2", "korrekt": False},
                    {"text": "Antwort 3", "korrekt": False},
                    {"text": "Antwort 4", "korrekt": False}
                ],
                "code_snippet": ""
            }
            self.questions.append(new_question)
            self.save_questions()
            self.load_question_list()
            self.question_list.setCurrentRow(len(self.questions) - 1)
            self.display_question(len(self.questions) - 1)

    def save_current_question(self):
        if self.current_question_index is None or self.current_question_index >= len(self.questions):
            return

        if not self.validate_question_data():
            QMessageBox.warning(self, 'Warnung', 'Bitte füllen Sie alle erforderlichen Felder aus.')
            return

        self.questions[self.current_question_index]['frage'] = self.question_text.text()
        self.questions[self.current_question_index]['code_snippet'] = self.code_snippet_text.toPlainText()
        self.questions[self.current_question_index]['antworten'] = [
            {"text": self.answer_texts[i].toPlainText(), "korrekt": self.correct_checkboxes[i].isChecked()}
            for i in range(4)
        ]
        self.save_questions()

    def validate_question_data(self):
        if not self.question_text.text().strip():
            return False
        for i in range(4):
            if not self.answer_texts[i].toPlainText().strip():
                return False
        return True

    def on_question_change(self, index):
        if self.current_question_index is not None:
            self.save_current_question()
        if index >= 0 and index < len(self.questions):
            self.display_question(index)

    def update_question_title(self, new_title):
        if self.current_question_index is not None:
            self.questions[self.current_question_index]['frage'] = new_title
            self.question_list.item(self.current_question_index).setText(new_title)

    def apply_theme(self):
        palette = QPalette()
        if self.is_dark_mode:
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, Qt.white)
        else:
            palette.setColor(QPalette.Window, Qt.white)
            palette.setColor(QPalette.WindowText, Qt.black)
        self.setPalette(palette)

    def closeEvent(self, event):
        self.save_current_question()
        self.closed.emit()
        super().closeEvent(event)
