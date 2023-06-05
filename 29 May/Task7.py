circle_length = input("Введите длину окружности: ")
square_p = input("Введите значение периметра квадрата: ")
try:
    circle_length = float(circle_length)
    square_p = float(square_p)
except ValueError:
    message = "Введенное значение не числовое!"
else:
    circle_d = circle_length/3.14
    square_side = square_p/4
    if circle_d <= square_side:
        message = "Окружность с длиной %.2f поместится в квадрате с периметром %.2f." %(circle_length, square_p)
    else:
        message = "Окружность с длиной %.2f НЕ поместится в квадрате с периметром %.2f." %(circle_length, square_p)
print(message) 