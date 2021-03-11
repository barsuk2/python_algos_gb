# суммирование последовательность

def sum_recurs(n):
    if isinstance(n, int):
        n = list(range(n + 1))
    if len(n) == 1:
        return n[0]
    return n[0] + sum_recurs(n[1:])


# print(sum_recurs(20))

"""Рекурсия против цикла
Вывод чисел по убыванию, начиная с текущего и до нуля"""


def display_list(n):
    print(n)
    if n <= 0:
        return
    display_list(n - 1)


# display_list(6

"""Изменение значений переменных
вывести числа с n по m
print(recursion(20, 15))
print(recursion(10, 15))
20 19 18 17 16 15
10 11 12 13 14 15
"""


def recursion(a, b):
    # базовый случай когда a == b
    if a == b:
        return str (a)
    # шаг рекурсии
    # рекурсивное условие
    if a > b:
        return f'{str(a)} {recursion(a - 1, b)}'
    # шаг рекурсии
    # рекурсивное условие
    if a < b:
        return f'{str(a)} {recursion(a + 1, b)}'


print(recursion(15, 12))
print(recursion(12, 15))

def convert_to_str(n, base_val):
    convert_str = "0123456789ABCDEF"
    # Базовый случай, в котором n должно быть меньше,
    # чем основание, по которому мы конвертируем
    if n < base_val:
        return convert_str[n]
    # Здесь выполняются 2-й и 3-й законы рекурсии
    # выполняется рекурсивный вызов и происходит
    # уменьшение размера задания с помощью деления
    else:
        return convert_to_str(n // base_val, base_val) + convert_str[n % base_val]


print(convert_to_str(17, 16))