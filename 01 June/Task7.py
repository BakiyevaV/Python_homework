def get_time(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds

user_hours = input("Введите часы в числовом формате: ")
user_minutes = input("Введите минуты в числовом формате: ")
user_seconds = input("Введите секунды в числовом формате: ")

if user_hours != "" and user_minutes != "" and user_seconds != "":
    try:
        hours = int(user_hours)
        minutes = int(user_minutes)
        seconds = int(user_seconds)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Время: ", get_time(hours, minutes, seconds))

elif user_seconds == "":
    try:
        hours = int(user_hours)
        minutes = int(user_minutes)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Время: ", get_time(hours, minutes, 0))

elif user_minutes == "":
    try:
        hours = int(user_hours)
        seconds = int(user_seconds)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Время: ",get_time(hours, 0 , seconds))







