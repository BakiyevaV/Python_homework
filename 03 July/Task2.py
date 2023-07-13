def is_word(word):
    return True if len(word)>0 else False

def text_wrap(paragraph, max_len):
    lines = []
    current_line = ''
    for word in paragraph:
        if word == paragraph[0]:
            current_line = '####'
            if len(current_line) + len(word) <= max_len:
                current_line += f"{word} "
            else:
                lines.append(current_line.strip())
                current_line = f'{word} '
        else:
            if len(current_line) + len(word) <= max_len:
                current_line += f"{word} "
            else:
                lines.append(current_line.strip())
                current_line = f'{word} '
    lines.append(current_line.strip())
    return lines

def add_space(line, max_len):
    words = line.split()
    num_words = len(words)
    if num_words == 1:
        line = line.ljust(max_len)
    else:
        while len(line) < max_len:
            for i in range(num_words - 1):
                words[i] += " "
                line = " ".join(words)
                if len(line) == max_len:
                    break
    return line

str_max_len = int(input("Введите максимальную длину строк в символах: "))
with open('Task_2.txt','r', encoding = 'utf-8') as file1:
    text = file1.read()
    text2 = text.split("\n")
    text2 = list(filter(lambda x: len(x) >= 1, text2))
    new_text = []
    new__text = []
    
for paragraph in text2:
    words = paragraph.split()
    new_text.append(words)

    """считаю, что удаление лишних символов здесь не нужно, 
    так как изначально формируется список через разделение, 
    где разделителем является пробел.И объединение элементов прошедших проверку 
    ни на каком этапе не нужно. Но на всякий случай
    предусмотрена часть кода с такой функцией, 
    которая возвращает слова, прошедшие проверку, объединенные в предложение. """
    for i in range(len(new_text)):
            result = list(filter(is_word, new_text[i]))
            new__line = " ".join(result)
            new__text.append(new__line)

n_text = []
    #функция, которая делит на строки не превышающие порог. 
for i in range(len(new_text)):
    lines = text_wrap(new_text[i],str_max_len)
    n_text.append(lines)
    

#функция добавляющая пробелы между слов.
n__text = []
for i in range(0,len(n_text)):
    for line in n_text[i]:
        n_line=add_space(line, str_max_len)
        n__text.append(n_line) 

#удаление пробелов между слов в последней строке
n__text[-1] = n__text[-1].split()
n__text[-1] = " ".join(n__text[-1]) 

new_text.clear()
for line in n__text:
    x = line.replace("####","    ")
    new_text.append(x)
   
#Перевод первой буквы строки в верхний регистр
new___t = []
for line in new_text:
    if line.startswith(" "):
        line = line
    else:
        line = line.capitalize()
    new___t.append(line)

final_text = "\n".join(new___t)

#создание файла и запись результата/ закрытие файла
with open('Task_2_out.txt','w', encoding = 'utf-8') as file2:
    file2.write(final_text)
    file1.close()
    file2.close()






        

