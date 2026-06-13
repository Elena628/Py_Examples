from typing import Iterable, Callable

s = [2, 1, 3, 4]

def my_for(it: Iterable, callback: Callable):
    iterator = iter(it)
    while True:
        try:
            value = next(iterator)
        except StopIteration:
            break
        callback(value)

my_for(s, lambda x: print('iter-value', x))