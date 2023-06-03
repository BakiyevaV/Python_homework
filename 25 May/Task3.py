
user_input_num = input("Введите длину стороны квадрата: ")
try:
    user_num = float(user_input_num)
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
else:
    square_s = user_num  * user_num
    message = "Квадрат введенного Вами числа равен: %f" %square_s
print(message)