import re
import sys

console_args = sys.argv
print(console_args)

with open(console_args[1]) as file:
    data = file.read()
    file.close()
new_data = data.split(" ")


pattern = r'\w[\w\.-]*\w+@\w[\w\.]*\.[a-zA-Z]{2,3}'
matched = re.findall(pattern, data)

for w_email in new_data:
    if w_email not in matched:
        print(w_email)

print(matched)



