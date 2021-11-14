"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""


def my_func(num):
    cnt = 1
    res = 1
    sum_res = 0
    while cnt != num:
        sum_res = sum_res + res
        res = res / -2
        cnt += 1
    return res


n = input('Enter "n": ')
if n.isdigit():
    print(my_func(int(n)))
else:
    print('Input data error!')
