user_number_input = input ("Введите трехзначное число:")
sign_num = len(user_number_input)
try:
    user_number= int(user_number_input)
except ValueError:
    message = "Вы ввели не число!"
else:
    # VN: тоже можно одним условием:  if sign_num != 3:
    if sign_num > 3:
        message = "Введенное число вне допустимого диапазона!"
    elif sign_num < 3:   
        message = "Введенное число вне допустимого диапазона!"
    else:
        var1 = user_number // 100
        var2 = (user_number % 100) // 10
        var3 = user_number % 10
        if var1 == var2 or var2 == var3 or var1 == var3:
            message = "Имеются повторяющиеся цифры!"
        else:
            message = "Повторяющиеся цифры отсутствуют!"
print(message)

# В такой проверке ввода есть нюанс. Если пользователь введёт "123 ", то число будет трёхзачное,
# и преобразование пройдет без проблем, но длина строки будет 4. Поэтому лучше не использовать len(),
# а условие корректности будет:  100 <= user_number <= 999
