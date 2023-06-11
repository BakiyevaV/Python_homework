def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

def get_perfect_numbers(min, max):
    perfect_numbers = []
    for num in range(min, max + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers

user_min_num = input("Введите минимальное число: ")
user_max_num = input("Введите максимальное число: ")
try:
    min = int(user_min_num)
    max = int(user_max_num)
except ValueError:
    print("Вы ввели не число!")
else:
    if min <= 0:
        print("Необходимо ввести положительное число больше нуля!")
    else:
        print("Совершенные числа в указанном Вами диапазоне", get_perfect_numbers(min, max))
