
user_input_num1 = input("Введите первое число: ")
user_input_num2 = input("Введите второе число: ")
try:
    user_num1 = float(user_input_num1)
    user_num2 = float(user_input_num2)
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
except TypeError:
    message = "Ошибка! Невозможно выполнить операцию с введенными значениями"
else: 
    result = (user_num1  + user_num2)/2
    message = "Среднее арифметическое введенных Вами чисел равно: %f" %result
print(message)


