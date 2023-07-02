names = ["Аня","Саша","Петр","Илья","Клара","Петр","Валентин","Аня","Клара"]
double_names = []
for i in names:
   num = names.count(i)
   if num >1 and i not in double_names:
      double_names.append(i)
print(double_names)