# #capitalize, title
# word = "дезинформация - введение в заблуждение, путем предоставления ложной информации."
# cap = word.capitalize()# делает заглавной первую букву первого слова
# ttl = word.title()# делает заглавной каждую первую букву каждого слова
# print(cap)
# print(ttl)

# #count, find, rfind,index
# word = "дезинформация - введение в заблуждение, путем предоставления ложной информации."
# print(word.count("ци")) # сочетание "ци" встречается в строке 2 раза
# print(word.count("",0,13)) # при сокращении диапазона поиска, искомое сочетание встречается 1 раз.
# print(word.find("ци")) # возвращает первый индекс найденного сочетания. Проверка производится слева направо
# print(word.rfind("ци")) # возвращает первый индекс найденного сочетания. Проверка производится справа налево
# print(word.index("ци")) # возвращает первый индекс найденного сочетания. Отличия от fine и rfind в том, что в случае отсутствия искомого в строке, вернет value error.

# #upper,join,lower,swapcase
# word = "дезинформация - введение в заблуждение, путем предоставления ложной информации."
# word_list = list(word)
# for i in range(0, len(word),5):
#     word_list[i] = word_list[i].upper() #Делает заглавной каждый пятый элемент списка, который является строкой
# word1 = "".join(word_list)#Объединяем элементы списка в единую строку. 
# print(word1)
# print(word1.lower())#переводит все элементы строки в нижний регистр.
# print(word1.swapcase())#переводит все строчные элементы в прописные и наоборот. 


# #center,ljust,rjust,strip, rstrip, lstrip, zfill
# word = "дезинформация - введение в заблуждение, путем предоставления ложной информации."
# word1= word[0:13]
# word2 = word1.center(60,"$")
# print(word2)# отражает строчный элемент посередине. 60 - длина строки, "$" свободное место в строке справа и слева заполняется данным символом
# print(word1.ljust(60,"$"))# отражает строчный элемент слева. 60 - длина строки, "$" свободное место в строке справа заполняется данным символом
# print(word1.rjust(60,"$"))# отражает строчный элемент справа. 60 - длина строки, "$" свободное место в строке слева заполняется данным символом
# print(word2.strip("$"))# удаляет указанный символ справа и слева
# print(word2.rstrip("$"))# удаляет указанный символ справа
# print(word2.lstrip("$"))# удаляет указанный символ слева
# print(word1.zfill(25))# добавляет нули слева

# #startswith, endswith
# word = "дезинформация - введение в заблуждение, путем предоставления ложной информации."
# print(word.startswith("дезинформация"))# Предикативная функция, проверяющая начинается ли строка с заданного значения.
# print(word.endswith("путем"))# Предикативная функция, проверяющая заканчивается ли строка с заданного значения.

# #encode, decode
# word = "дезинформация - введение в заблуждение, путем предоставления ложной информации."
# encoded = word.encode() # возвращает объект байтов
# print(encoded)
# print(encoded.decode()) # преобразует байты в строки

# word = "дезинформация\t-\tвведение\tв\tзаблуждение,\tпутем\tпредоставления\tложной\tинформации."
# print(word.expandtabs())# Заменяет знак табуляции на пробел. Количество пробелов зависит от количества символов перед табуляцией.  
# print(word.expandtabs(tabsize=1)) # Указывается количество пробелов

# #format, 
# word = "дезинформация - введение в заблуждение, путем предоставления ложной информации."
# print("Слово: {}.".format(word[0:13]))# подставляет элемент

# #format_map
# words = {"x":'дезинформация',"y":'введение', "z":'заблуждение'}
# print("{x} - {y} в {z}".format_map(words))# подставляет значение соответствующее ключу в словаре. 

# #replace
# word = "Имя - Виктория, Фамилия - Бакиева"
# print(word.replace("Виктория", "Вика")) # З аменяет старое значение(первое) на новое (второе).

# #isalpha, isdigit, isupper, islower
# word = "Имя - Виктория, Фамилия - Бакиева"
# print(word[6:14].isalpha()) #Предикативная функция отвечающая все ли элементы строки являются буквами?
# print(word[6:14].isdigit()) #Предикативная функция отвечающая все ли элементы строки являются цифрами?
# print(word[6:14].isupper()) #Предикативная функция отвечающая все ли элементы строки являются прописными?
# print(word[6:14].islower()) #Предикативная функция отвечающая все ли элементы строки являются строчными?






