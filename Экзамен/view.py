class XoViev():
    def show(self,some_text):
        print(some_text)

    def show_win(self):
        print("Вы выиграли!")

    def show_loose(self):
        print("Вы проиграли!")

    def input(self, char):
        print(f"Ваша масть {char}")
        move = input("Ваш ход: ")
