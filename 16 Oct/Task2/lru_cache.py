from tinydb import TinyDB, Query
from functools import lru_cache
import os

#Пример 1
# class StudentsDB():
#     def __init__(self, file):
#         self.file = file
#         self.db  = TinyDB(self.file)
#         self.table = self.db.table('students')

#     def write_data(self,name, age):
#         student = {'name': f"{name}-", 'age': age+1}
#         self.table.insert(student)
#         self.name = name
        
#     @lru_cache
#     def get_data(self):
#         result = self.table.search(Query().name == f"{self.name}-")
#         self.table.truncate()
#         return result[0]['name'], result[0]['age']
    

# first = StudentsDB("db.json")
# first.write_data("Alice", 25)
# print(first.table)
# print(first.get_data())
# print(first.table)

# name, age = first.get_data()
# print(name, age)

# second = StudentsDB('db2.json')
# second.write_data(name, age)

#Пример 2


class TinyDBWrapper:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.table = self.db.table("users")

    @lru_cache(maxsize=128)
    def save_data(self,number, ip):
        if number:
            number = int(number)
        ip_w = ip[0:10]
        ip_la_num = ip[10:]
        if ip_la_num:
            ip_la_num = int(ip_la_num)
        user = {'number': f"{number+1}", 'ip': f"{ip_w}{ip_la_num+1}"}
        self.table.insert(user)
        result = self.table.search(Query().number == f"{number+1}")
        result = self.table.search(Query().number == f"{number+1}")
        return result[0]['number'], result[0]['ip']

    @lru_cache(maxsize=128)
    def get_all_users(self):
        return self.table.all()
    

db = TinyDBWrapper("base.json")
number = 0
ip = "172.168.0.0"
for _ in range(10):
    number, ip = db.save_data(number, ip)

print(db.save_data.cache_info())
print(db.get_all_users())

db.table.truncate()

print(db.table.all()) 
print(db.get_all_users())

db.get_all_users.cache_clear()

print(db.get_all_users())














