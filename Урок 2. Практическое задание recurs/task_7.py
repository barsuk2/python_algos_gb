"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
P = 100

def funk(n):
    if n == 1:
        return 1
    return n+ funk(n-1)

def formula(n):
    return n*(n+1)/2


print(True if funk(P) == formula(P) else False )
