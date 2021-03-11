"""Профилировка затрат памяти"""
# https://pypi.org/project/guppy3/

from guppy import hpy
from copy import deepcopy

h = hpy()

x = list(range(100000))
y = deepcopy(x)

print(h.heap())
