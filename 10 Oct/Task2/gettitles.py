import re
import sys

def get_titles(input, output):
    with open(input,encoding="UTF-8") as file:
        document = file.read()
        file.close()

    pattern = r"<title>.*</title>|<h\d>.*</h\d>"

    matches = re.findall(pattern, document)
    new_str = " ".join(matches)
    pattern_title = r"<title>"
    text = re.sub(pattern_title,"",new_str )

    pattern_first_tag = r"<title>|<h[3-9]>"
    text = re.sub(pattern_first_tag,"\n",text)

    pattern_f_tag = r"<h[12]{1}>"
    new_text = re.sub(pattern_f_tag,"\n\n",text)

    pattern_last_tag = r"</title>|</h\d>"
    final_text = re.sub(pattern_last_tag,"",new_text)

    with open(output,"w",encoding="UTF-8") as out_file:
        out_file.write(final_text)
        out_file.close()

    return final_text

console_args = sys.argv

if len(console_args) == 3:
    print(get_titles(console_args[1],console_args[2]))
else:
    print("Отсутсвуют необходимые аргументы")


