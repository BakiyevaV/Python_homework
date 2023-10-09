from PyQt6.QtCore import QThread,pyqtSignal
import datetime
import socket


class MessageReceiver(QThread):
    message = pyqtSignal(str,str)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        self.running = True
        self.msg = None

    def run(self):
        print("Ресивер запущен")
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%d-%m-%Y %H:%M:%S" )
        while self.running:
            data, addr = self.socket.recvfrom(1024)
            message  = data.decode(encoding="UTF-8")
            message = message.split("`")
            print(f'Получено сообщение типа:"{message[1]}" от {addr} в [{current_time}]: {message[0]} ')
            self.message.emit(message[0], "public")
            if message[0] == "exit":
                self.stop()

    def stop(self):
        self.running = False




