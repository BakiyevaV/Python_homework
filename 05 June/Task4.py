import random

def get_random_int(min, max):
    number = random.random() * (max-min)
    number += min
    return int(number)


def game(my_random, min, max, amount = 7):
    user_num = input(f"Угадай число от {min} до {max}. Попыток осталось {amount} : " )
    try:
        user_num = int(user_num)
    except ValueError:
        print("Целое число надо вводить!")
        game(my_random, min, max, amount)
    else:
        if amount <= 1:
            return print(f"Попыток не осталось. Вы проиграли! Число было - {my_random}")
        elif my_random < user_num:
            print("Меньше ;)")
            game(my_random, min, max, amount-1)
        elif my_random > user_num:
            print("Больше ;)")
            game(my_random, min, max, amount-1)
        elif my_random == user_num:
            times = 7 - amount + 1
            print(f"Правильно! Моё число - {my_random}. Вы угадали за {times} раз" )
    
bottom = 0
top = 20
num = get_random_int(bottom, top)
game(num, bottom, top)

