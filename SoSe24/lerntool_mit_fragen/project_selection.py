import os
import sys
import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox, QMenu, QAction, QFileDialog, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QIcon
from question_manager import QuestionManager
from quiz_app import QuizApp

class ProjectSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.is_dark_mode = True
        self.init_ui()
        self.toggle_theme()

    def init_ui(self):
        self.setWindowTitle('Fragenkatalog Auswahl')
        self.setGeometry(100, 100, 400, 300)

        self.project_list = QListWidget(self)
        self.project_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.project_list.customContextMenuRequested.connect(self.open_context_menu)
        self.project_list.doubleClicked.connect(self.open_project)

        self.load_projects()

        self.add_project_button = QPushButton('Neuer Fragenkatalog', self)
        self.add_project_button.clicked.connect(self.add_project)

        self.import_button = QPushButton('Fragenkatalog importieren', self)
        self.import_button.clicked.connect(self.import_project)

        self.theme_button = QPushButton(self)
        self.update_theme_icon()
        self.theme_button.setCheckable(True)
        self.theme_button.setChecked(True)
        self.theme_button.clicked.connect(self.toggle_theme)

        self.easter_egg_button = QPushButton()
        self.easter_egg_button.setIcon(QIcon('utils/info.svg'))
        self.easter_egg_button.clicked.connect(self.show_easter_egg)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.theme_button)
        top_layout.addWidget(self.easter_egg_button)
        top_layout.addStretch()

        self.layout = QVBoxLayout()
        self.layout.addLayout(top_layout)
        self.layout.addWidget(self.project_list)
        self.layout.addWidget(self.add_project_button)
        self.layout.addWidget(self.import_button)
        self.setLayout(self.layout)

    def load_projects(self):
        if not os.path.exists('projects'):
            os.makedirs('projects')
        projects = os.listdir('projects')
        self.project_list.clear()
        self.project_list.addItems([proj.replace('.json', '') for proj in projects if proj.endswith('.json')])

    def add_project(self):
        project_name, ok = QInputDialog.getText(self, 'Neuer Fragenkatalog', 'Projektname eingeben:')
        if ok and project_name:
            project_file = os.path.join('projects', project_name + '.json')
            if not os.path.exists(project_file):
                with open(project_file, 'w', encoding='utf-8') as f:
                    json.dump([], f)
                self.load_projects()
            else:
                QMessageBox.warning(self, 'Warnung', 'Projekt existiert bereits!')

    def import_project(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Fragenkatalog importieren', '', 'JSON Dateien (*.json)')
        if file_name:
            project_name, ok = QInputDialog.getText(self, 'Neuer Fragenkatalog', 'Projektname eingeben:')
            if ok and project_name:
                project_file = os.path.join('projects', project_name + '.json')
                if not os.path.exists(project_file):
                    with open(file_name, 'r', encoding='utf-8') as f:
                        try:
                            data = json.load(f)
                            if isinstance(data, list) and all('frage' in q and 'antworten' in q for q in data):
                                with open(project_file, 'w', encoding='utf-8') as pf:
                                    json.dump(data, pf, ensure_ascii=False, indent=4)
                                self.load_projects()
                            else:
                                QMessageBox.warning(self, 'Warnung', 'Ungültiges JSON-Format. Erwartet wird eine Liste von Fragen mit den erforderlichen Feldern.')
                        except json.JSONDecodeError:
                            QMessageBox.warning(self, 'Warnung', 'Fehler beim Lesen der JSON-Datei.')
                else:
                    QMessageBox.warning(self, 'Warnung', 'Projekt existiert bereits!')

    def open_context_menu(self, position):
        item = self.project_list.itemAt(position)
        if not item:
            return

        context_menu = QMenu()
        manage_questions_action = QAction('Fragen verwalten', self)
        manage_questions_action.triggered.connect(self.manage_questions)
        rename_action = QAction('Umbenennen', self)
        rename_action.triggered.connect(self.rename_project)
        merge_action = QAction('Zusammenfügen', self)
        merge_action.triggered.connect(self.prepare_merge_projects)
        delete_action = QAction('Löschen', self)
        delete_action.triggered.connect(self.delete_project)
        context_menu.addAction(manage_questions_action)
        context_menu.addAction(rename_action)
        context_menu.addAction(merge_action)
        context_menu.addAction(delete_action)
        context_menu.exec_(self.project_list.mapToGlobal(position))

    def manage_questions(self):
        item = self.project_list.currentItem()
        if item:
            project_name = item.text()
            self.question_manager = QuestionManager(self, project_name, self.is_dark_mode)
            self.question_manager.show()
            self.question_manager.raise_()
            self.question_manager.activateWindow()
            self.question_manager.closed.connect(self.on_question_manager_closed)
            self.hide()

    def on_question_manager_closed(self):
        self.show()

    def rename_project(self):
        item = self.project_list.currentItem()
        if not item:
            QMessageBox.warning(self, 'Warnung', 'Bitte wählen Sie ein Projekt aus!')
            return
        old_project_name = item.text()
        new_project_name, ok = QInputDialog.getText(self, 'Projekt umbenennen', 'Neuen Projektnamen eingeben:')
        if ok and new_project_name:
            old_project_file = os.path.join('projects', old_project_name + '.json')
            new_project_file = os.path.join('projects', new_project_name + '.json')
            if not os.path.exists(new_project_file):
                os.rename(old_project_file, new_project_file)
                self.load_projects()
            else:
                QMessageBox.warning(self, 'Warnung', 'Projektname existiert bereits!')

    def prepare_merge_projects(self):
        item = self.project_list.currentItem()
        if not item:
            QMessageBox.warning(self, 'Warnung', 'Bitte wählen Sie ein Projekt aus!')
            return
        self.project_to_merge = item.text()
        QMessageBox.information(self, 'Projekt auswählen', 'Wählen Sie das zweite Projekt zum Zusammenfügen aus.')
        self.project_list.itemClicked.connect(self.merge_projects)

    def merge_projects(self, item):
        if not hasattr(self, 'project_to_merge') or not self.project_to_merge:
            return

        project1 = self.project_to_merge
        project2 = item.text()
        if project1 == project2:
            QMessageBox.warning(self, 'Warnung', 'Sie können nicht dasselbe Projekt auswählen!')
            return

        project1_file = os.path.join('projects', project1 + '.json')
        project2_file = os.path.join('projects', project2 + '.json')

        with open(project1_file, 'r', encoding='utf-8') as f:
            data1 = json.load(f)
        with open(project2_file, 'r', encoding='utf-8') as f:
            data2 = json.load(f)

        merged_data = data1 + data2
        new_project_name = f"{project1}-{project2}"
        new_project_file = os.path.join('projects', new_project_name + '.json')
        with open(new_project_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=4)
        self.load_projects()
        del self.project_to_merge

    def delete_project(self):
        item = self.project_list.currentItem()
        if not item:
            QMessageBox.warning(self, 'Warnung', 'Bitte wählen Sie ein Projekt aus!')
            return
        project_name = item.text()
        project_file = os.path.join('projects', project_name + '.json')
        os.remove(project_file)
        self.load_projects()

    def open_project(self):
        selected_project = self.project_list.currentItem().text()
        self.main_window = QuizApp(selected_project, self.is_dark_mode)
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()
        self.close()

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.update_theme_icon()
        self.apply_theme()

    def update_theme_icon(self):
        self.theme_button.setIcon(QIcon('utils/moon.svg') if self.is_dark_mode else QIcon('utils/sun.svg'))

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
        palette.setColor(QPalette.Button, QColor(75, 75, 75))  # Darker gray for buttons
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        QApplication.instance().setPalette(palette)

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

    def show_easter_egg(self):
        QMessageBox.information(self, 'Über', 'Entwickler: Der Pfiff\nEmail: derpfiff@proton.me\n\nErstellt für die nächsten Jahrgänge und auf das der Fragenkatalog sich weiterhin nicht groß ändert.\n\nFeedback und Bug Reports sind herzlich willkommen!\nTrage gerne weitere Fragen zusammen, entwickle das Tool weiter oder refactore den Code nach Belieben.\n\nHappy Coding und viel Erfolg beim Lernen! 🚀')
