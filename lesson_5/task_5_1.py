"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""

import collections

comps = collections.defaultdict(list)
comps_cat = collections.defaultdict(list)
nums_comp = int(input('Enter numbers of enterprises: '))
sum_profit = 0

for comp in range(1, nums_comp + 1):
    name_comp = input(f'Enter name of enterprise {comp}: ')
    for quarter in range(1, 5):
        comps[name_comp].append(int(input(f'Enter profit {name_comp} in quarter {quarter}: ')))
    sum_profit += sum(comps.get(name_comp))

avg_profit = round(sum_profit / nums_comp, 2)

for comp, profit in comps.items():
    if sum(profit) > avg_profit:
        comps_cat['high_avg_comps'].append(comp)
    elif sum(profit) < avg_profit:
        comps_cat['low_avg_comps'].append(comp)

print(f'Enterprises with high profit: {", ".join(comps_cat.get("high_avg_comps"))}')
print(f'Enterprises with low profit: {", ".join(comps_cat.get("low_avg_comps"))}')
