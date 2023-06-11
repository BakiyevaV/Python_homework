def get_time(hours, minutes=0, seconds=0):
    return f"{hours:02}:{minutes:02}:{seconds:02}"

user_hour = input("Введите часы в числовом формате: ")
user_minutes = input("Введите минуты в числовом формате: ")
user_seconds = input("Введите секунды в числовом формате: ")
if user_seconds== "":
    try:
        hours = int(user_hour)
        minutes = int(user_minutes)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Время: ", get_time(hours, minutes, 0))

elif user_minutes == "":
    try:
        hours = int(user_hour)
        seconds = int(user_seconds)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Время: ",get_time(hours, 0 , seconds))

elif user_hour != "" and user_minutes != "" and user_seconds != "":
    try:
        hours = int(user_hour)
        minutes = int(user_minutes)
        seconds = int(user_seconds)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Время: ", get_time(hours, minutes, seconds) )


    


    
