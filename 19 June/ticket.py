from random import randint
from person import Person

class Ticket:
    number = 0
    train_id = 0
    source = ""
    destination = ""
    wagon = 0
    seat = 0
    datetime = ""
    passenger: Person = False

    def __init__(self, train_id, source, destination, date, time, person):
        self.train_id = train_id
        self.source = source
        self.destination = destination
        self.date= date
        self.time = time
        self.passenger = person
        self.number = randint(100000, 999999)
        self.wagon = randint(1, 12)
        self.seat = randint(1, 32)

    def __repr__(self):
        info = f"""Билет номер: {self.number}\nНа имя: {self.passenger.first_name} {self.passenger.last_name}\nИз {self.source} в {self.destination},\nНомер поезда: № {self.train_id}\nДата: {self.date}, Время: {self.time}"""
        return info

