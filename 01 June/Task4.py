def get_square(x, y):
    if x != y:
        square = x * y
    if y == 0:
        square = x ** 2
    if x == 0:
        square = y ** 2
    if x == y:
        square = x ** 2
    return square

user_num1 = input("Введите длину прямоугольника/квадрата: ")
user_num2 = input("Введите ширину прямоугольника/квадрата: ")
if user_num1 and user_num2 != "":
    try:
        num1 = int(user_num1)
        num2 = int(user_num2)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Площадь прямоугольника/квадрата",get_square(num1, num2)  )

if user_num1 == "":
    try:
        num2 = int(user_num2)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Площадь прямоугольника/квадрата",get_square(0, num2))

if user_num2 == "":
    try:
        num1 = int(user_num1)
    except ValueError:
        print("Вы ввели не число!")
    else:
        print("Площадь прямоугольника/квадрата",get_square(num1, 0))



   
