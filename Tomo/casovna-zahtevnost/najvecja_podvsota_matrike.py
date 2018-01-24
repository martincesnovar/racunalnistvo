# =============================================================================
# Največja podvsota matrike
# =====================================================================@011785=
# 1. podnaloga
# Sestavite funkcijo `matrika_delnih_vsot(matrika)`, ki vrne matriko delnih
# vsot, v kateri je na vsakem mestu vsota vseh elementov v bloku levo zgoraj od
# danega mesta. Na primer, če je `matrika` enaka
# 
#      1  2 -1
#     -5  4  6
#      2  0  1
# 
# mora funkcija vrniti matriko
# 
#      1  3  2
#     -4  2  7
#     -2  4  10
# 
# Če želite uspešno rešiti zadnji del naloge, mora funkcija delovati v
# linearnem času (v odvisnosti od velikosti matrike).
# =============================================================================

def matrika_delnih_vsot(matrika):
    '''vrne matriko delnih vsot'''
    vsote = [vrs[:] for vrs in matrika]
    for i, vrs in enumerate(matrika):
        for j in range(len(vrs)):
            if j > 0:
                vsote[i][j] += vsote[i][j - 1]
            if i > 0:
                vsote[i][j] += vsote[i - 1][j]
            if i > 0 and j > 0:
                vsote[i][j] -= vsote[i - 1][j - 1]
    return vsote

# =====================================================================@011786=
# 2. podnaloga
# Sestavite funkcijo `vsota_podmatrike(delne_vsote, i1, j1, i2, j2)`, ki iz
# matrike delnih vsot, kot jo izračuna prejšnja funkcija, v konstantnem času
# izračuna vsoto vseh elementov med vrsticami `i1` (vključno) in `i2` (brez) ter
# stolpci `j1` (vključno) in `j2` (brez).
# 
# Natančneje, če velja `delne_vsote = matrika_delnih_vsot(matrika)`, potem velja
# 
#     vsota_podmatrike(delne_vsote, i1, j1, i2, j2)
#     = sum(vrstica[j1:j2] for vrstica in matrika[i1:i2])
# =============================================================================

def vsota_podmatrike(delne_vsote, i1, j1, i2, j2):
    '''vrne vsoto podmatrike'''
    if i2 == 0 or j2 == 0:
        return 0
    vs = delne_vsote[i2 - 1][j2 - 1]
    if j1 > 0:
        vs -= delne_vsote[i2 - 1][j1 - 1]
    if i1 > 0:
        vs -= delne_vsote[i1 - 1][j2 - 1]
    if i1 > 0 and j1 > 0:
        vs += delne_vsote[i1 - 1][j1 - 1]
    return vs

# =====================================================================@011787=
# 3. podnaloga
# Nadaljevanje sledi…
# =============================================================================

