from datetime import datetime
import socket
import json
from logger import log

class XoServer():
    print("XoServer")
    def __init__(self, hostname, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((hostname, port))
        self.on_char_request = None
        self.client_addr = None


    def char_response(self):
        log.i("Запрос масти")
        char = self.on_char_request()
        c = "{'char': %s}" %char
        strng = json.dumps(c, ensure_ascii=False)
        log.t("strng",strng)
        self.socket.sendto(strng.encode(), self.client_addr)

    
    def send(self, row, col):
        move = "{'row': %s, 'col': %s}" %(row, col)
        strn = json.dumps(move, ensure_ascii=False)
        self.socket.sendto(strn.encode(), self.client_addr)

    def receive(self):
        global is_running
        is_running = True
        while is_running == True:
            data, addr = self.socket.recvfrom(1024)
            data_n = data.decode(encoding="UTF-8")
            self.client_addr = addr
            dict = json.loads(data_n)
            keys = list(dict.keys())
            if keys[0] == 'char_request':
                self.char_response()
            


    





