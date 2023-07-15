from datetime import datetime, timedelta
class Room:   
    def __init__(self): 
        self.free_rooms = []


    def is_empty(self,bed_num, date_from, days, single_room,double_room):
        bed_num = int(bed_num)
        days = int(days)
        days_num = timedelta(days=days)
        date_to = date_from + days_num
        if bed_num == 2:
            for i in range(len(double_room)):
                if date_from  > double_room[i][1] and date_from <= double_room[i][2]:
                    continue
                else:
                    self.free_rooms.append(double_room[i][0])
        elif bed_num == 1:
            for i in range(len(single_room)):
                if date_from  > single_room[i][1] and date_from <= single_room[i][2]:
                    continue
                else:
                    self.free_rooms.append(single_room[i][0])
        
        return date_to, self.free_rooms





    




