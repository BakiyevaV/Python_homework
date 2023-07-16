from random import randint

class Person:
    balance = 0
    iin = 0
    birth_date = ""
    first_name = ""
    last_name = ""
    ticket = False

    def __init__(self, name, last_name, birth_date):
        self.first_name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.iin = randint(100000000000, 999999999999)

    def show_info(self):
        info = f"""Человек: {self.first_name} {self.last_name},
        Дата рождения: {self.birth_date},
        ИИН: {self.iin}, денег: {self.balance}"""
        print(info)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        return 0

