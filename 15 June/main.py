from hotel import Hotel
from person import Person
from room import Room
from order import Order
from datetime import datetime


if __name__ == "__main__":
    hotel = Hotel("Hilton", 10000, 20, 200, 500)
    single_room, double_room = hotel.gen_rooms()
    room = Room()
    request = input(f"Добрый день. Вы хотели бы забронировать номер? " )
    if request.lower() in ["да","д","Y","y"]:
        request_parameters = input("Прошу указать через запятую ваше имя, фамилию, ИИН,\nжелаемую дату(через дефис в формате день-месяц-год),\nжелаемый срок бронирования,кол-во спальных мест(1 или 2): ")
        visitor_f_name, visitor_l_name, visitor_iin, date_from, days_quantity, bed_num = [x.strip() for x in request_parameters.split(",")]
        if date_from == "":
            current_date = datetime.now().date()
            date_from = current_date.strftime("%d-%m-%Y")
        else:
            d,m,y = date_from.split("-")
            new_date = []
            a = int(d)
            b = int(m)
            c = int(y)
            if a < 10 and len(d) == 2:
                d = d[1]
            if b < 10 and len(m) == 2:
                m = m[1]
            new_date.append(d)
            new_date.append(m)
            new_date.append(y)
            date_from = "-".join(new_date)
            date_from = datetime.strptime(date_from,"%d-%m-%Y")   
        visitor1 = Person(visitor_f_name,visitor_l_name, visitor_iin,10000)
        price = hotel.get_price(days_quantity, bed_num)
        say_price = input(f"Стоимость номера на указанный срок составит {price} $. Хотите забронировать? ")
        if say_price.lower() in ["да","д","Y","y"]:
            date_to,free_rooms = room.is_empty(bed_num, date_from, days_quantity,single_room,double_room)
            visitor_room = None
            if len(free_rooms) >=1:
                while visitor_room == None:
                    room_num = int(input(f"На данный момент свободные комнаты: {free_rooms}. Какую Вы хотите забронировать? "))
                    if room_num in free_rooms:
                        visitor_room = room_num
                    else:
                        print(f"Комнаты {room_num} нет среди свободных комнат. Попробуйте еще раз.")
                if visitor1.get_pay(price) is False:
                    add_balance_ask1 = (f"Вам нужно пополнить баланс на {price - visitor1.balance} $.\nВы хотите пополнить баланс? ")
                    if add_balance_ask1 in ["да","д","Y","y"]:
                        while visitor1.balance < price:
                            add_balance_ask2 = int(input("На какую сумму Вы хотите пополнить? "))
                            visitor1.balance += add_balance_ask2
                        visitor1.get_pay(price)
                        hotel.buy_order(room_num, bed_num, date_from, date_to)
                    else: 
                        print ("Просим прощения! Мы не можем забронировать Вам номер")
                else: 
                    order = Order(hotel.name, visitor_room,date_from,date_to,visitor_f_name, visitor_l_name,visitor_iin,bed_num)
                    visitor1.order = True
                    print(order.get_info())
                    hotel.register_time(order)
                    if hotel.check_in(order) == True:
                        if hotel.check_out(order,visitor1) == True:
                            hotel.null_room_time(order)
            else:
                print("Просим прощения! на указанную дату свободных комнат нет.")     
        else:
            print("Будем Вас ждать в следующий раз.")
    else:
        print("Будем Вас ждать в следующий раз.")