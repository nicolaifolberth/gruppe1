import os
import json
import sys
import random
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QAction, QApplication, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QIcon

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class QuizApp(QMainWindow):
    def __init__(self, project_name, is_dark_mode):
        super().__init__()
        self.project_name = project_name
        self.is_dark_mode = is_dark_mode
        self.correct_answers_first_try = 0
        self.total_questions_first_try = 0
        self.incorrect_questions = []
        self.init_ui()
        self.apply_theme()

    def init_ui(self):
        self.setWindowTitle(f'Projekt: {self.project_name}')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.load_questions()
        self.current_question_index = -1

        self.question_label = QLabel(self.central_widget)
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet("font-size: 18px; margin-bottom: 20px;")

        self.code_snippet = QTextEdit(self.central_widget)
        self.code_snippet.setReadOnly(True)
        self.code_snippet.setVisible(False)

        self.answer_buttons = [QPushButton(self.central_widget) for _ in range(4)]
        for btn in self.answer_buttons:
            btn.setStyleSheet("font-size: 16px; padding: 10px;")
            btn.clicked.connect(self.check_answer)

        self.status_label = QLabel(self.central_widget)
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("font-size: 18px; color: blue; margin-top: 20px;")

        self.home_button = QPushButton(self)
        self.home_button.setIcon(QIcon(resource_path('utils/home.svg')))
        self.home_button.clicked.connect(self.back_to_main_menu)

        self.theme_button = QPushButton(self)
        self.theme_button.setIcon(QIcon(resource_path('utils/moon.svg' if self.is_dark_mode else resource_path('utils/sun.svg'))))
        self.theme_button.setCheckable(True)
        self.theme_button.setChecked(True)
        self.theme_button.clicked.connect(self.toggle_theme)

        self.question_progress = QLabel(self.central_widget)
        self.question_progress.setStyleSheet("font-size: 14px; margin-top: 20px; text-align: center;")

        self.correct_percentage = QLabel(self.central_widget)
        self.correct_percentage.setStyleSheet("font-size: 14px; margin-top: 20px; text-align: center;")

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.home_button)
        top_layout.addWidget(self.theme_button)
        top_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.question_label)
        main_layout.addWidget(self.code_snippet)
        for btn in self.answer_buttons:
            main_layout.addWidget(btn)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.question_progress, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.correct_percentage, alignment=Qt.AlignCenter)
        self.central_widget.setLayout(main_layout)

        self.randomize_questions()
        self.next_question()

    def load_questions(self):
        project_file = resource_path(os.path.join('projects', self.project_name + '.json'))
        if os.path.exists(project_file):
            with open(project_file, 'r') as f:
                self.questions = json.load(f)
        else:
            self.questions = []

    def randomize_questions(self):
        self.questions += self.incorrect_questions
        random.shuffle(self.questions)
        self.incorrect_questions = []

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index >= len(self.questions):
            QMessageBox.information(self, 'Quiz Beendet', 'Du hast alle Fragen beantwortet!')
            self.randomize_questions()
            self.current_question_index = 0
            self.correct_answers_first_try = 0
            self.total_questions_first_try = 0
        self.show_question(self.current_question_index)
        self.status_label.setText("")
        self.set_buttons_enabled(True)
        self.update_question_progress()

    def show_question(self, index):
        question = self.questions[index]
        self.question_label.setText(question['frage'])

        if 'code_snippet' in question and question['code_snippet'].strip():
            self.code_snippet.setMarkdown(f"```{question['code_snippet']}```")
            self.code_snippet.setVisible(True)
        else:
            self.code_snippet.setVisible(False)

        random.shuffle(question['antworten'])
        for i, answer in enumerate(question['antworten']):
            self.answer_buttons[i].setText(answer['text'])
            self.answer_buttons[i].setProperty('korrekt', answer['korrekt'])
            self.answer_buttons[i].setStyleSheet("font-size: 16px; padding: 10px;")
            self.answer_buttons[i].show()
        for i in range(len(question['antworten']), 4):
            self.answer_buttons[i].hide()

    def check_answer(self):
        button = self.sender()
        correct = button.property('korrekt')
        if correct:
            button.setStyleSheet("background-color: green; font-size: 16px; padding: 10px;")
            self.status_label.setText("Das ist korrekt!")
            self.correct_answers_first_try += 1
        else:
            button.setStyleSheet("background-color: red; font-size: 16px; padding: 10px;")
            self.status_label.setText("Das ist falsch!")
            for btn in self.answer_buttons:
                if btn.property('korrekt'):
                    btn.setStyleSheet("background-color: green; font-size: 16px; padding: 10px;")
            self.incorrect_questions.append(self.questions[self.current_question_index])
        self.total_questions_first_try += 1
        self.set_buttons_enabled(False)
        QTimer.singleShot(2000, self.next_question)
        self.update_correct_percentage()

    def set_buttons_enabled(self, enabled):
        for btn in self.answer_buttons:
            btn.setEnabled(enabled)

    def toggle_theme(self):
        if self.is_dark_mode:
            self.set_light_mode()
            self.theme_button.setIcon(QIcon(resource_path('utils/sun.svg')))
        else:
            self.set_dark_mode()
            self.theme_button.setIcon(QIcon(resource_path('utils/moon.svg')))
        self.is_dark_mode = not self.is_dark_mode

    def apply_theme(self):
        if self.is_dark_mode:
            self.set_dark_mode()
        else:
            self.set_light_mode()

    def set_dark_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        QApplication.instance().setPalette(palette)

        self.setStyleSheet("""
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: #353535;
                color: white;
                border: 1px solid #555555;
            }
            QTextEdit {
                background-color: #353535;
                color: white;
                border: 1px solid #555555;
            }
        """)

    def set_light_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.white)
        palette.setColor(QPalette.WindowText, Qt.black)
        palette.setColor(QPalette.Base, QColor(240, 240, 240))
        palette.setColor(QPalette.AlternateBase, Qt.white)
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.black)
        palette.setColor(QPalette.Text, Qt.black)
        palette.setColor(QPalette.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.white)
        QApplication.instance().setPalette(palette)

        self.setStyleSheet("""
            QLabel {
                color: black;
            }
            QPushButton {
                background-color: #f0f0f0;
                color: black;
                border: 1px solid #aaaaaa;
            }
            QTextEdit {
                background-color: #f0f0f0;
                color: black;
                border: 1px solid #aaaaaa;
            }
        """)

    def back_to_main_menu(self):
        from project_selection import ProjectSelection
        self.project_selection = ProjectSelection()
        self.project_selection.show()
        self.project_selection.raise_()
        self.project_selection.activateWindow()
        self.close()

    def update_question_progress(self):
        total_questions = len(self.questions) + len(self.incorrect_questions)
        answered_questions = self.current_question_index + 1
        self.question_progress.setText(f'{answered_questions} von {total_questions} Fragen beantwortet')

    def update_correct_percentage(self):
        if self.total_questions_first_try > 0:
            percentage = (self.correct_answers_first_try / self.total_questions_first_try) * 100
            self.correct_percentage.setText(f'Prozent der korrekt beantworteten Fragen: {percentage:.2f}%')
        else:
            self.correct_percentage.setText('')
