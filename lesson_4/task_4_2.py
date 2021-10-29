"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в
виде комментариев в файле с кодом.
"""
import cProfile
from math import log


def func_range(num):
    n = 100
    while num > n / log(n):
        n += 1000
    return num


def func_erat(i):
    n = func_range(i)
    nums = [i for i in range(2, n + 1)]
    for num in nums:
        if num != 0:
            for el in range(2 * num, n + 1, num):
                nums[el - 2] = 0
    result = [i for i in nums if i != 0]
    if len(result) > i:
        return result[i - 1]
    return result
    # return 0


def my_func(i):
    n = func_range(i)
    nums = []
    for i in range(2, n + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            nums.append(i)
    # if len(nums) > i:
    #     return nums[i - 1]
    return nums


cProfile.run('func_erat(1000)')
cProfile.run('my_func(1000)')
