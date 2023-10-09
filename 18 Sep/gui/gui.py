from PyQt6.QtCore import QThread,pyqtSignal
from PyQt6.QtWidgets import *
import sys
 
class Gui(QThread):
    message = pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.running = True

        
    def run(self):
        print("Gui запущен")
        while self.running:
            msg = input()
            if msg:
                self.message.emit(msg,"public")
                print("Сигнал отправлен")

    
    def stop(self):
        self.running = False




