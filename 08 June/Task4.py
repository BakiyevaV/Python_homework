count_num = 0
negative = 0
positive = 0
zero = 0
even = 0
odd = 0
while count_num < 10:
    num = input ("Введите число: ")
    try:
       num = float(num) 
    except ValueError:
        print ("Вы ввели не число!")
    else: 
        count_num += 1
        if num % 2 == 0:
            even += 1
        elif num % 2 != 0:
            odd += 1
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        elif num == 0:
            zero += 1 
        
        
else:
    print ("Количество положительных чисел: ",positive)
    print ("Количество отрицательных чисел: ",negative)
    print ("Количество нулей: ",zero)
    print ("Количество четных чисел: ",even)
    print ("Количество нечетных чисел: ",odd)
    

            

