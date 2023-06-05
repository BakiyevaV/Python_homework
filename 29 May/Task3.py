user_year = input ("Введите год в числовом виде:")
sign_num = len(user_year)
try:
    user_year = int(user_year)
except ValueError:
    message = "Вы ввели не число!"
else:
    if sign_num > 4:
        message = "Введенное число вне допустимого диапазона - 4 цифры!"
    elif sign_num < 4:
        message = "Введенное число вне допустимого диапазона - 4 цифры!"
    else:
        div1 = user_year % 400
        div2 = user_year % 4
        div3 = user_year % 100
        if div1 == 0 and div3 > 0:
            message = "Введенный Вами %d год- високосный" %user_year
        elif div2 == 0 and div3 > 0:
            message = "Введенный Вами %d год- високосный" %user_year
        else: 
            message = "Введенный Вами %d год- невисокосный" %user_year
print(message)
