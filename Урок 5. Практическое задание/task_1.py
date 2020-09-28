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
namedtuple_obj = namedtuple('Org', ['id', 'name', 'profit_1', 'profit_2', 'profit_3', 'profit_4'])
org_1 = namedtuple_obj(
    id=1,
    name='ООО',
    profit_1 =723,
    profit_2 =721,
    profit_3 =856,
    profit_4 =654,
)
org_2 = namedtuple_obj(
    id=2,
    name='ОАО',
    profit_1 =789,
    profit_2 =587,
    profit_3 =463,
    profit_4 =963,

)
profit_year_org1 = sum(org_1[-4:])
profit_year_org2 = sum(org_2[-4:])
print(f'Годовая прибыль организации {org_1.name} = {profit_year_org1}')
print(f'Годовая прибыль организации {org_2.name} = {profit_year_org2}')
print(f'Средняя годовая прибыль по всем организвциям = {(profit_year_org1+profit_year_org2) / 2}')
print(f'Годовая прибыль организации {org_1.name if profit_year_org1 > profit_year_org2 else org_2.name} больше средней')
print(f'Годовая прибыль организации {org_1.name if profit_year_org1 < profit_year_org2 else org_2.name} меньше средней')
