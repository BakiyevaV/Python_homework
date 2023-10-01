import threading
def open_file(file_name,character):
    with open(file_name,"r", encoding = 'utf-8') as file:
        text = file.readlines()
        file.close()
    modify_text(text, character,file_name)

#VN: первое, что бросилось в глаза - это нарушение принципа единой ответственности: функция open_file() не только 
# занимается чтением файла, но и его модификацией. То же самое и с функцией modify_text() - она не только делает 
# замены, но и записывает изменённый текст в файл. Вызовы в конце функции - это тоже часть функции!


#VN: функция modify_text() - жуткий монстр, сложный для чтения и понимания. 
# Разбивайте такие алгоритмы на более маленькие шаги - функции!

def modify_text(text, character,file_name):
    signs = (",",".","!","?",":",'"',"»","«","'")
    #VN: если в этом цикле ind переименовать в row, а второй цикл сделать for sign in signs:, всё станет понятнее
    for ind in range(len(text)):
        for i in range(len(signs)):
            new_line = text[ind].replace(signs[i],f" {signs[i]} ")
            text[ind] = new_line
    # print(text)

    #VN: по сути происходит преобразование каждой строки в список слов. То же самое: станет сильно понятнее,
    # если l_ind переименовать в row, а new_l - в word_list
    for l_ind in range(len(text)):
        new_l = text[l_ind].split()
        text[l_ind] = new_l

    # print(text)
    new_text = []
    #VN: поскольку вы в результате этого блока формируете новый текст, можно обойтись без индексов.
    # Т.е. for line in text:, for word in line:, new_word in character: и тд. Ч - читаемость!)))
    for l_ind in range(len(text)):
        for k in range(len(text[l_ind])):
            for j in range(len(character)):
                if text[l_ind][k].lower() == character[j][0].lower():
                    if text[l_ind][k].istitle() == True:
                        text[l_ind][k] = character[j][1]
                    else: 
                        text[l_ind][k] = character[j][1].lower()
        new_line = " ".join(text[l_ind])
        #VN: этот кусок тоже можно в отдельную функцию - по смыслу: "поправить знаки"
        for i in range(len(signs)):
            if signs[i] == "'":
                new_line = new_line.replace(f"{signs[i]} ",f"{signs[i]}")
            new_line = new_line.replace(f" {signs[i]} ",f"{signs[i]} ")
            new_line = new_line.replace(f" {signs[i]}",f"{signs[i]}")
        write_text((f"{new_line}\n"),file_name)


#VN: возможно, алгоритмы были бы чуть проще, если в open_file() читать сразу весь текст через read(), а не по строкам.
                
def write_text(line,file_name):
    with open(f"modified_{file_name}","a", encoding = 'utf-8') as file2:
        file2.write(line)
        file2.close()

files = {"Winnie_the_Pooh.txt":[("Винни-Пух", "Обжора"),("Винни-Пухом", "Обжорой"),("Винни-Пуху", "Обжоре"),("Винни-Пухе", "Обжоре"),("Пух", "Обжора"),("Пуху", "Обжоре"),("Пухом", "Обжорой"),("Пухе", "Обжоре"),("Пуха", "Обжоры"),('Пу-ух','Обжо-ора'),("Винни", "Жора")],
         "Gold_fish.txt":[("Старик", "Бедняга"),("Старика", "Беднягу"),("Старику", "Бедняге"),("Стариком", "Беднягой"),("Старике", "Бедняге"),("Старичок","Бедняга")],
         "Kolobok.txt":[("Колобок","Булка с корицей"),("Колобка","Булку с корицей"),("Колобку","Булке с корицей"),("Колобком","Булкой с корицей"),("Колобке","Булке с корицей")],
         "Tri_mushketera.txt":[("Артаньян","Лимонохват"),("Артаньяна","Лимонохвата"),("Артаньяну","Лимонохвату"),("Артаньяном","Лимонохватом"),("Артаньяне","Лимонохвате")]}

#VN: этот цикл можно сделать ещё так: for file_name, replace_list in files.items():
for key in files.keys():
    n = 1
    thread = threading.Thread(target = open_file, args = (key, files[key]))
    thread.start()
    thread.join()