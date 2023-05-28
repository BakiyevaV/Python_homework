# user_word_input = input("Введите слово: ")
# central_part = user_word_input[1:-1]
# sym_count = len(central_part)
# substitution = "*" * sym_count
# print(user_word_input[0],substitution,user_word_input[-1])

user_word_input = input("Введите слово: ")
central_part = user_word_input[1:-1]
sym_count = len(central_part)
substitution = "*" * sym_count
message = "%s%s%s" %(user_word_input[0],substitution,user_word_input[-1])
print(message)