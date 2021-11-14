"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

my_lst = [i for i in range(2, 100)]
cnt = 0
for el in range(2, 10):
    cnt += len([i for i in my_lst if i % el == 0])
print(cnt)
