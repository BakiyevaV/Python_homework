import sys
from PyQt6.QtWidgets import QApplication
from Task_4 import TextDisplayer


if __name__ == "__main__":
    app = QApplication(sys.argv)
    text_displayer = TextDisplayer()
    text_displayer.start()
    app.exec()

