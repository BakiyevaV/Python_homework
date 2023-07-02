num_list = [3, 9, 8, 4, 5, 1, -5, 55]
min_num_index = num_list.index(min(num_list))
max_num_index = num_list.index(max(num_list))
if min_num_index > max_num_index:
    distance =  min_num_index - max_num_index
else: 
    distance =  max_num_index - min_num_index
print(distance)
