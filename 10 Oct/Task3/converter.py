import re
import sys

class Converter():
    def __init__(self,eur, usd, input, output):
        self.eur = eur
        self.usd = usd
        self.input = input
        self.output = output
        self.currency = "₸"
        self.read_file()


    def read_file(self):
        with open(self.input, encoding="UTF-8") as input_file:
            self.text = input_file.read()
            input_file.close()  
        self.get_match(self.text)

    def get_match(self, text):
        pattern_sum = r"\d+\.*\d*€|\d+\.*\d* EUR|\d+\.*\d*$|\d+\.*\d* USD"
        matched_sum = re.findall(pattern_sum,text)
        matched_list = []
        for s in  matched_sum:
            pattern_num = r"\d+\.*\d*"
            matched_num = re.search(pattern_num,s)
            pattern_val = r"€| EUR|$| USD"
            matched_val = re.search(pattern_val,s)
            matched_list.append((matched_num.group(), matched_val.group()))
        self.convert(matched_list)

    def convert(self, list):
        converted_list = []
        for num, cur in list:
            if cur == "€" or cur == "EUR":
                num = float(num)
                num *= self.eur
                converted_list.append((f"{round(num, 2)}",self.currency))
            elif cur == "$" or cur == "USD":
                num = float(num)
                num *= self.usd
                converted_list.append((f"{round(num, 2)}",self.currency))
        self.change_currency(converted_list, list)

    def change_currency (self,converted_list, list):
        for index in range(len(converted_list)):
            converted_list[index] = "".join(converted_list[index])
            list[index] = "".join(list[index])
        text_list = re.split(r"\. ", self.text)
        for s in range(len(text_list)):
            for i, k  in zip(converted_list, list):
                if k in text_list[s]:
                    new_sentense = re.sub(k, i, text_list[s])
                    text_list[s] = new_sentense

        new_text = ". ".join(text_list)
        self.write_new_text(new_text)

    def write_new_text(self, new_text):
        with open (self.output, "w", encoding="UTF-8") as output_file:
            output_file.write(new_text)
            output_file.close()
        print(new_text)

console_args = sys.argv
if len(console_args) == 3:
    converter = Converter(496.78, 470.3, console_args[1], console_args[2])
else:
    print("Отсутсвуют необходимые аргументы")





        



        