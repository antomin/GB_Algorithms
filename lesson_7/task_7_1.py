"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По
возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint


def mod_bubble_sort(lst):
    cnt = 1
    while cnt < len(lst):
        is_sorted = True
        for el in range(len(lst) - cnt):
            if lst[el] < lst[el + 1]:
                lst[el], lst[el + 1] = lst[el + 1], lst[el]
                is_sorted = False
        if is_sorted is True:
            return lst
        cnt += 1
    return lst


my_list = [randint(-100, 100) for _ in range(10)]
print(my_list)
print(mod_bubble_sort(my_list))
