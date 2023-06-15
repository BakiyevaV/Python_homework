def get_smile(num, i = 1):
    if i >= num:
        return ":)" * num
    else:
        return get_smile(num, i + 1)

user_num = input("Введите число: ")
try:
    num = int(user_num)
except ValueError:
    print("Вы ввели не число! ")
else:
    result = get_smile(num)
    print("Вот Ваши смайлики:", result)



    