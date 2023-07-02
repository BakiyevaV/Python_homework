list1 = ["BMW","Mazda","Nissan","Toyota","Mercedes","Volkswagen"]
list2 = ["Zeekr","Mazda","Cadillac","Geely","Mercedes","Volkswagen","Toyota"]
for i in list2:
    if i in list1:
        list1.remove(i)
print(list1)