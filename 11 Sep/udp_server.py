from datetime import datetime
import socket

class UDP_server():
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))

    def start(self,):
        current_time = datetime.now()
        global is_running
        is_running = True
        while is_running == True:
            data, addr = self.socket.recvfrom(1024)
            message = data.decode(encoding="UTF-8")
            print(f'Получено сообщение от {addr} {current_time}: {message} ')
            self.socket.sendto("ОК".encode(), addr)
            if message == "exit":
                self.stop()

    def stop(self):
        global is_running
        is_running = False




