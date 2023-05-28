user_price = input("Введите стоимость товара в $: ")
user_discount = input("Введите размер скидки в %: ")
price = float(user_price)
discount = float(user_discount)
discount_sum = price/100 * discount
final_price = price - discount_sum
message = "Итоговая сумма к оплате: %.2f $" %final_price
print(message)