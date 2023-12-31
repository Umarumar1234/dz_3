# 6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**

# 1 2  3  4  5  6
# 2 4  6  8  10 12
# 3 6  9  12 15 18
# 4 8  12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36'''

# def print_operation_table(operation, rows=6, cols=6):
#     matrix = [[0] * cols for _ in range(rows)]

#     for i in range(rows):
#         for j in range(cols):
#             matrix[i][j] = operation((i + 1), (j + 1))

#     for i in matrix:
#         print(*i)
#     return ''

# print(print_operation_table(lambda x, y: x * y))