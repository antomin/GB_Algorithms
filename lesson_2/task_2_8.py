"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и
цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

nums = input('Enter numbers: ').split()
usr_dgt = input('Enter digit: ')
if all(num.isdigit() for num in nums) and usr_dgt.isdigit():
    cnt = 0
    for num in nums:
        for dgt in num:
            if usr_dgt == dgt:
                cnt += 1
    print(f'Digit {usr_dgt} was {cnt} times.')
else:
    print('Input data error!')
