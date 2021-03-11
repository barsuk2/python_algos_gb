import time


# start = time.perf_counter()
def time_count(fn):
    def wrapper(arg):
        start = time.perf_counter()
        fn(arg)
        finish = time.perf_counter() - start
        print(finish)
    return wrapper


@time_count
def fill_list(n):
    list_ = []
    for i in range(10 ** n):
        list_.append(i)


fill_list(6)


@time_count
def fill_dict(n):
    dict_ = {}
    for ind, val in enumerate(range(10 ** n)):
        dict_[str(ind)] = val


fill_dict(6)

def hello():
    print('hello')


def add_hello(fn):
    print('напасить до исполение функции')
    fn()
    print('напасить после исполение функции')

add_hello(hello)