from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)

def memo(neumna_f):
    ze_izracunani = {}
    def pametna_f(n):
        if n not in ze_izracunani:
            vrednost = neumna_f(n)
            ze_izracunani[n] = vrednost
        return ze_izracunani[n]
    return pametna_f

def fib_(n):
    ze_izracunani = {}
    def pametni_fib(n):
        if n in ze_izracunani:
            return ze_izracunani[n]
        if n<2:
            ze_izracunani[n] = 1
            return 1
        vrednost = pametni_fib(n-2) + pametni_fib(n-1)
        ze_izracunani[n] = vrednost
        return ze_izracunani[n]
    return pametni_fib(n)

@memo
def fib(n):
    if n<2:
        return 1
    return fib(n-2)+fib(n-1)


