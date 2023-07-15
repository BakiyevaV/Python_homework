from datetime import datetime
from order import Order
class Hotel:
    def __init__(self, name,balance,room_num,single_room_cost, double_room_cost, days_quantity = 0,bed_num = 0, single_room= [], 
        double_room = [], price = 0):
        self.name = name
        self.balance = balance
        self.room_num = room_num
        self.days_quantity = days_quantity
        self.bed_num = bed_num
        self.single_room = single_room
        self.double_room = double_room 
        self.single_room_cost = single_room_cost
        self.double_room_cost = double_room_cost 
        self.price = price

    def gen_rooms(self):
        start_day = datetime.strptime("01-01-0001","%d-%m-%Y")  
        end_day = datetime.strptime("01-01-0001","%d-%m-%Y")   
        self.single_room = []
        self.double_room = []
        for i in range (1, self.room_num  + 1):
            if i % 2 == 0:
                self.double_room.append([i, start_day, end_day])
            else:
                self.single_room.append([i, start_day, end_day])
        return self.single_room, self.double_room

    def get_price(self,days_quantity, bed_num):
        if int(bed_num) == 1:
            self.price = int(days_quantity) * self.single_room_cost
        elif int(bed_num) == 2:
            self.price  = int(days_quantity) * self.double_room_cost
        return self.price  
    
    def buy_order(self, room_id, bed_num, start_day, end_day):
        if bed_num == 1:
            for room in self.single_room:
                if room[0] == room_id:
                    room[1] = start_day
                    room[2] = end_day
                else:
                    continue
        return True
    
    def check_in(self,order):
        order_num_verification= int(input("Прошу назвать номер брони: "))
        if order.order_id == order_num_verification:
            parameters_ver =input ("Укажите свое имя, фамилию и ИИН (через запятую): ")
            v_f_name, v_l_name, v_iin = [x.strip() for x in parameters_ver.split(",")]
            if v_f_name == order.visitor_name and v_l_name == order.visitor_last_name and v_iin == order.visitor_iin:
                print("Вот ваша ключ-карта. Можете располагаться.")
                status = True
            else:
                print("Указанная информация не соответствует данным брони.")
                status = False
        else: 
            print("Бронь с таким номером не найдена!")
            status = False
        return status
    
    def check_out(self,order, visitor):
        check_out_date = input("Введите дату выезда!(день-месяц-число): ") 
        end_day = datetime.strptime(check_out_date,"%d-%m-%Y")    
        if end_day > order.date_to:
            diff = end_day - order.date_to
            seconds = diff.total_seconds()
            days = seconds // 86400
            days = int(days)
            if int(order.bed_num) == 2:
                add_cash = days * self.double_room_cost
                print(f"Вы прибывали в отеле дольше чем планировалось.\nВам нужно доплатить:{add_cash}")
                stat = False
                while stat == False:
                    if visitor.get_pay(add_cash) == True:
                        print("Спасибо. До свидания")
                        result = True
                        stat = True
                    else:
                        add_bal = int(input("На какую сумму вы хотите пополнить баланс?"))
                        visitor.balance += add_bal
            if int(order.bed_num) == 1:
                add_cash = days * self.single_room_cost
                print(f"Вы прибывали в отеле дольше чем планировалось.\nВам нужно доплатить:{add_cash}")
                stat = False
                while stat == False:
                    if visitor.get_pay(add_cash) == True:
                        print("Спасибо. До свидания")
                        result = True
                        stat = True
                    else:
                        add_bal = int(input("На какую сумму вы хотите пополнить баланс?"))
                        visitor.balance += add_bal
        else:
            print("До свидания")
            result = True
        return result
    
    def register_time(self,order):
        if order.bed_num == 1:
            for room in self.single_room:
                if room[0] == order.room_id:
                    room[1] = order.date_from      
                    room[2] = order.date_to       
        elif order.bed_num == 2:
            for room in self.double_room:
                if room[0] == order.room_id:
                    room[1] = order.date_from  
                    room[2] = order.date_to  
        return True
                    
    def null_room_time(self,order):
        if order.bed_num == 1:
            for room in self.single_room:
                if room[0] == order.room_id:
                    room[1] = datetime.strptime("01-01-0001","%d-%m-%Y")    
                    room[2] = datetime.strptime("01-01-0001","%d-%m-%Y")     
                    return True
        elif order.bed_num == 2:
            for room in self.double_room:
                if room[0] == order.room_id:
                    room[1] = datetime.strptime("01-01-0001","%d-%m-%Y")  
                    room[2] = datetime.strptime("01-01-0001","%d-%m-%Y")  
                    return True




            


    





        




    


           







     

