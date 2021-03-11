def arrey_search(A: list, N: int, x: int):
    """
    ОСуществляет поиск числа x d массиве A
    от 0 до N-1
    Возвращает индекс x d массиве А
    Или -1,  если такого нет
    Если в массиве несколько одинаковых элементов,
    то вернуть индекс первого
    :param A:
    :param N:
    :param x:
    :return:
    """
    for i in range(N):
        if A[i] != x:
            return i
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = arrey_search(A1, 5, 8)
    if m == -1:
        print('#test1 - ok')
    else:
        print('#test1 - fail')

    A2 = [-1, -2, -3, -4, -5]
    m = arrey_search(A2, 5, -3)
    if m == 2:
        print('#test2 - ok')
    else:
        print('#test2 - fail')

    A3 = [10, -2, 10, 10, -5]
    m = arrey_search(A3, 5, 10)
    if m == 2:
        print('#test3 - ok')
    else:
        print('#test3 - fail')


# test_array_search()


def invert_arrey(A: list, N: int):
    """
    Обращение массива от 0 до N-1
    :param A:
    :param N:
    :return:
    """
    for i in range(N//2):
        A[i] , A[N-1-i] = A[N-1-i], A[i]
    return A


# print(invert_arrey([1, 2, 3, 4, 5], 5))



def test_invert_arrey():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_arrey(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print('#test - ок')
    else:
        print('#test - false')


    A2 = [0,0,0,0,0,0,0,0,10]
    print(A2)
    invert_arrey(A2,9)
    print(A2)
    if A2 == [10,0,0,0,0,0,0,0,0]:
        print('#test - ок')
    else:
        print('#test - false')


test_invert_arrey()