# =============================================================================
# Razčlenitve
#
# Naraščajočemu zaporedju neničelnih naravnih števil
#   $m_1 \le m_2 \le \cdots \le m_k$,
# za katere velja
#   $m_1 + m_2 + \cdots + m_k = n$,
# pravimo _razčlenitev naravnega števila $n$ na $k$ členov_.
# Na primer, $1 + 3 + 7$ in $2 + 4 + 5$ sta dve razčlenitvi števila $11$
# na $3$ člene.
# 
# S $p_k(n)$ označimo število vseh razčlenitev števila $n$ na $k$ členov.
# Očitno velja $p_k(n) = 0$, če je $k > n$. Če dodatno predpostavimo še
# $p_0(0) = 1$ ter $p_0(n) = 0$ za vse $n > 0$, potem velja
#   $p_k(n) = p_{k - 1}(n - 1) + p_k(n - k)$,
# kar lahko pokažemo na sledeč način:
# 
# * če je prvi člen zaporedja enak $1$, potem preostanek zaporedja tvori
#   razčlenitev števila $n - 1$ na $k - 1$ členov;
# * če je prvi člen zaporedja večji od $1$, potem lahko vsakemu izmed $k$
#   členov odštejemo $1$ (saj je zaporedje naraščajoče) in s tem dobimo
#   razčlenitev števila $n - k$ na $k$ členov.
# =====================================================================@010384=
# 1. podnaloga
# Sestavite funkcijo `stevilo_razclenitev(n, k)`, ki vrne število vseh
# razčlenitev števila `n` na `k` členov. Primer:
# 
#     >>> stevilo_razclenitev(7, 3)
#     4
#     >>> stevilo_razclenitev(6, 2)
#     3
# =============================================================================


def stevilo_razclenitev(n, k):
    '''Vrne število razčlenitev'''
    if k>n:
        return 0
    elif k==0:
        return 1 if n==0 else 0
    return stevilo_razclenitev(n-1, k-1) + stevilo_razclenitev(n-k,k)

# =====================================================================@010385=
# 2. podnaloga
# Sestavite generator `razclenitve(n, k)`, ki zaporedoma vrača vse
# razčlenitve števila `n` na `k` členov, predstavljene s seznami števil.
# Generator naj razčlenitve vrača v leksikografskem vrstnem redu. Primer:
# 
#     >>> for razclenitev in razclenitve(7, 3):
#     ...     print(razclenitev)
#     [1, 1, 5]
#     [1, 2, 4]
#     [1, 3, 3]
#     [2, 2, 3]
# 
# _Opomba:_ Razčlenitev števila 0 na 0 členov predstavimo s praznim seznamom.
# =============================================================================

def razclenitve(n,k):
    ''''''
    if k==n==0:
        yield []
    elif 0<k<=n:
        for razcl in razclenitve(n-1,k-1):
            yield [1] + razcl
        for razlc in razclenitve(n-k,k):
            yield [t+1 for t in razlc]

# =====================================================================@010386=
# 3. podnaloga
# Sestavite generator `vse_razclenitve(n)`, ki zaporedoma vrača vse razčlenitve
# števila `n` (ne glede na število členov). Generator naj razčlenitve vrača v
# leksikografskem vrstnem redu. Primer:
# 
#     >>> for razclenitev in vse_razclenitve(6):
#     ...     print(razclenitev)
#     [1, 1, 1, 1, 1, 1]
#     [1, 1, 1, 1, 2]
#     [1, 1, 1, 3]
#     [1, 1, 2, 2]
#     [1, 1, 4]
#     [1, 2, 3]
#     [1, 5]
#     [2, 2, 2]
#     [2, 4]
#     [3, 3]
#     [6]
# =============================================================================

def vse_razclenitve(n,m=1):
    ''''''
    if n==0:
        yield []
    for x in range(m, n+1):
        for razlc in vse_razclenitve(n-x,x):
            yield [x] + razlc
