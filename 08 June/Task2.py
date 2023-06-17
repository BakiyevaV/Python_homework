num1 = input ("Введите первое число: ")
num2 = input ("Введите второе число: ")  
try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Вы ввели не число!")
else:
    divisors = []
    if num1 > num2:
        for i in range (1,num2 + 1):
            if num1 % i == 0 and num2 % i == 0:
                divisors.append(i)
                i += 1

    elif num1 < num2:
        for i in range (1,num1 + 1):
            if num1 % i == 0 and num2 % i == 0:
                divisors.append(i)
                i += 1
    print(max(divisors))
