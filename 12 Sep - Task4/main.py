import sys
from PyQt6.QtWidgets import QApplication
from Task_4 import MyWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

