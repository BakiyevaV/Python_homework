user_num_input = input("Введите шестизначное число: ")
first_half_sum = int(user_num_input[0:3])
second_half_sum = int(user_num_input[3:6])
both_half_sum = first_half_sum + second_half_sum
print("сумма цифр в составе введенного вами числа равна: ",both_half_sum)


