
user_km_num = input("Введите количество километров для последующей конвертации в мили:")
try:
    km_num = float(user_km_num)
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"

else:
    miles = km_num * 0.621371
    message = "%f км. равно %f миль" %(km_num, miles)
print(message)