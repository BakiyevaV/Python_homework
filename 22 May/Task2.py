user_word_input = input("Введите слово: ")
sym_amount = len(user_word_input)
half_division = sym_amount//2
first_half = user_word_input[:half_division]
second_half = user_word_input[half_division:]
print(first_half, " ", second_half)