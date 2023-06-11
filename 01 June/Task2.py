def get_sum(num):
    if num == 0:
       return 0
    else:
       return num + get_sum(num - 1)

user_num = input("Введите число: ")
try:
   num = int(user_num)
except ValueError:
     print("Вы ввели не число!")
else:
    result = get_sum(num)
print("Сумма чисел равна:", result)