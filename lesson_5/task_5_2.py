"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from itertools import zip_longest
from collections import deque
from functools import reduce

list_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def sum_16(num_1, num_2):
    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1
    res_sum = deque()
    rem = 0
    for el_1, el_2 in zip_longest(num_1[::-1], num_2[::-1], fillvalue='0'):
        sub_sum = list_16.index(el_1) + list_16.index(el_2) + rem
        if sub_sum >= 15:
            rem = sub_sum // 16
            sub_sum %= 16
        else:
            rem = 0
        res_sum.appendleft(list_16[sub_sum])
    if rem != 0:
        res_sum.appendleft(list_16[rem])
    return list(res_sum)


def mul_16(num_1, num_2):
    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1
    sums_mul = []
    k = []
    for el_2 in num_2[::-1]:
        rem = 0
        res_mul = deque()
        for el_1 in num_1[::-1]:
            sub_mul = list_16.index(el_1) * list_16.index(el_2) + rem
            if sub_mul >= 15:
                rem = sub_mul // 16
                sub_mul %= 16
            else:
                rem = 0
            res_mul.appendleft(list_16[sub_mul])
        if rem != 0:
            res_mul.appendleft(list_16[rem])
        if len(k) > 0:
            res_mul += k
        sums_mul.append(list(res_mul))
        k.append('0')
    return reduce(sum_16, sums_mul)


user_num_1 = list(input('Enter number 1: ').upper())
user_num_2 = list(input('Enter number 2: ').upper())
if all([el in list_16 for el in (user_num_1 + user_num_2)]):
    print(sum_16(user_num_1, user_num_2))
    print(mul_16(user_num_1, user_num_2))
else:
    print('Input error!')
