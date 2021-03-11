"Профилировка затрат памяти"

from memory_profiler import profile
from sys import getrefcount
from copy import deepcopy
import math


@profile
def func():
    d = list(range(10**5))
    a = deepcopy(d)
    # del d
    del a
    return a

func()
# @profile
def get_prime_numbers(count):
    prime_numbers = [2]
    next_number = 3

    while len(prime_numbers) < count:
        if is_prime(next_number, prime_numbers):
            prime_numbers.append(next_number)
        next_number += 1

    return prime_numbers

# @profile
def is_prime(num, prime_numbers):
    limit = int(math.sqrt(num)) + 1
    for i in prime_numbers:
        if i > limit:
            break
        if num % i == 0:
            return False
    return True
# Проблем с памятью нет. Всё в пределах нормы.
# get_prime_numbers(5)

"""Профилировка затрат памяти в разрезе коллекций"""
from guppy import hpy

h = hpy()

x = list(range(100000))
y = deepcopy(x)

print(h.heap())