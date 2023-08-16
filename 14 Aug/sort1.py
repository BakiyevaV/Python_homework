# Сортировка "пузырьком"
def get_second_letter(word):
    sl = word[-1]
    return sl

def buble_sort(the_list, key= None):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        if key == None:
             for i in range(len(the_list) - 1):
                 if the_list[i] > the_list[i+1]:
                     the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
                     is_sorted = False
        elif key != None:
             for i in range(len(the_list) - 1):
                 if key(the_list[i]) > key(the_list[i + 1]):
                     the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]
                     is_sorted = False
    return the_list

user_in = input("Введите желаемые товары к покупке через запятую: ")
user_in = user_in.split(',')
the_list = list(map(lambda x: x.strip(), user_in))

print(buble_sort(the_list, get_second_letter))
print(buble_sort(the_list))
