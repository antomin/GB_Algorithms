"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import cProfile
import random
"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться.
"""


def my_func(lst):
    lst.sort()
    return lst[0], lst[1]


def my_func_2(lst):
    min_el_0 = min(lst)
    lst.pop(min_el_0)
    min_el_1 = min(lst)
    return min_el_0, min_el_1


def my_func_3(lst):
    min_el_0 = 0
    min_el_1 = 0
    for i in lst:
        if i < min_el_0:
            min_el_0 = i
    lst.pop(min_el_0)
    for i in lst:
        if i < min_el_1:
            min_el_1 = i
    return min_el_0, min_el_1


my_list = [random.randint(0, 10000000) for _ in range(1000000)]
cProfile.run('my_func(my_list)')
cProfile.run('my_func_2(my_list)')
cProfile.run('my_func_3(my_list)')
