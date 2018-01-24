# =============================================================================
# Funkcije višjih redov
#
# Spodaj je primer funkcije višjega reda `eksponentna(a)`, ki kot argument
# dobi število $a$ in vrne funkcijo $x \mapsto a^x$. Zgled uporabe:
# 
#     >>> f = eksponentna(2)
#     >>> f(5)
#     32
#     >>> f(0.5)
#     1.4142135623730951
# =====================================================================@011780=
# 1. podnaloga
# Sestavite funkcijo `linearna(a, b)`, ki kot argumenta dobi števili $a$
# in $b$ ter vrne funkcijo $x \mapsto a \cdot x + b$. Zgled:
# 
#     >>> f = linearna(3, 2)
#     >>> f(0.5)
#     3.5
# =============================================================================
import math

def eksponentna(a):
    return (lambda x: a ** x)

def linearna(a, b):
    return lambda x: a*x+b
# =====================================================================@011781=
# 2. podnaloga
# Sestavite funkcijo `kompozitum(f, g)`, ki kot argumenta dobi funkciji
# `f` in `g`, ter vrne njun kompozitum.
# Zgled:
# 
#     >>> import math
#     >>> f = kompozitum(abs, math.sin)
#     >>> f(3*math.pi/2)
#     1.0
# =============================================================================
def kompozitum(f,g):
    return lambda x:f(g(x))
# =====================================================================@011782=
# 3. podnaloga
# Sestavite funkcijo `odvod(f, epsilon=10e-5)`, ki sprejme funkcijo `f`
# in vrne njen odvod (ki je spet funkcija). Odvod v točki `x` ocenimo z izrazom
# $f'(x) \approx (f(x + \epsilon/2) - f(x - \epsilon/2)) / \epsilon$.
# Zgled:
# 
#     >>> f = odvod((lambda x: x * x + 1))
#     >>> f(1.0)
#     2.000000000002
# =============================================================================
def odvod(f, eps=10e-5):
    return lambda x:(f(x+eps/2)-f(x-eps/2))/eps
# =====================================================================@011783=
# 4. podnaloga
# Sestavite funkcijo `uporabi_nkrat(f, x, n)`, ki kot argumente dobi
# funkcijo `f`, število `x` in naravno število `n` ter vrne število, ki
# ga dobimo, če na `x` funkcijo `f` uporabimo $n$-krat. Zgled:
# 
#     >>> collatz = lambda x: x // 2 if x % 2 == 0 else 3*x + 1
#     >>> uporabi_nkrat(collatz, 13, 7)
#     4
# =============================================================================
def uporabi_nkrat(f,x,n):
    for _ in range(n):
        x=f(x)
    return x
# =====================================================================@011784=
# 5. podnaloga
# Sestavite funkcijo `uporabi_vse(sez, x)`, ki kot argumenta dobi seznama
# funkcij `sez` in število `x`. Funkcija naj vsako od funkcij iz `sez` uporabi
# na `x` in vrne seznam tako dobljenih števil. Zgled:
# 
#     >>> f = lambda x: x**2 - 3*x + 4
#     >>> g = lambda x: x**x
#     >>> uporabi_vse([math.sin, math.cos, f, g, abs, int], math.pi/2)
#     [1.0, 6.123233995736766e-17, 1.7550121198876498, 2.032658322210728, 1.5707963267948966, 1]
# =============================================================================
def uporabi_vse(sez, x):
    vrednosti = []
    for fun in sez:
        vrednosti.append(fun(x))
    return vrednosti
