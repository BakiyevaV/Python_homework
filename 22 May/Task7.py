year_input = input("Введите ваш год рождения: ")
month_input = input("Введите ваш месяц рождения: ")
day_input = input("Введите ваш месяц рождения: ")
message = "Ваш день рождения: %s.%s.%s" %(day_input, month_input, year_input)
print(message)

# VN: Формат "дд.мм.гггг" предполагает, что если пользователь введёт 2010, 3, 3, то вывести надо "03.03.2010"
# Ваша программа выводит не так. Это можно поправить, используя в шаблоне спецификаторы длины и заполнения