from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QPushButton,QLabel, QFileDialog
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MyWindow, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super().__init__()
        uic.loadUi("myui.ui",self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.display = self.findChild(QLabel, "label")
        self.button.clicked.connect(self.get_file)

    def get_file (self):
        self.textDisplayer = TextDisplayer(file_name="input.txt")
        self.textDisplayer.textIsReady.connect(self.display_text)
        self.textDisplayer.start()
        
    #Slot
    def display_text(self,text):
        self.display.setText(text)

class TextDisplayer(QThread):
    textIsReady = pyqtSignal(str)

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        with open (self.file_name,"r",encoding="UTF-8") as file:
            text = file.read()
            if text:
               self.textIsReady.emit(text) 
            file.close()
            
    



