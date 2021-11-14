"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import sample

my_list = sample([i for i in range(-10, 4)], 10)
print(my_list)
res_el = max([el for el in my_list if el < 0])
print(f'Element {res_el} have index {my_list.index(res_el)}')
