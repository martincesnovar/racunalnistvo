# =============================================================================
# SSCŠ
#
# Seznam seznamov celih števil (SSCŠ) je seznam, katerega elementi so bodisi
# cela števila bodisi seznami seznamov celih števil. Da bo enostavneje,
# recimo, da je tudi prazen seznam SSCŠ. Nekaj primerov:
# 
#     [-1, 2, -3]
#     [1, [2], 3, [2, 3, 4]]
#     [[[[2]], 1], [2, [[-3], [4]]]]
# =====================================================================@010376=
# 1. podnaloga
# Sestavi funkcijo `prestejStevila(sscs)`, ki prešteje, koliko je
# v sscs celih števil. Za primere od zgoraj so rezultati:
# 
#     3
#     6
#     5
# =============================================================================

def prestejStevila(sscs):
    '''Koliko je celih števil'''
    stevila = 0
    for el in sscs:
        if isinstance(el, list):
            stevila += prestejStevila(el)
        elif isinstance(el, int):
            stevila+=1
    return stevila

# =====================================================================@010377=
# 2. podnaloga
# Sestavi funkcijo `prestejNegativnaStevila(sscs)`, ki prešteje,
# koliko je v seznamu seznamov negativnih celih števil.
# Za primere od zgoraj so rezultati:
# 
#     2
#     0
#     1
# =============================================================================

def prestejNegativnaStevila(sscs):
    '''Koliko je celih negativnih števil'''
    stevila = 0
    for el in sscs:
        if isinstance(el, list):
            stevila += prestejNegativnaStevila(el)
        elif isinstance(el, int):
            if el <0:
                stevila+=1
    return stevila


# =====================================================================@010378=
# 3. podnaloga
# Sestavi funkcijo `sestejStevila(sscs)`, ki sešteje vsa cela števila
# v seznamu seznamov celih števil. Za primere od zgoraj so rezultati:
# 
#     -2
#     15
#     6
# =============================================================================

def sestejStevila(sscs):
    '''vrne vsoto števil v sscs'''
    vsota = 0

    for el in sscs:
        if isinstance(el, list):
            vsota += sestejStevila(el)
        elif isinstance(el, int):
            vsota += el
    return vsota

# =====================================================================@010379=
# 4. podnaloga
# Sestavi funkcijo `jeSSCS(sscs)`, ki preveri
# (vrne True oz. False), če je dan seznam res seznam seznamov celih števil.
# 
# **POZOR**: Python pravi, da je  `isinstance(True, int)` enako `True`, pa tudi
# `isinstance(False, int)` enako `True`, zato se "znebi" napačnih logičnih
# vrednosti z `isinstance(True, bool)`
# =============================================================================

def jeSSCS(sscs):
    '''preveri ali je res sscs'''
    if not isinstance(sscs, list):
        return False
    for el in sscs:
        if isinstance(el, bool):
            return False
        if not (isinstance(el, int) or jeSSCS(el)):
            return False
    return True

# =====================================================================@010380=
# 5. podnaloga
# Sestavi funkcijo `splosci(sscs)`, ki "splošči" seznam
# seznamov celih števil, torej vrne navaden seznam celih števil,
# ki so vsebovana v SSCŠ (v istem vrstnem redu). Za primere od zgoraj so rezultati:
# 
#     [-1, 2, -3]
#     [1, 2, 3, 2, 3, 4]
#     [2, 1, 2, -3, 4]
# =============================================================================

def splosci(sscs):
    '''splošči seznam celih števil v navaden seznam'''
    sez = []
    for el in sscs:
        if isinstance(el, list):
            sez.extend(splosci(el))
        elif isinstance(el, int):
            sez.append(el)

    return sez

