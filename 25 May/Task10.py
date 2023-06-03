sales_amount_input = input("Введите общую сумму продаж за месяц в $: ")
try:
    sales_amount = float(sales_amount_input)
except ValueError:
    message = "Ошибка! Введенное вами значение не является числовым!"
else:
    sales_percent = sales_amount / 100 * 10
    sum = 250 + sales_percent
    message = "Общая сумма к получению: %f" %sum
print(message)
