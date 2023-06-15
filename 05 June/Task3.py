def get_mult_table ( n, i=1):
   if i > 10:
       return
   else:
       print(f'{n} * {i} = {n*i}')
       get_mult_table (n, i + 1)

for n in range(2, 10): 
    print(f"Таблица умножения для {n}")
    get_mult_table(n)


      