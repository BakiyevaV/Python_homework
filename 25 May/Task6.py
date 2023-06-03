user_input_num1 = input("Введите первое число: ")
user_input_num2 = input("Введите второе число: ")
try:
    user_num1 = float(user_input_num1)
    user_num2 = float(user_input_num2)
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
else:
    if user_num2 == 0:
        message = "На ноль делить нельзя!"
    else:
        x= -(user_num2/user_num1)
        message = " X равен %f" %x
     
print(message)