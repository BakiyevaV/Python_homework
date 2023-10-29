import time

def measuretime(func):
    def wrapper(text):
        start_time = time.time()
        text = func(text)
        end_time = time.time()
        res = end_time - start_time
        print(f"{func.__name__} - {res*1000} мс")
        return text
    return wrapper

@measuretime
def text_wrapper(text):
    new_text = text.split(" ")
    current_str = "Бугагашеньки-"
    for index in range(len(new_text)):
        current_str += new_text[index]
        new_text[index] = current_str
        current_str = "Бугагашеньки-"
    new_text = " ".join(new_text)
    return new_text

def open_file(file):
    with open(file, encoding="UTF-8") as file:
        text = file.read()
        file.close()
    return text

@measuretime
def write_file(text):
    with open("Task1\output.txt","w", encoding="UTF-8") as file:
        file.write(text)
        file.close()

text = open_file("Task1\input.txt")
new_text = text_wrapper(text)
if new_text:
    write_file(new_text)

    

    






