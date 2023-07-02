numbers = input("Введите 10 чисел через запятую: ")
nums = numbers.split(',')
if len(nums)<10:
    col = 10 - len(nums)
    numbers2 = input(f"Вы ввели не достаточное кол-во цифр. Введите еще {col} чисел через запятую: ")
    nums2 = numbers2.split(',')
    total_list = nums + nums2 
elif len(nums) > 10:
    del nums[10:]
    total_list = nums
int_list = []
for i in total_list:
    i = int(i)
    int_list.append(i)

even_numbers = []
for i in int_list:
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)



