"""Сортировка вставками"""

import timeit
import random


def insertion_sort(lst_obj):
    for i in range(len(lst_obj)):
        v = lst_obj[i]
        j = i

        while (lst_obj[j-1] > v) and (j > 0):

            lst_obj[j] = lst_obj[j-1]
            j = j - 1

        lst_obj[j] = v
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("insertion_sort(orig_list)", \
    setup="from __main__ import insertion_sort, orig_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("insertion_sort(orig_list)", \
    setup="from __main__ import insertion_sort, orig_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("insertion_sort(orig_list)", \
    setup="from __main__ import insertion_sort, orig_list", number=1))
