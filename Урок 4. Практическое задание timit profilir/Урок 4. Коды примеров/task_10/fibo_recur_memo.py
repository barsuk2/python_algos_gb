"""Фибо через рекурсию с мемоизацией через декоратор"""

import timeit


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)


n = 8

print(timeit.timeit("f(n)", setup="from __main__ import f, n"))

"""0.19176139999999997"""
