# =============================================================================
# Levenshteinova razdalja
#
# _Levenshteinova razdalja_ med dvema nizoma je definirana kot najmanjše
# število sprememb, potrebnih da pretvorimo en niz v drugega, pri čemer so
# dovoljene spremembe: vstavljanje, brisanje, ali zamenjava enega znaka.
# =====================================================================@010510=
# 1. podnaloga
# Sestavite funkcijo `razdalja(niz1, niz2)`, ki izračuna Levenshteinovo
# razdaljo med nizoma `niz1` in `niz2`.
# 
#     >>> razdalja("morje", "poletje")
#     4
# =============================================================================
def razdalja(a, b):
    '''Izracuna razdaljo med nizoma'''
    n = len(a)
    m = len(b)

    sez = [(m + 1) * [0] for i in range(n + 1)]
    for i in range(0, n + 1):
        sez[i][0] = i
    for j in range(1, m + 1):
        sez[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            el = sez[i - 1][j - 1]
            if a[i - 1] != b[j - 1]:
                el += 1
            if sez[i][j - 1] + 1 < el:
                el = sez[i][j - 1] + 1
            if sez[i - 1][j] + 1 < el: el = sez[i - 1][j] + 1
            sez[i][j] = el
    return sez[n][m]

# =====================================================================@010511=
# 2. podnaloga
# Sestavite funkcijo `spremembe(niz1, niz2)`, ki vrne seznam sprememb
# (enega izmed možnih), ki jih je potrebno izvesti, da `niz1` pretvorimo
# v `niz2`. Pri tem spremembe zapišemo kot:
# 
# * `('+z', i)`, če na mestu `i` v nizu `niz1` dodamo znak `z`
# * `('-z', i)`, če na mestu `i` v nizu `niz1` pobrišemo znak `z`
# * `('n/z', i)`, če na mestu `i` v nizu `niz1` znak `z` zamenjamo z znakom `n`
# 
# Zgled:
# 
#     >>> spremembe("morje", "poletje")
#     [('p/m', 1), ('l/r', 3), ('+e', 4), ('+t', 5)]
# =============================================================================

def spremembe(a, b):
    '''Vrne spremembe med nizoma'''
    n = len(a)
    m = len(b)
    sez = [(m + 1) * [0] for i in range(n + 1)]
    for i in range(0, n + 1):
        sez[i][0] = i
    for j in range(1, m + 1):
        sez[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            el = sez[i - 1][j - 1]
            if a[i - 1] != b[j - 1]:
                el += 1
            if sez[i][j - 1] + 1 < el:
                el = sez[i][j - 1] + 1
            if sez[i - 1][j] + 1 < el:
                el = sez[i - 1][j] + 1
            sez[i][j] = el

    i = n
    j = m
    s = []
    while i > 0 or j > 0:
        if i > 0 and sez[i][j] > sez[i - 1][j]:
            s.append(('-' + a[i - 1], j + 1))
            i -= 1
        elif j > 0 and sez[i][j] > sez[i][j - 1]:
            s.append(('+' + b[j - 1], j))
            j -= 1
        else:
            if sez[i][j] > sez[i - 1][j - 1]: s.append((b[j - 1] + '/' + a[i - 1], j))
            i -= 1
            j -= 1

    s.reverse()
    return s

