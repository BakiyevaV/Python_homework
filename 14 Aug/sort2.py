# Сортировка выборкой

def marks(student):
    return student[1]

def select_sort(the_list, key = None):
    n = len(the_list)
    if key == None:
        for i in range(n):
            min_item = min(the_list[i:n])
            min_index = the_list[i:n].index(min_item)+i
            the_list[i],the_list[min_index] = the_list[min_index],the_list[i]
    else:
        for i in range(n):
            min_item = min(the_list[i:n], key=key)
            min_index = the_list[i:n].index(min_item)+i
            the_list[i],the_list[min_index] = the_list[min_index],the_list[i]

    return the_list

students = [("Лиза", 99),("Кирилл", 65),("Марк", 86), ("Саша", 78)]

print(select_sort(students, marks))
print(select_sort(students))
