from person import Person
from ticket import Ticket
from kassa import Kassa
from train import Train

if __name__ == "__main__":
    ilon = Person("Ilon", "Kask", "1994-06-25")
    ilon.earn(95000)

    alec = Person("Alec", "Boldwin", "1954-06-25")
    alec.earn(85000)

    kassa = Kassa()
    train1 = Train("0001   ",kassa, 'Алматы   ', "Сантьяго","24-05-2023","21:30")
    train2 = Train( "0002",kassa,'Алматы', "Монтевидео","24-05-2023","21:30")
    train3 = Train( "0003",kassa,'Алматы', "Москва","22-05-2023","21:30")
    place_from = "Алматы"
    place_to = "Москва"
    date = "22-05-2023"
    train_number, date_time, status = kassa.check_train(place_from, place_to,date)
    if status == True:
        print(f"Имеется поезд из {place_from} в {place_to} на {date_time}.")
        price = kassa.get_price(place_from, place_to)
        print(f"Стоимость билета составляет - {price} тг.")
        if kassa.buy_ticket(ilon, place_from, place_to, train3) == True:
            print(kassa.tickets)
            print(train3.go(ilon))
            print(kassa.tickets)
    else:
        if train_number == 0:
            print("Нет поездов с таким направлением!")
        else: 
            print(f"Есть поезд с таким направлением, но с другой датой - {date_time}.\nВы можете изменить параметры запроса")



