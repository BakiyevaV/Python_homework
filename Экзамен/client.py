import socket
import json
from logger import log

class XoClient():
    print("XoClient")
    def __init__(self, hostname, port):
        self.socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (hostname, port)

    def char_request(self):
        log.i("Нужна масть")
        ask = {'char_request': ''}
        ask_r = json.dumps(ask, ensure_ascii=False)
        log.t(self.server_address)
        self.socket.sendto(ask_r.encode(), self.server_address)
        char = self.receive()
        return char
    
    def send(self, row, col):
        move = "{'row': %s, 'col': %s}" %(row, col)
        strn = json.dumps(move, ensure_ascii=False)
        self.socket.sendto(strn.encode(), self.server_address)

    def receive(self):
        log.i("случаю ответ от сервера")
        data = self.socket.recv(1024)
        response= json.loads(data)
        keys = list(response.keys())
        if keys[0] == 'char':
            log.i("ответ",response)
            return keys
            
    




