"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его
цифр.
"""


def sum_dgt_func(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sum_dgt_func(num // 10)


input_nums = input('Enter your numbers: ').split()
if all(i.isdigit() for i in input_nums):
    input_nums = map(int, input_nums)
    max_dgt_sum = 0
    current_max_num = 0
    for el in input_nums:
        if sum_dgt_func(el) > max_dgt_sum:
            max_dgt_sum = sum_dgt_func(el)
            current_max_num = el
    print(f'Max sum for {current_max_num} is {max_dgt_sum}.')
else:
    print('Input data error!')
