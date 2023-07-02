num_list = [3, 9, 8, 4, 5, 1]
total_list = []
for i in range(len(num_list) - 1):
    if num_list[i+1] > num_list[i]:
        total_list.append(num_list[i+1])
print(total_list)
