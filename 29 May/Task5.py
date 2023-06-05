user_money_sum = input ("Введите денежную сумму в долларах США: ")
user_val = input ("Введите желаемую валюту: ")
try:
    user_money_sum = float(user_money_sum)
except ValueError:
    message ="Вы ввели не число"
else:
    eur_in_stock = 100000 #указывается сумма в соответствующей валюте в наличии в обменном пункте. 
    uah_in_stock = 55000
    azn_in_stock = 100000
    aed_in_stock = 1000
    inr_in_stock = 0
    if user_val in "eur":
        eur = user_money_sum * 0.93
        if eur_in_stock == 0:
            message = "Данная валюта сейчас не доступна. Вы можете выбрать другую!"
        elif eur > eur_in_stock:
            message = "В наличии нет желаемого Вам количества денежных средств!\n Вы можете уменьшить сумму или выбрать другую валюту!"
        else:
            message = "Вам доступна следующая сумма в EUR: %.3f" %eur
    
    elif user_val in "azn":
        azn = user_money_sum * 1.70
        if azn_in_stock == 0:
            message = "Данная валюта сейчас не доступна. Вы можете выбрать другую!"
        elif azn > azn_in_stock:
            message = "В наличии нет желаемого Вам количества денежных средств!\n Вы можете уменьшить сумму или выбрать другую валюту!"
        else:
            message = "Вам доступна следующая сумма в AZN: %.3f" %azn

    elif user_val in "uah":
        uah = user_money_sum * 37.07
        if uah_in_stock == 0:
            message = "Данная валюта сейчас не доступна. Вы можете выбрать другую!"
        elif uah > uah_in_stock:
            message = "В наличии нет желаемого Вам количества денежных средств!\n Вы можете уменьшить сумму или выбрать другую валюту!"
        else:
            message = "Вам доступна следующая сумма в UAH: %.3f" %uah   

    elif user_val in "aed":
        aed = user_money_sum * 3.67
        if aed_in_stock == 0:
            message = "Данная валюта сейчас не доступна. Вы можете выбрать другую!"
        elif aed > aed_in_stock:
            message = "В наличии нет желаемого Вам количества денежных средств!\n Вы можете уменьшить сумму или выбрать другую валюту!"
        else:
            message = "Вам доступна следующая сумма в AED: %.3f" %aed 

    elif user_val in "inr":
        inr = user_money_sum * 82.40
        if inr_in_stock == 0:
            message = "Данная валюта сейчас не доступна. Вы можете выбрать другую!"
        elif inr > inr_in_stock:
            message = "В наличии нет желаемого Вам количества денежных средств!\n Вы можете уменьшить сумму или выбрать другую валюту!"
        else:
            message = "Вам доступна следующая сумма в INR: %.3f" %inr 
print (message)
