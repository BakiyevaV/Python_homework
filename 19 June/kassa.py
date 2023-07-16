from ticket import Ticket

class Kassa:
    balance = 0
    tickets = []
    trains = []

    def get_price(self, source, destination):
        price = (len(source) + len(destination))*1000
        return price

    def buy_ticket(self, passenger, source, destination, train):
        money = passenger.pay(self.get_price(source, destination))
        if money > 0:
            self.balance += money
            ticket = Ticket(train.train_id, source, destination, train.date,train.time, passenger)
            self.tickets.append(ticket)
            return True
        else:
            return False

    def get_ticket(self, passenger, train_number, date, time):
        for x in self.tickets:
            if x.passenger.iin == passenger.iin and x.train_id == train_number and x.date == date and x.time == time:
                return x

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)

    def register_train(self, train):
            train_parameters = {}
            train_parameters[train.train_id.strip()] = {"train_source":train.source.strip(),"train_destination":train.destination.strip(),"train_date":train.date.strip(), "train_time":train.time.strip()}
            self.trains.append(train_parameters)
            return self.trains
        
    def check_train(self, pass_source, pass_distination,date):
        pass_source = pass_source.strip()
        pass_distination = pass_distination.strip()
        for train in self.trains:
            for key, value in train.items():
                if value['train_source'] == pass_source and value['train_destination'] == pass_distination:
                    if  value['train_date']== date:
                        result = key, value['train_time'], True
                    elif  value['train_date']!= date:
                        result = key, value['train_date'], False
                elif value['train_source'] != pass_source or value['train_destination'] != pass_distination:
                    result = 0, 0, False
        return result

