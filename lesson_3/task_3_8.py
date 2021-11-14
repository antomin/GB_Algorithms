"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных
элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

my_mtr = []
cnt = 1
for i in range(1, 6):
    new_row = input(f'Enter 4 numbers to row {i}: ').split()
    if len(new_row) != 4:
        print('Input data error!')
        i -= 1
        continue
    my_mtr.append(list(map(int, new_row)))
    my_mtr[i - 1].append(sum(map(int, new_row)))
for i in my_mtr:
    print(' '.join(map(str, i)))
