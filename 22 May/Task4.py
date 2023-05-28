user_word_input = input("Введите слово: ")
first_part = user_word_input[0:2]
second_part = user_word_input[-2:]
message = "Введенное вами слово сокращено до: %s-%s" % (first_part, second_part)
print(message)