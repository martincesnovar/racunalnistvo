# =============================================================================
# Matrično množenje
#
# Naj bo $A$ matrika velikosti $n \times m$ in naj bo $B$ matrika
# velikosti $p \times r$. Če je $m = p$, potem lahko matriki zmnožimo.
# Matrika $AB$ je velikosti $n \times r$. Da jo dobimo potrebujemo
# $nmr$ množenj. Če je $m \neq p$, matrik $A$ in $B$ ne moremo zmnožiti.
# =====================================================================@010427=
# 1. podnaloga
# Sestavite funkcijo `stevilo_mozenj(izraz, velikost)`, ki kot argumenta
# dobi niz `izraz` in slovar `velikost`. Izraz vsebuje le znake `(` in `)`
# ter velike črke angleške abecede, ki predstavljajo matrike, npr. `((A((BC)D))(EF))`.
# Predpostaviš lahko, da je izraz smiseln in da so v njem zapisani vsi oklepaji,
# tudi če niso potrebni. Slovar `velikost` za vsako matriko vsebuje njene dimenzije
# (ključ je ime matrike, vrednost pa par oblike (število vrstic, število stolpcev)).
# Funkcija naj vrne skupno število množenj, ki jih je potrebno narediti,
# da izračunamo dani matrični izraz. Funkcija naj vrne `None`,
# če množenje ni možno. Zgled:
# 
#     >>> stevilo_mnozenj('((AB)C)', {'A': (10, 5), 'B': (5, 20), 'C': (20, 3)})
#     1600
# =============================================================================


from sklad import Sklad

def stevilo_mnozenj(izraz, velikost):
    '''izraz - niz, velikost - slovar {A:(n,m),B:(p,r)} n==p
    stevilo množenj n*m*r'''
    st_mnozenj = 0
    sklad = Sklad()
    for znak in izraz:
        if znak.isalpha():
            sklad.vstavi((velikost[znak]))
        elif znak == ')':
            p,r = sklad.vrh()
            sklad.odstrani()
            n, m = sklad.vrh()
            sklad.odstrani()
            if p!=m: #dimenzije se ne ujemajo
                return None
            st_mnozenj += r * m * n
            sklad.vstavi((n, r))
    return st_mnozenj

