"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple

# count_org = int(input('Введите количество предприятий для расчета прибыли:'))
namedtuple_obj = namedtuple('Org', ['id', 'name', 'profit_1', 'profit_2', 'profit_3', 'profit_4', 'sum_'])
# list_1 = []
# for i in range(1,count_org+1):
#     name_org = input('Введите название предприятия:')
#     profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):')
#     list_1.append(namedtuple_obj(i, name_org, int(profit.split()[0]),
#                                  int(profit.split()[1]),
#                                  int(profit.split()[2]),
#                                  int(profit.split()[3]),
#                                  sum([int(i) for i in profit.split()])
#                                  )
#                   )
count_org = 4
list_ = [namedtuple_obj(
    id=1, name='ООО', profit_1=723, profit_2=721, profit_3=856, profit_4=654, sum_=2400),
    namedtuple_obj(
        id=2, name='ОАО', profit_1=789, profit_2=587, profit_3=463, profit_4=463, sum_=3400),
    namedtuple_obj(
        id=3, name='РАО', profit_1=589, profit_2=889, profit_3=565, profit_4=763, sum_=3100),
    namedtuple_obj(
        id=4, name='ФГБУ', profit_1=389, profit_2=587, profit_3=563, profit_4=964, sum_=2900)]
profit_year = 0
for i in list_:
    print(f'Годовая прибыль организации {i.name} = {i.sum_}')
    profit_year += i.sum_

print(f'Средняя годовая прибыль по всем организвциям = {profit_year / count_org}')
print(f'Предприятия, с прибылью выше среднего значения: '
      f'{[i.name for i in list_ if i.sum_ > profit_year / count_org]} больше средней')
print(f'Годовая прибыль организации {[i.name for i in list_ if i.sum_ < profit_year / count_org]} меньше средней')
