user_word_input = input("Введите слово из 5 букв: " )
if type(user_word_input) != str:
    message = "Вы ввели не слово"
else:
    sign_num = len(user_word_input)
    if sign_num > 5:
        message = "Ваше слово состоит из более чем 5 букв!"
    elif sign_num < 5:
        message = "Ваше слово состоит из менее чем 5 букв!"
    else:
        if user_word_input[0] == user_word_input[4] and user_word_input[1] == user_word_input[3]:
            message = "Ваше слово является полиндромом"
        else:
            message = "Ваше слово не является полиндромом"
print(message)

