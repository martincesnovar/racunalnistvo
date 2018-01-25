# =============================================================================
# Nadomestni upor
#
# Kot je dobro znano iz elektrotehnike, nadomestni upor dveh zaporedno
# vezanih upornikov izračunamo po formuli $R = R_1 + R_2$, nadomestni
# upor dveh vzporedno vezanih upornikov pa je $1/R = 1/R_1 + 1/R_2$.
# =====================================================================@010420=
# 1. podnaloga
# Napišite funkcijo `nadomestni_upor(r1, r2, tipV)`, ki kot argumenta dobi
# dve števili `r1` in `r2` (tj. upor obeh upornikov) in tip vezave `tipV`,
# ki je bodisi znak `'V'` bodisi znak `'Z'`. Funkcija naj vrne nadomestni
# upor vezja.
# Pozor: nekateri uporniki so vezani kratkostično in imajo upor 0.
# (Upor dveh vzporedno vezanih upornikov, od katerih ima vsaj en upor 0, je 0.)
# 
#     >>> nadomestni_upor(3, 5, 'Z')
#     8
#     >>> nadomestni_upor(3, 0, 'V')
#     0
#     >>> nadomestni_upor(2, 5, 'V')
#     1.875
# =============================================================================
from sklad import Sklad

def nadomestni_upor(r1, r2, tipV):
    '''izračuna nadomestni upor'''
    if tipV == 'Z':
        return r1+r2
    elif tipV == 'V':
        if not(r1 and r2): #vsaj eden 0
            return 0
        else:
            r = 1/r1 + 1/r2
            return 1/r


# =====================================================================@010421=
# 2. podnaloga
# Sestavite funkcijo `upor_vezja(niz)`, ki izračuna nadomestni upor vezja.
# Vezje je podano kot niz v "RPN notaciji": operandom (tj. vrednosti uporov)
# sledi operator (tj. način vezave, `'V'` ali `'Z'`).
# 
# Analizirajmo vezje `'3 5 Z 0 V 3 2 Z V'`: 
# Niz `'3 5 Z'` tako pomeni, da sta zaporedno vezana upornika z upornostma
# 3 in 5 (ki ju lahko nadomestimo z enim upornikom z upornostjo 8). Skratka,
# dobimo vezje `'8 0 V 3 2 Z V'`.
# V tem novem vezju niz `'8 0 V'` pomeni, da sta vzporedno vezana upornika z
# upornostma 8 in 0. Vzporedna vezava, ki vsebuje kratkostični upornik, je
# kratkostična, zato je 0 nadomestni upor vezja `'8 0 V'`. Skratka, dobimo
# vezje `'0 3 2 Z V'`.
# Niz `'3 2 Z'` pomeni, da sta zaporedno vezana upornika z upornostma 3 in 2
# (in torej z nadomestno upornostjo 5). Če upoštevamo še to, potem dobimo
# vezje `'0 5 V'`, kar na koncu da rezultat 0.
# 
#     >>> upor_vezja('3 5 Z 0 V 3 2 Z V')
#     0
# 
# Predpostavite lahko, da v nizu `niz` nastopajo (poleg znakov `'V'`, `'Z'`
# in `' '`) le nenegativna cela števila.
# =============================================================================

def upor_vezja(niz):
    '''Vrne nadomestni upor'''
    sklad_uporov = Sklad()
    sez = niz.strip().split(' ')
    for el in sez:
        if el not in {'V','Z'}:
            sklad_uporov.vstavi(int(el))
        else:
            r1 = sklad_uporov.vrh()
            sklad_uporov.odstrani()
            r2 = sklad_uporov.vrh()
            sklad_uporov.odstrani()
            rez = nadomestni_upor(r1, r2, el)
            sklad_uporov.vstavi(rez)
    return sklad_uporov.vrh()

# =====================================================================@010422=
# 3. podnaloga
# Napišite še funkcijo `sestavi_racun(niz)`, ki namesto da izračuna
# nadomestni upor vezja sestavi račun, ki ga je potrebno izračunati,
# da dobimo nadomestni upor vezja.
# 
#     >>> sestavi_racun('3 5 Z 0 V 3 2 Z V')
#     '(1/(1/(3 + 5) + 1/0)^-1 + 1/(3 + 2))^-1'
# 
# _Namig_: Ali lahko nalogo rešite tako, da malenkost predelate rešitev
# prejšnje naloge?
# =============================================================================

def nadomestni_formula(r1, r2, tip):
    '''Sestavi pravilno formulo glede na tip'''
    if tip == 'Z':
        return '({0} + {1})'.format(r2, r1)
    if tip == 'V':
        if r1== 0 or r2 == 0:
            return 0
        return '(1/{0} + 1/{1})^-1'.format(r2,r1)

def sestavi_racun(niz):
    '''Vrne račun'''
    sklad = Sklad()
    tab = niz.strip().split(' ')
    for el in tab:
        if el in {'V','Z'}:
            r1 = sklad.vrh()
            sklad.odstrani()
            r2 = sklad.vrh()
            sklad.odstrani()
            upor = nadomestni_formula(r1, r2, el)
            sklad.vstavi(upor)
        else:
            sklad.vstavi(el)
    return sklad.vrh()

# =====================================================================@010423=
# 4. podnaloga
# Stari električarski mački si račun poenostavijo na sledeč način: če je
# upor $R_a$ več kot 10-krat večji kot upor $R_b$, potem za nadomestni
# upor zaporedne vezave upornikov $R_a$ in $R_b$ vzamejo kar $R_a$, kot
# nadomestni upor vzporedne vezave pa kar upor $R_b$. Seveda pa pravilno
# razumejo vezavo, če je kakšen upor enak 0.
# 
# Sestavite funkcijo `stari_macki(niz)`, ki bo nadomestni upor vezja
# izračunala po "metodi starih mačkov".
# 
#     >>> stari_macki('2 30 Z 20 V 3 2 Z V')
#     3.5294117647058822
# =============================================================================

def nadomestni_macki_formula(r1, r2, tip):
    '''izračuna upore po metodi starih mačkov'''
    if r1 < r2:
        r2, r1 = r1, r2
    if tip == 'Z':
        if r1 > 10*r2:
            return r1
        else:
            return r1+r2
    elif tip == 'V':
        if r2==0:
            return 0
        if r1 > 10*r2:
            return r2
        else:
            return 1 / (1/r1 + 1/r2)


def stari_macki(niz):
    '''vrne upor po metodi starih mačkov'''
    sklad = Sklad()
    tab = niz.strip().split(' ')
    for el in tab:
        if el in {'V','Z'}:
            r1 = sklad.vrh()
            sklad.odstrani()
            r2 = sklad.vrh()
            sklad.odstrani()
            sklad.vstavi(nadomestni_macki_formula(r1, r2, el))
        else:
            sklad.vstavi(int(el))
    return sklad.vrh()

