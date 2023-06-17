num1 = input ("Введите первое число: ")
num2 = input ("Введите второе число: ")
try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print ("Вы  ввели не число!")
else:
    if num1 < num2:
        sum = 0
        for i in range(num1,num2+1):
            sum += i
        print (sum)
    elif num1 > num2:
        sum = 0
        for i in range(num2,num1+1):
            sum += i
        print (sum)



