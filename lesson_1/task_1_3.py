"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

x_1, y_1, x_2, y_2 = int(input('x1 = ')), int(input('y1 = ')), int(input('x2 = ')), int(input('y2 = '))

if x_1 == x_2:
    print('Формулы уравнения не существует.')
else:
    k = (y_1 - y_2) / (x_1 - x_2)
    b = y_1 - (k * x_1)
    if b == 0:
        if k == 1:
            print(f'y = x')
        else:
            print(f'y = {k}x')
    elif b < 0:
        if k == 1:
            print(f'y = x - {abs(b)}')
        else:
            print(f'y = {k}x - {abs(b)}')
    else:
        if k == 1:
            print(f'y = x + {b}')
        else:
            print(f'y = {k}x + {b}')
