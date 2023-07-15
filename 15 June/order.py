from random import randint
class Order:
    def __init__(self,name, room_id,date_from,date_to,visitor_name,visitor_last_name,visitor_iin, bed_num, order_id = 0):
        self.room_id = int(room_id)
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name 
        self.visitor_last_name = visitor_last_name
        self.visitor_iin = visitor_iin
        self.order_id = randint(00000, 99999)
        self.bed_num = int(bed_num)
        self.name=name
        
    def get_info(self):
        info = f"Забронирован номер в отеле {self.name}:\nна имя -{self.visitor_name} {self.visitor_last_name}.\nИИН Посетителя - {self.visitor_iin}.\nКол-во спальных мест - {self.bed_num}.\nНомер комнаты - {self.room_id}\nДата заселения - {self.date_from}.\nДата выезда -{self.date_to}.\nНомер брони - {self.order_id}"
        return info
    