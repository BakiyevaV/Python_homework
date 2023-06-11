def is_perfect(num, i=1, sum =0):
    if i >= num:
        return sum == num
    elif num % i == 0:
        sum += i
    return is_perfect(num, i + 1, sum)
     
user_num = input("Введите число: ")
try:
    num = int(user_num)
except ValueError:
    print("Вы ввели не число!")
else:
    if num <= 0:
        print("Необходимо ввести положительное число больше нуля!")
    else:
        if is_perfect(num):
            print("Ваше число является совершенным")
        else:
            print("Ваше число НЕ является совершенным")