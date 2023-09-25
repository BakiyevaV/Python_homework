from PyQt6.QtCore import QThread
import PyQt6.QtWidgets as qt
from PyQt6.QtWidgets import QMainWindow, QPushButton,QLabel, QFileDialog
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("myui.ui",self)

# class MyWidget(qt.QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi("open_files.ui",self)
    
class TextDisplayer(QThread):
    def __init__(self):
        super().__init__()
        self.window = MyWindow()
        # self.files = MyWidget()
        self.window.show()

    def run(self):
        button = self.window.findChild(QPushButton, "pushButton")
        print(button)
        button.clicked.connect(self.open_file)

    def open_file (self):
        fname, _ = QFileDialog.getOpenFileName(self.window, "Open File", "$HOME", "All Files (*);; Python Files (*.py);; PNG Files (*.png);; TXT Files (*.txt)")
        # print(fname)
        # print("Кнопка нажата")
        with open (fname,"r",encoding="UTF-8") as file:
            text = file.read()
            file.close()
        print(text)
        self.display_text(text)
    
    def display_text(self,text):
        my_display = self.window.findChild(QLabel, "label")
        my_display.setText(text)



