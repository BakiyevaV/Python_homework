def get_time (seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = ((seconds % 3600) % 60) 
    return f"{hours:02}:{minutes:02}:{seconds:02}"
user_time = input ("Введите количество секунд: ")
try:
    seconds = int(user_time)
except ValueError:
    print("Вы ввели не число!")
else:
    print("Время составляет", get_time (seconds))