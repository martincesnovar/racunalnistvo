# =============================================================================
# Množenje matrik
#
# Izračunati želimo produkt $n$ matrik $A_1 \times A_2 \times \ldots \times A_n$.
# Dimenzije posameznih matrik so ustrezne, tako da je produkt možno izračunati.
# Zaradi asociativnosti množenja lahko matrike množimo na več različnih načinov,
# (tj. v izraz na različne načine postavimo oklepaje). Zanima nas, v kakšnem
# vrstnem redu moramo množiti, da bomo opravili kar se da malo množenj realnih števil.
# =====================================================================@010517=
# 1. podnaloga
# Sestavi funkcijo `stevilo_mnozenj(dim)`, ki izračuna najmanjše število množenj
# realnih števil, ki jih potrebujemo, da zmnožimo matrike danih velikosti.
# Velikosti matrik so podane s seznamom `dim`, katerega elementi so pari,
# ki določajo, koliko vrstic in koliko stolpcev ima posamezna matrika.
# 
#     >>> stevilo_mnozenj([(30, 35), (35, 15), (15, 10), (10, 5), (5, 10)])
#     10125
# =============================================================================
from functools import lru_cache
@lru_cache(maxsize=None)
def stevilo_mnozenj_dim(dim):
    if len(dim) == 1:
        return 0, dim[0]
    else:
        sez = []
        for k in range(1, len(dim)):
             st_mn_l, (vrs_l, sto_l) = stevilo_mnozenj_dim(dim[:k])
             st_mn_d, (vrs_d, sto_d) = stevilo_mnozenj_dim(dim[k:])
             sez.append(( st_mn_l + st_mn_d + vrs_l * sto_l * sto_d, (vrs_l, sto_d)))
        return min(sez)

from functools import lru_cache
@lru_cache(maxsize=None)
def stevilo_naj_mnozenj_dim(dim):
    if len(dim) == 1:
        return 0, dim[0]
    else:
        sez = []
        for k in range(1, len(dim)):
             st_mn_l, (vrs_l, sto_l) = stevilo_naj_mnozenj_dim(dim[:k])
             st_mn_d, (vrs_d, sto_d) = stevilo_naj_mnozenj_dim(dim[k:])
             sez.append(( st_mn_l + st_mn_d + vrs_l * sto_l * sto_d, (vrs_l, sto_d)))
        return max(sez)

from functools import lru_cache
@lru_cache(maxsize=None)
def stevilo_mnozenj_dim_v(dim):
    if len(dim) == 1:
        return 0, dim[0]
    else:
        sez = []
        for k in range(1, len(dim)):
             st_mn_l, (vrs_l, sto_l) = stevilo_mnozenj_dim_v(dim[:k])
             st_mn_d, (vrs_d, sto_d) = stevilo_mnozenj_dim_v(dim[k:])
             sez.append(( st_mn_l + st_mn_d + vrs_l * sto_l * sto_d, (vrs_l, sto_d)))
        return sum(sez[0])
        

def stevilo_mnozenj(dim):
    '''vrne najmanjše število množenj'''
    return stevilo_mnozenj_dim(tuple(dim))[0]

def stevilo_mnozenj_naj(dim):
    '''vrne najmanjše število množenj'''
    return stevilo_naj_mnozenj_dim(tuple(dim))[0]

def stevilo_mnozenj_v(dim):
    '''vrne najmanjše število množenj'''
    return stevilo_mnozenj_dim_v(tuple(dim))[0]


        

# =====================================================================@010518=
# 2. podnaloga
# Sestavi funkcijo `vrstni_red(dim)`, ki izračuna vrstni red množenj matrik,
# pri katerem bomo potrebovali najmanj množenj realnih števil.
# 
#     >>> vrstni_red([(30, 35), (35, 15), (15, 10), (10, 5), (5, 10)])
#     '((A1(A2(A3A4)))A5)'
# =============================================================================

@lru_cache(maxsize=None)
def stevilo_mnozenj_1(dim,i):
    if len(dim) == 1:
        return 0, 'A{}'.format(i), dim[0]
    else:
        sez = []
        for k in range(1, len(dim)):
             st_mn_l, vrsta_l, (vrs_l, sto_l) = stevilo_mnozenj_1(dim[:k], i)
             st_mn_d, vrsta_d, (vrs_d, sto_d) = stevilo_mnozenj_1(dim[k:], i + k)
             sez.append(( st_mn_l + st_mn_d + vrs_l * sto_l * sto_d, '({}{})'.format(vrsta_l, vrsta_d), (vrs_l, sto_d) ))
        return min(sez)

def vrstni_red(dim):
    return stevilo_mnozenj_1(tuple(dim),1)[1]

