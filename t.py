import functools


def func_plus(a,b):
    return a+b


def func_minus(a,b):
    return a-b


def calc(f,a,b):
    return f(a,b)


def funcit(max):
    n = 0
    while n < max:
        n += 1
        yield n

it = funcit(5)
for i in it:
    print(i)
