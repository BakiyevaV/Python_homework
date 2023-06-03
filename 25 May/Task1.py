user_input_num = input("Введите число: ")
try:
    user_num = float(user_input_num)
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
else:
    num_square = user_num  ** 2
    message = "Квадрат введенного Вами числа равен: %f" %num_square
print(message)

