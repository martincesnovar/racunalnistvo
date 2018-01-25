# =============================================================================
# Enostavne naloge z rekurzijo
# =====================================================================@011120=
# 1. podnaloga
# Sestavite funkcijo `fakulteta(n)`, ki izračuna fakulteto števila `n`.
# Argument `n` je nenegativno celo število. Zgled:
# 
#     >>> fakulteta(5)
#     120
# 
# Nalogo rešite z rekurzijo, torej brez uporabe zanke `for` oziroma `while`.
# =============================================================================

def fakulteta(n):
    assert n>=0
    if n==0:
        return 1
    return n*fakulteta(n-1)


# =====================================================================@011121=
# 2. podnaloga
# Sestavite funkcijo `gcd(m, n)`, ki izračuna največji skupni delitelj
# števil `m` in `n`. Argumenta `m` in `n` sta nenegativni celi števili.
# Če je $m = 0$ in $n = 0$, naj funkcija vrne vrednost `None`. Zgled:
# 
#     >>> gcd(10, 15)
#     5
# 
# Nalogo rešite z rekurzijo, torej brez uporabe zanke `for` oziroma `while`.
# =============================================================================

def gcd(m,n):
    if m==n==0:
        return None
    if n==0:
        return m
    return gcd(n,m%n)

# =====================================================================@011122=
# 3. podnaloga
# Sestavite funkcijo `cantor(n)`, ki kot argument dobi nenegativno celo
# število `n`. Funkcija naj vrne niz dolžine $3^n$ z $n$-tim približkom
# [Cantorjeve množice](http://sl.wikipedia.org/wiki/Cantorjeva_množica).
# Srednja tretjina niza sestoji iz samih presledkov, prva in zadnja tretjina
# niza pa sta $(n-1)$-ta približka Cantorjeve množice; $0$-ti približek
# Cantorjeve množice je niz `'*'`. Zgled:
# 
#     >>> cantor(0)
#     '*'
#     >>> cantor(1)
#     '* *'
#     >>> cantor(2)
#     '* *   * *'
#     >>> cantor(3)
#     '* *   * *         * *   * *'
# 
# Nalogo rešite z rekurzijo, torej brez uporabe zanke `for` oziroma `while`.
# =============================================================================

def cantor(n):
    niz = ''
    if n==0:
        return '*'
    cantorn1 = cantor(n-1)
    return cantorn1 + ' '*len(cantorn1) + cantorn1
    

# =====================================================================@011123=
# 4. podnaloga
# Sestavite funkcijo `fibonacci(n)`, ki vrne $n$-to Fibonaccijevo število.
# Nalogo bomo rešili z rekurzivno funkcijo, ki uporabi _akumulatorja_, to sta
# pomožna argumenta, v katerih si podajamo delne rezultate.
# 
# Najprej primer uporabe akumulatorjev (`x` je akumulator):
# 
#     def potenca(a, n, x=1):
#         """Izračunaj n-to potenco a."""
#         if n == 0:
#             return x
#         else:
#             return potenca(a, n-1, a*x)
# 
# Na začetku je `x` enak `1`. V vsakem klicu ga množimo z `a`, torej bo po
# `k` klicih enak `a ** k`. Ko pridemo do `n == 0`, je bilo klicev `n` in
# ima `x` želeno vrednost `a ** n`. V nekem smislu smo z rekurzijo simulirali
# zanko, katere števec je `n` in pomožna spremenljivka `x`:
# 
#      x = 1
#      while n > 0:
#          x = a * x
#          n = n - 1
#      return x
# 
# Funkcija `fibonacci` bo imela _dva_ akumulatorja, `fibonacci(n, x=0, y=1)` in
# bo simulirala zanko
# 
#      x = 0
#      y = 1
#      while n > 0:
#          x, y = y, x + y
#          n = n -1
#      return x
# 
# Zgled:
# 
#     >>> fibonacci(7)
#     13
# 
# Testi bodo vašo rešitev preizkusili pri velikih vrednostih argumenta `n`,
# zato rešitev napišite učinkovito.
# =============================================================================

def fibonacci_1(n, _cache={}):
    '''unčinkovita rekurzija
    https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci(n-1) + fibonacci(n-2))
    return n

def fibonacci(n,x=0,y=1):
    if n==0:
        return x
    return fibonacci(n-1,y,x+y)

