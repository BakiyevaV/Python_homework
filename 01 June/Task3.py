def get_new_number(num1, num2, num3):
    num1 = num1 * 100
    num2 = num2 * 10
    return num1 + num2 + num3

user_num1 = input("Введите первое число: ")
user_num2 = input("Введите второе число: ")
user_num3 = input("Введите третье число: ")
try:
   num1 = int(user_num1)
   num2 = int(user_num2)
   num3 = int(user_num3)
except ValueError:
     print("Вы ввели не число!")
else:
    result = get_new_number(num1, num2, num3)
print("Ваше составное число равно:", result)