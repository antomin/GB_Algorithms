"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input('Enter number: ')
if num.isdigit():
    ev_nums_cnt = 0
    ev_nums_ls = []
    od_nums_cnt = 0
    od_nums_ls = []
    for i in num:
        if int(i) % 2 == 0:
            ev_nums_cnt += 1
            ev_nums_ls.append(i)
        else:
            od_nums_cnt += 1
            od_nums_ls.append(i)
    print(f'Even numbers - {ev_nums_cnt} ({", ".join(ev_nums_ls)})')
    print(f'Odd numbers - {od_nums_cnt} ({", ".join(od_nums_ls)})')
else:
    print('Input data error!')
