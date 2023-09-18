import socket
from datetime import datetime

class UDP_Client():
    def __init__(self, ip_adress, port):
        self.adress = ip_adress
        self.port = port
        self.socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (self.adress, self.port)
    
    def create_message(self):
        current_time = datetime.now()
        is_running = True
        while is_running == True:
            message = input("Введите сообщение: ")
            self.send(message)
            response = self.receive()
            print(f"Получено сообщение от сервера в {current_time}: {response}")
            if message == "exit":
                is_running = False

    def send(self,message):             
        self.socket.sendto(message.encode(), self.server_address)
    
    def receive(self):
        data, addr = self.socket.recvfrom(1024)
        response= data.decode(encoding="UTF-8")
        return response
    




