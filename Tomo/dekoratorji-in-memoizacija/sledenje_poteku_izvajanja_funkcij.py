# =============================================================================
# Sledenje poteku izvajanja funkcij
# =====================================================================@011777=
# 1. podnaloga
# Sestavite funkcijo `izpisi_rezultat(f)`, ki sprejme funkcijo enega argumenta
# `f` in vrne funkcijo, ki pri danem argumentu `x` vrne isti rezultat, vendar
# prej še izpiše vrednost argumenta in rezultata. Na primer:
# 
#     >>> def g(x): return x + 2
#     >>> glasni_g = izpisi_rezultat(g)
#     >>> 10 * g(5)
#     70
#     >>> 10 * glasni_g(5)
#     Pri argumentu 5 je rezultat 7
#     70
# 
# Če ob definiciji funkcije `f` uporabite dekorator `@izpisi_rezultat`, bo `f`
# definirana kot `izpisi_rezultat(osnovni_f)`, kjer je `osnovni_f` funkcija,
# kakršna bi bila `f`, če ne bi uporabili dekoratorja. Na primer, če definirate:
# 
#     @izpisi_rezultat
#     def fakulteta(n):
#         if n == 0:
#             return 1
#         else:
#             return n * fakulteta(n - 1)
# 
# Bo klic funkcije `fakulteta` izpisoval svoj rezultat:
# 
#     >>> fakulteta(5)
#     Pri argumentu 0 je rezultat 1
#     Pri argumentu 1 je rezultat 1
#     Pri argumentu 2 je rezultat 2
#     Pri argumentu 3 je rezultat 6
#     Pri argumentu 4 je rezultat 24
#     Pri argumentu 5 je rezultat 120
#     120
# =============================================================================
def izpisi_rezultat(f):
    '''izpisuje rezultat argumentov'''
    def glasni_f(x):
        y = f(x)
        print('Pri argumentu {} je rezultat {}'.format(x, y))
        return y
    return glasni_f
# =====================================================================@011778=
# 2. podnaloga
# Sestavite funkcijo `prikazi_izracune(f)`, ki sprejme funkcijo `f` poljubnega
# števila argumentov (pomagajte si z `*args`) in vrne funkcijo, ki pri danih
# argumentih vrne isti rezultat, vendar na začetku izračuna pove, kaj računa,
# na koncu pa izpiše opravljen izračun. Na primer, ob definiciji:
# 
#     @prikazi_izracune
#     def gcd(m, n):
#         if n == 0:
#             return m
#         else:
#             return gcd(n, m % n)
# 
# bo klic funkcije `gcd` izpisoval, kako poteka izračun:
# 
#     >>> gcd(123, 45)
#     gcd(123, 45) = ...
#     gcd(45, 33) = ...
#     gcd(33, 12) = ...
#     gcd(12, 9) = ...
#     gcd(9, 3) = ...
#     gcd(3, 0) = ...
#     gcd(3, 0) = 3
#     gcd(9, 3) = 3
#     gcd(12, 9) = 3
#     gcd(33, 12) = 3
#     gcd(45, 33) = 3
#     gcd(123, 45) = 3
#     3
# 
# Namig: do imena funkcije dostopate z `f.__name__`
# =============================================================================
def pikazi_izracune(f):
    def glasni_f(*args):
        klic = '{}({})'.format(f.__name__, ', '.join(map(str, args)))
        print('{} = ...'.format(klic))
        y = f(*args)
        print('{} = {}'.format(klic,y))
        return y
    return glasni_f
# =====================================================================@011779=
# 3. podnaloga
# Sestavite funkcijo `prikazi_izvajanje(f)`, ki deluje tako kot
# `prikazi_izracune`, le da zaradi lepšega pregleda nad izvajanjem v vsakem
# klicu funkcije bolj zamakne izpis izračunov. Na primer, če definirate:
# 
#     @prikazi_izracun
#     def fib(n):
#         if n == 0 or n == 1:
#             return n
#         else:
#             return fib(n - 1) + fib(n - 2)
# 
# Bo klic funkcije `fib` izpisoval:
# 
#     >>> fib(3)
#     fib(3) = ...
#       fib(2) = ...
#         fib(1) = ...
#         fib(1) = 1
#         fib(0) = ...
#         fib(0) = 0
#       fib(2) = 1
#       fib(1) = ...
#       fib(1) = 1
#     fib(3) = 2
#     2
# =============================================================================
k=0
def prikazi_izracun(f):
    def glasni_f(*args):
        global k
        klic = '{}({})'.format(f.__name__, ', '.join(map(str, args)))
        print('{}{} = ...'.format(k * ' ', klic))
        k+=3
        y = f(*args)
        k-=3
        print('{}{} = {}'.format(k*' ', klic,y))
        return y
    return glasni_f

