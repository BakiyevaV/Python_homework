user_number_input = input("Введите число от 0 до 9: ")
try:
    user_number= int(user_number_input)
except ValueError:
    message = "Вы ввели не число!"
else:
    if user_number>9:
        message = "Введенное число вне допустимого диапазона!"
    elif user_number<0:
        message = "Введенное число вне допустимого диапазона!"
    elif user_number == 1:
        message = "Введенному Вами числу  - 1 соответстует спецсимвол: !" 
    elif user_number == 2:
        message = "Введенному Вами числу  - 2 соответстует спецсимвол: @" 
    elif user_number == 3:
        message = "Введенному Вами числу  - 3 соответстует спецсимвол: #" 
    elif user_number == 4:
        message = "Введенному Вами числу  - 4 соответстует спецсимвол: $" 
    elif user_number == 5:
        message = "Введенному Вами числу  - 5 соответстует спецсимвол: %" 
    elif user_number == 6:
        message = "Введенному Вами числу  - 6 соответстует спецсимвол: ^" 
    elif user_number == 7:
        message = "Введенному Вами числу  - 7 соответстует спецсимвол: &" 
    elif user_number == 8:
        message = "Введенному Вами числу  - 8 соответстует спецсимвол: *" 
    elif user_number == 9:
        message = "Введенному Вами числу  - 9 соответстует спецсимвол: ()" 
    
print(message)


