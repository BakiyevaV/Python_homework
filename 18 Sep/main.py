import sys
from PyQt6.QtWidgets import QApplication
from message_receiver import MessageReceiver
from message_sender import MessageSender
from gui import Gui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    server = MessageReceiver(9900)
    client = MessageSender("127.0.0.1", 9900)
    gui = Gui()
    client.start()
    server.start()
    gui.start()

    gui.message.connect(client.send)

    app.exec()