# =============================================================================
# Največje podvsote
#
# Na predavanjih ste že spoznali tri algoritme za izračun največje vsote
# strnjenega podzaporedja v danem seznamu. Pri tej nalogi boste namesto vsote
# izračunali krajišča vseh možnih podzaporedij, pri katerih je ta vsota
# dosežena. Na primer, pri seznamu `[12, 3, 5, -10, -8, 7, 11, -30, 6, 8, -40]`
# dobimo največjo vsoto za podzaporedji `[12, 3, 5]` ter `[12, 3, ..., 7, 11]`.
# V slogu Pythona bomo prvo podzaporedje predstavili s parom `(0, 3)`, saj je
# `[12, 3, 5]` ravno `[12, 3, 5, -10, ..., -40][0:3]`, drugo podzaporedje pa s
# parom `(0, 7)`.
# =====================================================================@011613=
# 1. podnaloga
# Priloženo kodo, ki v kubičnem času izračuna največjo vsoto strnjenega
# podzaporedja v zaporedju `sez`, spremenite, da bo vrnila množico parov vseh
# krajišč podzaporedij, kjer je ta vsota dosežena.
# =============================================================================
def intervali_najvecjih_vsot_kubicna(sez):
    '''vrne množico parov indeksov'''
    opt = 0
    mnozica = set()
    n = len(sez)
    for i in range(n):
        for j in range(i, n):
            s = sez[i]
            for k in range(i + 1, j + 1):
                s = s + sez[k]
            if s>=opt:
                if s > opt:
                    opt = s
                    mnozica.clear() #Spraznemo množico
                mnozica.add((i,j+1))
    return mnozica
# =====================================================================@011614=
# 2. podnaloga
# Priloženo kodo, ki v kvadratnem času izračuna največjo vsoto strnjenega
# podzaporedja v zaporedju `sez`, spremenite, da bo vrnila množico parov vseh
# krajišč podzaporedij, kjer je ta vsota dosežena.
# =============================================================================
def intervali_najvecjih_vsot_kvadratna(sez):
    '''vrne množico parov indeksov'''
    opt = 0
    mnozica = set()
    n = len(sez)
    for i in range(n):
        s = sez[i]
        if s>=opt:
            if s > opt:
                opt = s
                mnozica.clear()
            mnozica.add((i,i+1))
        for j in range(i + 1, n):
            s = s + sez[j]
            if s>=opt:
                if s > opt:
                    opt = s
                    mnozica.clear()
                mnozica.add((i,j+1))
    return mnozica
# =====================================================================@011615=
# 3. podnaloga
# Priloženo kodo, ki v linearnem času izračuna največjo vsoto strnjenega
# podzaporedja v zaporedju `sez`, spremenite, da bo vrnila množico parov vseh
# krajišč podzaporedij, kjer je ta vsota dosežena. Ker je število vseh takih
# parov lahko tudi kvadratno v odvisnosti od zaporedja, pri vsakem možnem
# začetku izberite le najkrajše podzaporedje, kjer je vsota dosežena.
# =============================================================================
def intervali_najvecjih_vsot_linearna(sez):
    '''vrne množico parov indeksov'''
    opt = 0
    mnozica = set()
    n = len(sez)
    s = 0
    k = 0
    mnozica_pregledanih = set()
    for i in range(n):
        t = s + sez[i]
        if t > 0:
            s = t
            if s >= opt:
                if s > opt:
                    mnozica.clear()
                    mnozica_pregledanih.clear()
                    opt = s
                if k not in mnozica_pregledanih:
                    mnozica.add((k, i+1))
                    mnozica_pregledanih.add(k)
        else:
            s = 0
            k=i+1
    return mnozica
