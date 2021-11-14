"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

x, y = input('Введите две буквы.\nОт: '), input('До: ')

if 65 <= ord(x.upper()) <= 90 and 65 <= ord(y.upper()) <= 90:
    print(f'{x.upper()} - {ord(x.upper()) - 64}-я буква алфавита.')
    print(f'{y.upper()} - {ord(y.upper()) - 64}-я буква алфавита.')
    if ord(x.upper()) < ord(y.upper()):
        print(f'Между ними {ord(y.upper()) - ord(x.upper()) - 1} букв.')
    else:
        print(f'Между ними {ord(x.upper()) - ord(y.upper()) - 1} букв.')
else:
    print('Неверные данные!')
