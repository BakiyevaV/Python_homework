
def get_conpare(x,y):
    if x < y:
        return -1
    if x > y:
        return 1
    if x == y:
        return 0
    
user_num1 = input("Введите первое число: ")
user_num2 = input("Введите второе число: ")
try:
    num1 = float(user_num1)
    num2 = float(user_num2)
except ValueError:
    result = "Вы ввели не число!"
else:
    result = get_conpare(num1,num2)
print(result)