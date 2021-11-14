"""
Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
вправо и влево на два знака.
"""

print('5 = ' + str(bin(5))[2:])
print('6 = ' + str(bin(6))[2:])
print(f'5 & 6 = {5 & 6} ({str(bin(4))[2:]})')
print(f'5 | 6 = {5 | 6} ({str(bin(7))[2:]})')
print(f'5 ^ 6 = {5 ^ 6} ({str(bin(3))[2:]})')
print(f'5 << 2 = {5 << 2} ({str(bin(20))[2:]})')
print(f'5 >> 2 = {5 >> 2} ({str(bin(1))[2:]})')
