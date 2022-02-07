import time

_m = 32768
_b = 9757
_c = 6925

def _rand(seed):
    n = seed % _m
    while True:
        n = (n * _b + _c) % _m
        yield n

_r = _rand(int(time.time()))

def rand():
    return _r.__next__()

def randDouble():
    return _r.__next__() / _m
