import threading
def open_file(file_name,character):
    with open(file_name,"r", encoding = 'utf-8') as file:
        text = file.readlines()
        file.close()
    modify_text(text, character,file_name)


def modify_text(text, character,file_name):
    signs = (",",".","!","?",":",'"',"»","«","'")
    for ind in range(len(text)):
        for i in range(len(signs)):
            new_line = text[ind].replace(signs[i],f" {signs[i]} ")
            text[ind] = new_line
    # print(text)

    for l_ind in range(len(text)):
        new_l = text[l_ind].split()
        text[l_ind] = new_l

    # print(text)
    new_text = []
    for l_ind in range(len(text)):
        for k in range(len(text[l_ind])):
            for j in range(len(character)):
                if text[l_ind][k].lower() == character[j][0].lower():
                    if text[l_ind][k].istitle() == True:
                        text[l_ind][k] = character[j][1]
                    else: 
                        text[l_ind][k] = character[j][1].lower()
        new_line = " ".join(text[l_ind])
        for i in range(len(signs)):
            if signs[i] == "'":
                new_line = new_line.replace(f"{signs[i]} ",f"{signs[i]}")
            new_line = new_line.replace(f" {signs[i]} ",f"{signs[i]} ")
            new_line = new_line.replace(f" {signs[i]}",f"{signs[i]}")
        write_text((f"{new_line}\n"),file_name)
                
def write_text(line,file_name):
    with open(f"modified_{file_name}","a", encoding = 'utf-8') as file2:
        file2.write(line)
        file2.close()

files = {"Winnie_the_Pooh.txt":[("Винни-Пух", "Обжора"),("Винни-Пухом", "Обжорой"),("Винни-Пуху", "Обжоре"),("Винни-Пухе", "Обжоре"),("Пух", "Обжора"),("Пуху", "Обжоре"),("Пухом", "Обжорой"),("Пухе", "Обжоре"),("Пуха", "Обжоры"),('Пу-ух','Обжо-ора'),("Винни", "Жора")],
         "Gold_fish.txt":[("Старик", "Бедняга"),("Старика", "Беднягу"),("Старику", "Бедняге"),("Стариком", "Беднягой"),("Старике", "Бедняге"),("Старичок","Бедняга")],
         "Kolobok.txt":[("Колобок","Булка с корицей"),("Колобка","Булку с корицей"),("Колобку","Булке с корицей"),("Колобком","Булкой с корицей"),("Колобке","Булке с корицей")],
         "Tri_mushketera.txt":[("Артаньян","Лимонохват"),("Артаньяна","Лимонохвата"),("Артаньяну","Лимонохвату"),("Артаньяном","Лимонохватом"),("Артаньяне","Лимонохвате")]}
for key in files.keys():
    n = 1
    thread = threading.Thread(target = open_file, args = (key, files[key]))
    thread.start()
    thread.join()