n = input("Введите длину строки: ")
n = int(n)
c1 = input("Введите первый символ: ")
c2 = input("Введите второй символ: ")
s = c1 + c2
pair_sum = s * (n // 2)
odd_num = c1 * (n % 2)
result = pair_sum + odd_num
print(result)