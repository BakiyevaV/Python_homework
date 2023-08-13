from random import randint
n = 4
m = 5
matrix = [[randint(-10, 10) for col in range(1,m + 1)] for string in range(1,n+1)]
max_row_val = []
min_row_val = []
max_col_val = []
min_col_val = []
new_matrix = [[row[i] for row in matrix]for i in range(len(matrix[0]))]


for row in matrix:
    max_row_num = max(row)
    max_row_val.append(max_row_num)
    min_row_num = min(row)
    min_row_val.append(min_row_num)

for row in new_matrix:
    max_col_num = max(row)
    max_col_val.append(max_col_num)
    min_col_num = min(row)
    min_col_val.append(min_col_num)

print(matrix)
print("Максимальные числа в строках матрицы:",max_row_val)
print("Минимальные числа в строках матрицы:",min_row_val)
print("Максимальные числа в столбцах матрицы:",max_col_val)
print("Минимальные числа в строках матрицы:",min_col_val)








