from PyQt6.QtCore import QThread
import socket
import time


class MessageSender(QThread):

    def __init__(self, ip_adress, port):
        super().__init__()
        self.adress = ip_adress
        self.port = port
        self.socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (self.adress, self.port)
        self.running = True
        self.queue = []
        print("Сэндер запущен")

    def run(self):
        while self.running:
            if len(self.queue) > 0:
                text, text_type= self.queue.pop()    
                msg = f"{text}`{text_type}"
                self.socket.sendto(msg.encode(), self.server_address)
            else:
                time.sleep(0.025)


    #Slot
    def send(self,text,text_type):       
        self.queue.append((text, text_type)) 
        print(self.queue)   
    
    def stop(self):
        self.running = False




    