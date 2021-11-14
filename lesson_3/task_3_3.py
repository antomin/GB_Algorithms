"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import sample

my_list = sample([i for i in range(1, 100)], 10)
print(my_list)
max_el = max(my_list)
min_el = min(my_list)
"""Можно обойтись без переменных max_el и min_el. Но я подумал, что это будет дорого - вычислять эти значения каждую
итерацию. Прокоментируйте пожалуйста, это правильно?"""
for idx, el in enumerate(my_list):
    if el == min_el:
        my_list[idx] = max_el
    elif el == max_el:
        my_list[idx] = min_el
print(my_list)
