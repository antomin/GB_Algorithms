"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей
ОС.
"""

# Linux x64 Python 3.9.5
from memory_profiler import profile
import objgraph

"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


@profile
def my_func():
    num = '2453562352363456'  # input('Enter number: ')
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


my_func()

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     19     39.0 MiB     39.0 MiB           1   @profile
#     20                                         def my_func():
#     21     39.0 MiB      0.0 MiB           1       num = '2453562352363456'  # input('Enter number: ')
#     22     39.0 MiB      0.0 MiB           1       if num.isdigit():
#     23     39.0 MiB      0.0 MiB           1           ev_nums_cnt = 0
#     24     39.0 MiB      0.0 MiB           1           ev_nums_ls = []
#     25     39.0 MiB      0.0 MiB           1           od_nums_cnt = 0
#     26     39.0 MiB      0.0 MiB           1           od_nums_ls = []
#     27     39.0 MiB      0.0 MiB          17           for i in num:
#     28     39.0 MiB      0.0 MiB          16               if int(i) % 2 == 0:
#     29     39.0 MiB      0.0 MiB           8                   ev_nums_cnt += 1
#     30     39.0 MiB      0.0 MiB           8                   ev_nums_ls.append(i)
#     31                                                     else:
#     32     39.0 MiB      0.0 MiB           8                   od_nums_cnt += 1
#     33     39.0 MiB      0.0 MiB           8                   od_nums_ls.append(i)
#     34     39.0 MiB      0.0 MiB           1           print(f'Even numbers - {ev_nums_cnt} ({", ".join(ev_nums_ls)})')
#     35     39.0 MiB      0.0 MiB           1           print(f'Odd numbers - {od_nums_cnt} ({", ".join(od_nums_ls)})')
#     36                                             else:
#     37                                                 print('Input data error!')

"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

objgraph.show_growth()
@profile
def my_func():
    my_lst = [i for i in range(2, 100)]
    cnt = 0
    for el in range(2, 10):
        cnt += len([i for i in my_lst if i % el == 0])  # 808 вхождений в переменную cnt. Это можно считать утечкой?
    print(cnt)


my_func()
objgraph.show_growth()
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     47     39.0 MiB     39.0 MiB           1   @profile
#     48                                         def my_func():
#     49     39.0 MiB      0.0 MiB         101       my_lst = [i for i in range(2, 100)]
#     50     39.0 MiB      0.0 MiB           1       cnt = 0
#     51     39.0 MiB      0.0 MiB           9       for el in range(2, 10):
#     52     39.0 MiB      0.0 MiB         808           cnt += len([i for i in my_lst if i % el == 0])  # 808 вхождений в переменную cnt. Это можно считать утечкой?
#     53     39.0 MiB      0.0 MiB           1       print(cnt)

# Кол-во созданных объектов (но что-то тут не так)

# function                      12487    +12487
# dict                           7459     +7459
# tuple                          7002     +7002
# weakref                        2527     +2527
# cell                           2239     +2239
# type                           1611     +1611
# getset_descriptor              1554     +1554
# wrapper_descriptor             1294     +1294
# builtin_function_or_method     1167     +1167
# list                           1166     +1166