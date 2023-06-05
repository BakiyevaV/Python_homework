price = input("Введите сумму покупки: ")
try:
   price = float(price)
except ValueError:
   print("Вы ввели не число!")
else:
    if price < 200:
        print("Скидка отсутствует. Сумма к оплате:",price)
    elif price >= 200 and price < 300:
        price *= 0.97
        print("Скидка - 3%. Сумма к оплате:",price)
    elif price >= 300 and price < 500:
        price *= 0.95
        print("Скидка - 5%. Сумма к оплате:",price)
    elif price >= 500:
        price *= 0.93
        print("Скидка - 7%. Сумма к оплате:",price)
