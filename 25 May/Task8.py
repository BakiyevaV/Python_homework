user_input_num = input("Введите трехзначное число: ")
try:
    sym_num = len(user_input_num)
    user_input_num = int (user_input_num)
    
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
else:
    if sym_num > 3:
        message = "Введенное число не является трехзначным"
    elif sym_num < 3:
        message = "Введенное число не является трехзначным"
    else: 
        div1 = user_input_num % 100
        div2 = div1 // 10
        message = "Вторая цифра введенного Вами числа равна: %d" %div2
print(message)

