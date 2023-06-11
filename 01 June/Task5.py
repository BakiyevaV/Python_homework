def get_capacity(diameter, height):
    return (3.141592 * ((diameter/2)**2)*height)*1000
user_diameter = input("Введите диаметр резервуара в метрах: ")
user_height = input ("Введите высоту резервуара в метрах: ")
try:
    diameter = float(user_diameter)
    height = float(user_height)
except ValueError:
    print("Вы ввели не число!")
else:
    result = get_capacity(diameter, height)
    print("Объем резервуара составляет", result, "литров")