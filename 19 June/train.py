from random import randint


class Train:
    def __init__(self,train_id, kassa, source, destination, date, time):
        self.source = source
        self.destination = destination
        self.date = date
        self.time = time
        self.train_id = train_id
        self.kassa = kassa
        kassa.register_train(self)

    def go(self, passenger):
        ticket = self.kassa.get_ticket(passenger, self.train_id, self.date, self.time)
        if ticket:
            print(f'Вы поехали из {self.source} в {self.destination}\nПриехали')
            self.kassa.delete_ticket(ticket)
        else:
            print("У вас нет билета на этот поезд")


