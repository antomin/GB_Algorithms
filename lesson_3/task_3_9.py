"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import sample

my_mtr = []
min_col_els = []

# matrix 5x5 random generation
for row in range(0, 5):
    my_mtr.append(sample([i for i in range(10, 100)], 5))

# print our matrix
for row in my_mtr:
    print(' '.join(map(str, row)))

# searching minimal elements in column
for idx in range(0, len(my_mtr)):
    column = []
    for row in my_mtr:
        column.append(row[idx])
    min_col_els.append(min(column))

print(f'\nMaximum of minimum is {max(min_col_els)}')
