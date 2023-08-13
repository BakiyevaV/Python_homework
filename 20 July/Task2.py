from random import randint
n = 4
m = 5
matrix = [[randint(-10, 10) for col in range(1,m + 1)] for string in range(1,n+1)]
odd_row_sum = 0
odd_row_sums = []
odd_col_sum = 0
odd_col_sums = []

for i in range(len(matrix)):
    for num in matrix[i]:
        if num % 2 != 0:
            odd_row_sum += num    
    odd_row_sums.append (odd_row_sum)
    odd_row_sum = 0

new_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
for i in range(len(new_matrix )):
    for num in new_matrix [i]:
        if num % 2 != 0:
            odd_col_sum += num    
    odd_col_sums.append (odd_col_sum)
    odd_col_sum = 0

print(matrix)
print("Суммы нечетных чисел в строках матрицы:",odd_row_sums)
print("Суммы нечетных чисел в столбцах матрицы:",odd_col_sums)











