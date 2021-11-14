"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter

my_str = 'algorithms great course'
print(Counter(my_str))
haffman_dict = {'r': '000', 'a': '0010', 'g': '0011', 'o': '0100', 't': '0101', 's': '0110', ' ': '0111', 'e': '100',
                'l': '1010', 'i': '1011', 'h': '1100', 'm': '1101', 'c': '1110', 'u': '1111'}  # see task_8_2.png
haffman_str = ''
for letter in my_str:
    haffman_str += haffman_dict[letter]

print(haffman_str)
