 
days = ["Понедельник","Вторник", "Среда", "Черверг", "Пятница", "Суббота", "Воскресенье"]
def get_days(i):
    print("Ваш день недели! - ", days[i])
    answer = input("Вам подсказать следующий день?")
    if answer == "Да":
        return get_days(i+1)
    else:
        return print("Конец.")

get_days(0)