"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только
из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""

import hashlib


def sub_str_gen(string):
    sub_str_lst = []
    for i in range(1, len(string)):
        for idx in range(len(string)):
            sub_str = string[idx:idx + i]
            if sub_str not in sub_str_lst:
                sub_str_lst.append(sub_str)
    return sub_str_lst


def sub_counter(my_str):
    cnt_dict = {}
    for sub_str in sub_str_gen(my_str):
        cnt = 0
        hash_sub_str = hashlib.sha1(sub_str.encode('utf-8')).hexdigest()
        for i in range(len(my_str) - len(sub_str) + 1):
            if hash_sub_str == hashlib.sha1(my_str[i:i + len(sub_str)].encode('utf-8')).hexdigest():
                cnt += 1
        cnt_dict[sub_str] = cnt
    return cnt_dict


my_string = 'abracadabra'
for k, v in sub_counter(my_string).items():
    print(k, v)
