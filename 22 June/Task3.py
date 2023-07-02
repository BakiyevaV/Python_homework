num_list = [3, 9, 8, 4, 5, 1]
min_num = min(num_list)
max_num = max(num_list)
min_i = num_list.index(min_num)
max_i = num_list.index(max_num)
num_list[max_i] = min_num
num_list[min_i] = max_num
print(num_list)