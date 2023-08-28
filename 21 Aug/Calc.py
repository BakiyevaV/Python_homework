import sys
from PyQt5.QtWidgets import *

def calc():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Калькулятор")
    central_widget = QWidget()
    window.setCentralWidget(central_widget)
    grid = QGridLayout(central_widget)

    result = QLineEdit()

    btn_c = QPushButton("C")
    btn_last = QPushButton("<=")

    btn0 = QPushButton("0")
    btn1 = QPushButton("1")
    btn2 = QPushButton("2")
    btn3 = QPushButton("3")
    btn4 = QPushButton("4")
    btn5 = QPushButton("5")
    btn6 = QPushButton("6")
    btn7 = QPushButton("7")
    btn8 = QPushButton("8")
    btn9 = QPushButton("9")

    btn_sum = QPushButton("+")
    btn_sub = QPushButton("-")
    btn_mult = QPushButton("*")
    btn_div = QPushButton("/")

    btn_res = QPushButton("=")

    grid.addWidget(result, 0, 0, 1, 4)

    grid.addWidget(btn_c, 1, 0)
    grid.addWidget(btn_last, 1, 1)
    grid.addWidget(btn_res, 1, 2, 1, 2)


    grid.addWidget(btn7, 2, 0)
    grid.addWidget(btn8 , 2, 1)
    grid.addWidget(btn9, 2, 2)
    grid.addWidget(btn4 , 3, 0)
    grid.addWidget(btn5 , 3, 1)
    grid.addWidget(btn6, 3, 2)
    grid.addWidget(btn1, 4, 0)
    grid.addWidget(btn2, 4, 1)
    grid.addWidget(btn3, 4, 2)
    grid.addWidget(btn0, 5, 0, 1, 3)


    grid.addWidget(btn_div, 2, 3)
    grid.addWidget(btn_mult, 3, 3)
    grid.addWidget(btn_sub, 4, 3)
    grid.addWidget(btn_sum, 5, 3)

    window.setFixedSize(500, 500)
    result.setFixedSize(480,90)

    buttons_list = [btn_c, btn_last, btn0, btn1, btn2, btn3, btn4, btn5, btn6,
                    btn7, btn8, btn9, btn_sum, btn_sub, btn_mult,
                    btn_div, btn_res]

    for button in buttons_list:
        button.setFixedHeight(70)

    buttons_list2 = [ btn0, btn1, btn2, btn3, btn4, btn5, btn6,
                    btn7, btn8, btn9]

    for button in buttons_list2:
        button.setStyleSheet('background: rgb(53,58,78); border-radius: 5px; color: rgb(241,242,243); font-size: 16px;')

    buttons_list3 = [btn_c, btn_last, btn_sum, btn_sub, btn_mult,
                    btn_div, btn_res]

    for button in buttons_list3:
        button.setStyleSheet('background: rgb(44,49,69); border-radius: 5px; color: rgb(241,242,243); font-size: 16px;')

    result.setStyleSheet('border: 0px;')

    window.setStyleSheet('background: rgb(26,31,50);color: rgb(241,242,243); font-size: 30px;')
    window.show()
    app.exec()

if __name__ == '__main__':
    calc()
