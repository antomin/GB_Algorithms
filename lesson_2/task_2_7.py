"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def sum_func(num):
    if num == 0:
        return 0
    else:
        return num + sum_func(num - 1)


n = int(input('Enter "n": '))
if sum_func(n) == n * (n + 1) / 2:
    print(True)
else:
    print(False)
