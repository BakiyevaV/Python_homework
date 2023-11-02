import sys
import json

class JsonConverter():
    def __init__(self, name,age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def user_to_json(self):
        str = "{'name': %s, 'age': %s, 'position': %s,'salary': %s}" % (self.name, self.age, self.position, self.salary)
        return json.dumps(str, ensure_ascii=False)
    
args = sys.argv
if len(args) == 5:
    emploee = JsonConverter(args[1], args[2], args[3], args[4])
    json_string = emploee.user_to_json()
    try:
        print("Это Json формат ",json.loads(json_string))
    except ValueError:
        print("Недопустимый формат")

else:
    print("Недопустимое количество аргументов")





