 
days = ["Понедельник","Вторник", "Среда", "Черверг", "Пятница", "Суббота", "Воскресенье"]
def get_days(i):
    print("Ваш день недели! - ", days[i])
    answer = input("Вам подсказать следующий день?")
    if answer == "Да":
        return get_days(i+1)
    else:
        return print("Конец.")

get_days(0)

''' VN: Всё прекрасно, с одним нюансом:
Ваш день недели! -  Воскресенье
Вам подсказать следующий день?Да
Traceback (most recent call last):
  ...
    print("Ваш день недели! - ", days[i])
                                 ~~~~^^^
IndexError: list index out of range
'''