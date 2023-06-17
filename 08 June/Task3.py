num = input ("Введите число больше 50: ")
try:
    num = float(num)
except ValueError:
    print("Вы ввели не число!")
else:
   count = 0
   while num > 50:
    num /= 2
    count += 1

print("Полученное число:", num)
print("Количество делений:", count)
            