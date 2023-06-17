num = input("Введите число:")
shift = input ("На сколько символов сдвинуть ваше число?: ")
try:
    number = int (num)
    shift = int (shift)
except:
    print("Вы ввели не число!")
else:
    if shift == len(num):
        print("Нельзя сдвигать на то же количество символов что и у вашего числа!")
    else:
        sym_num = len(num)
        new_num = ""
        for i in range(sym_num):
               new_num += num[(i + shift)%sym_num]
        print("Ваше новое число:",new_num)
     

