user_input_num = input("Введите трехзначное число: ")
try:
    sym_num = len(user_input_num)
    user_input_num = int (user_input_num)
    
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
else:
    if sym_num > 5:
        message = "Введенное число не является пятизначным"
    elif sym_num < 5:
        message = "Введенное число не является пятизначным"
    else: 
        div1 = user_input_num // 10
        div2 = user_input_num % 10
        mult = div1 * 10000
        sum = mult + div2
        message = "Вторая цифра введенного Вами числа равна: %d" %sum
print(message)