# Список фруктов, который ,будет проверяться на дубликаты
fruits = ['apple', 'banana', 'cherry', 'apple', 'orange', 'banana'] 
# Словарь, в котором будут храниться фрукты, которые уже была проверен циклом
passed = {} 
#Cписок, в котором будут собираться дубликаты
duplicates = [] 
#  Цикл, который проходит по каждому фрукту в списке
for item in fruits: 
    # Это условие, которое проверяет, есть ли фрукт в словаре passed.
    if item in passed: 
        # Если есть, то это дубликат, и он добавляется в список duplicates
        duplicates.append(item)
        """Если нет, то это новый фрукт, и он добавляется в словарь passed
            ключом является элемент списка, который не является элементом списка. 
            а значением - True"""
    else: 
        passed[item] = True 
"""В результате получилось два списка. В первом списке passed - уникальные значения фруктов. 
Во втором их двойники"""
print(f'Найденные дубликаты: {duplicates}') # Выводим на экран список дубликатов
