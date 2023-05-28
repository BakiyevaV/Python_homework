user_word_input = input("Введите слово из трех букв: ")
first_sym = user_word_input[0]
second_sym = user_word_input[1]
third_sym = user_word_input[2]
first_sym = ord(first_sym)
second_sym = ord(second_sym)
third_sym = ord(third_sym)
sum_code = first_sym + second_sym + third_sym
print("Сумма кодов в введенном вами слове равно: ", sum_code)