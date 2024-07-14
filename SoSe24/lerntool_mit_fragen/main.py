import sys
from PyQt5.QtWidgets import QApplication
from project_selection import ProjectSelection

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set application style
    app.setStyle("Fusion")
    

    window = ProjectSelection()
    window.show()

    sys.exit(app.exec_())
