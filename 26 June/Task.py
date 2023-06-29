# Программа осуществляет проверку устанавливаемого пользователем пароля на соответсвие условиям безопасности.
def is_correct(user_password):
    password = list(filter(str.isdigit, user_password))
    password2 = list(filter(str.isupper, user_password))
    password3 = list(filter(str.islower, user_password))
    if len(user_password)>=8 and len(password)>=1 and len(password2)>=1 and len(password3)>=1 and user_password[-1] in ["*","-","+","/","@","#"]:
        return True
    else:
        return False

user_password = input("Установите пароль с количеством символов не менее 8.\n Пароль должен содержать строчные и прописные буквы и символ из числа '*,-,+,/,@,#' в конце: ")
correct_password = list(filter(is_correct, [user_password]))
while correct_password == []:
    print("Введенный Вами пароль не соответствует условиям!")
    user_password = input("Установите пароль с количеством символов не менее 8.\n Пароль должен содержать строчные и прописные буквы и символ из числа '*,-,+,/,@,#' в конце: ")
    correct_password = list(filter(is_correct, [user_password]))
print("Пароль установлен")



