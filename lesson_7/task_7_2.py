"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import uniform


def merge_lists(l_lst, r_lst):
    res_lst = []
    l_idx = 0
    r_idx = 0
    while l_idx < len(l_lst) and r_idx < len(r_lst):
        if l_lst[l_idx] < r_lst[r_idx]:
            res_lst.append(l_lst[l_idx])
            l_idx += 1
        else:
            res_lst.append(r_lst[r_idx])
            r_idx += 1
    if l_idx < len(l_lst):
        res_lst += l_lst[l_idx:]
    if r_idx < len(r_lst):
        res_lst += r_lst[r_idx:]
    return res_lst


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        l_lst = merge_sort(lst[:len(lst) // 2])
        r_lst = merge_sort(lst[len(lst) // 2:])
        return merge_lists(l_lst, r_lst)


my_list = [uniform(0, 50) for _ in range(10)]
print(my_list)
print(merge_sort(my_list))
