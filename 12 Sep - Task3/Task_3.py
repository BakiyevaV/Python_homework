from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QMainWindow, QPushButton,QLabel
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("myui.ui",self)

class TextDisplayer(QThread):
    def __init__(self):
        super().__init__()
        self.window = MyWindow()
        self.window.show()

    def run(self):
        button = self.window.findChild(QPushButton, "pushButton")
        print(button)
        button.clicked.connect(self.open_file)

    def open_file (self):
        print("Кнопка нажата")
        with open ("input.txt","r",encoding="UTF-8") as file:
            text = file.read()
            file.close()
        print(text)
        self.display_text(text)
    
    def display_text(self,text):
        my_display = self.window.findChild(QLabel, "label")
        my_display.setText(text)



