def _number(num):
    ind = 0
    for i in range(1, num + 1):
        a, b = divmod(num, i)
        if b == 0:
            ind += 1
    if ind == 2:
        return 1  # print(f'{num} - простое число')
    return 0  # print(f'{num} - не простое число')


prime_num = [x for x in range(1, 10) if _number(x) == 1]
# print(prime_num)
