user_input_num1 = input("Введите первое число: ")
user_input_num2 = input("Введите второе число: ")
try:
    user_num1 = float(user_input_num1)
    user_num2 = float(user_input_num2)
    div = user_num1 / user_num2
    
except  ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"

except ZeroDivisionError:
    message = "Ошибка!На ноль делить нельзя!"
    
else:
    sum = user_num1 + user_num2
    sub = user_num1 - user_num2
    mult = user_num1 * user_num2
    div = user_num1 / user_num2
    message = "Сумма введенных вами чисел равна %f;\nРазница введенных вами чисел равна %f;\nУмножение введенных вами чисел равно %f;\nРeзультат деления введенных вами чисел равен %f" %(sum, sub, mult, div)

print(message)
