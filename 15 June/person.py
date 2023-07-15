from random import randint 
class Person:
    def __init__(self, first_name, last_name,iin,balance=0, order = False):
        self.first_name = first_name
        self.last_name = last_name
        self.iin = iin
        self.balance = balance
        self.order = False

    
    def get_pay(self, summ):
        difference = self.balance - summ
        if difference < 0:
            message = "У вас недостаточно средств на счете"
            print(message)
            return False
        else:
            message = "Оплата прошла."
            print(message)
            return True
    



        
        


    
