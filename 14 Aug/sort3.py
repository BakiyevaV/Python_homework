# Быстрая сортировка

user_in = input("Введите список слов через запятую: ")
user_in = user_in.split(',')
the_list = list(map(lambda x: x.strip(), user_in))

def get_length(word= None):
    signs_count = 0
    for i in word:
        signs_count +=1
    return signs_count
def quicksort(array,key=None):
    if key == None:
        if len(array) <= 1:
            return array
        pivot = array[0]
        less = [x for x in array if x < pivot]
        equal = [x for x in array if x == pivot]
        more = [x for x in array if x > pivot]
        return quicksort(less) + equal + quicksort(more)
    else:
        if len(array) <= 1:
            return array
        pivot = key(array[0])
        less = [x for x in array if key(x) < pivot]
        equal = [x for x in array if key(x) == pivot]
        more = [x for x in array if key(x) > pivot]
        return quicksort(less,get_length) + equal + quicksort(more,get_length)
print(quicksort(the_list,get_length))
print(quicksort(the_list))


