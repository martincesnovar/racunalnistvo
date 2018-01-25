# =============================================================================
# Minsko polje
# =====================================================================@010509=
# 1. podnaloga
# Robotka moramo prepeljati čez minirano območje, ki je pravokotne oblike
# in je razdeljeno na $m \times n$ kvadratnih polj. Na začetku je robotek
# parkiran v zgornjem levem polju s koordinatama $(1, 1)$. Spodnje desno
# polje ima koordinati $(m,n)$. Robotek se lahko v vsakem koraku pomakne
# za eno polje navzdol ali za eno polje v desno. Navzgor ali na desno se
# ne more premikati. Prav tako se ne more premikati diagonalni ali
# preskakovati polj. Na nekaterih poljih so zakopane mine, ki se jim mora
# robotek izogniti. Na koliko načinov lahko pride iz začetnega na končno
# polje? Predpostavite lahko, da na začetnem in končnem polju ni min.
# 
# Napišite funkcijo `stevilo_poti(m, n, mine)`, kjer sta `m` in `n` celi
# števili, ki predstavljata velikost polja. Mine je seznam parov in sicer
# so to koordinate polj, kjer so zakopane mine. Funkcija naj vrne število
# različnih poti med $(1, 1)$ in $(m, n)$, ki se izognejo minam. Zgled:
# 
#     >>> stevilo_poti(5, 4, [])
#     35
#     >>> stevilo_poti(5, 4, [(2, 3), (4, 3)])
#     9
# =============================================================================
from functools import lru_cache
@lru_cache(maxsize=None)
def stevilo_poti_1(m,n,mine):
    '''vrne stevilo poti'''
    if m==1 or n==1:
        return 1
    if (m,n) in mine:
        return 0
    return stevilo_poti_1(m-1,n, mine) + stevilo_poti_1(m,n-1,mine)
    

def stevilo_poti_2(m,n,mine):
    '''vrne stevilo poti'''
    return stevilo_poti_1(m,n,tuple(mine))

def stevilo_poti(m, n, mine):
    '''Vrne število vseh poti v mreži m x n, ki se izognejo vsem minam.'''
    polje = [[0 for j in range(n+1)] for i in range(m+1)]
    polje[1][1] = 1
    for r, c in mine:
        polje[r][c] = None
    for r in range(1, m+1):
        for c in range(1, n+1):
            if polje[r][c] is not None:
                if polje[r-1][c] is not None:
                    polje[r][c] += polje[r-1][c]
                if polje[r][c-1] is not None: polje[r][c] += polje[r][c-1]
    return polje[m][n]

