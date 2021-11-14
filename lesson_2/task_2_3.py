"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, то надо вывести число 6843.
"""


def revers_func(num):
    res = 0
    while num > 0:
        res = res * 10 + num % 10
        num = num // 10
    return res


print(revers_func(nt(input('Enter number: '))))
