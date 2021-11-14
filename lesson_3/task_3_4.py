"""
Определить, какое число в массиве встречается чаще всего.
"""

my_list = [1, 3, 4, 3, 6, 4, 7, 1, 1, 1, 7, 6, 1, 1, 7]
max_cnt_el = 0
for el in set(my_list):
    if my_list.count(el) > my_list.count(max_cnt_el):
        max_cnt_el = el
print(f'Element {max_cnt_el} have {my_list.count(max_cnt_el)} entry. It is maximum')
