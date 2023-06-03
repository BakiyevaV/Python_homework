
hour_input = input("Введите Ваше текущее время в часах: ")
minutes_input = input("Введите Ваше текущее время в минутах: ")
try:
    hour_input = int (hour_input)
    minutes_input = int (minutes_input)
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
else: 
    if hour_input >= 24:
        message = "Введенное вами число относится к недопустимому диапазону"
    elif minutes_input > 60:
        message = "Введенное вами число относится к недопустимому диапазону"
    else:
        hour = 24 - 1 - hour_input 
        minutes = 60 - minutes_input
        message = "До начала следующего дня осталось:%d Часов %d минут" %(hour,minutes)

print(message)
