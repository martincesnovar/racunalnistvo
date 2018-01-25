# =============================================================================
# Sestavljanje verig vozlov
#
# Za spodnje naloge morate uvoziti vse definicije iz naloge _Veriga vozlov_.
# To storite z:
# 
#     from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
# =====================================================================@010449=
# 1. podnaloga
# Sestavite funkcijo `stevilska_veriga(a, b)`, ki vrne referenco na prvi vozel
# v verigi, ki zaporedoma vsebuje števila od `a` do `b`. Predpostavite, da
# velja `a <= b`. Zgled:
# 
#     >>> v = stevilska_veriga(3, 7)
#     >>> v.vrni_seznam()
#     [3, 4, 5, 6, 7]
# =============================================================================

def stevilska_veriga_počasna(a,b):
    '''sestavi stevilsko verigo, ker mora iti nazaj'''
    vozel = Vozel(a)
    for t in range(a,b):
        vozel=dodaj_na_konec(vozel,t+1)
    return vozel

def stevilska_veriga(a,b):
    '''sestavi stevilsko verigo'''
    vozel = None
    for t in range(b, a-1, -1):
        vozel = dodaj_na_zacetek(vozel, t)
    return vozel

# =====================================================================@010461=
# 2. podnaloga
# Sestavite funkcijo `sodi_in_lihi(v)`, ki kot argument prejme referenco na
# vozel ter vrne dve verigi, ki jih dobi tako, da v eno zloži vozle, ki vebujejo
# sode podatke, v drugo pa vozle, ki vsebujejo lihe podatke. Funkcija naj vrne
# par in sicer referenci na začetna vozla v obeh verigah. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])
#     >>> v1, v2 = sodi_in_lihi(v)
#     >>> v1.vrni_seznam()
#     [2, 4, 8]
#     >>> v2.vrni_seznam()
#     [7, 5, 1, 3, 9]
# =============================================================================

def sodi_in_lihi(v):
    if v is None:
        return (None, None)
    sodi, lihi = sodi_in_lihi(v.naslednji)
    if v.podatek % 2 == 0:
        v.naslednji = sodi
        return v, lihi
    else:
        v.naslednji = lihi
        return sodi, v

# =====================================================================@010455=
# 3. podnaloga
# Sestavite funkcijo `podvoji_verigo(prvi)`, ki naj sestavi in
# vrne novo kopijo verige, stare pa naj ne spreminja. Zgled:
# 
#     >>> v = iz_seznama([2, 3, 4, 5])
#     >>> v2 = podvoji_verigo(v)
#     >>> v2.podatek = 11
#     >>> vrni_seznam(v)
#     [2, 3, 4, 5]
#     >>> v2.vrni_seznam(v)
#     [11, 3, 4, 5]
# =============================================================================

class Vozel:
    """
    Osnovni sestavni del verižnega seznama.
    """

    def __init__(self, podatek=None, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

    def __str__(self):
        return str(self.podatek)


def dodaj_na_zacetek(prvi, x):
    '''doda na zacetek nov element'''
    v = Vozel(x, prvi)
    return v

def vrni_seznam(prvi):
    '''Vrne seznam'''
    sez = []
    p = prvi
    if p.podatek is None and p.naslednji is None:
        return []
    while p is not None:
        sez.append(p.podatek)
        p = p.naslednji
    return sez

def iz_seznama(sez):
    '''Vrni verižni seznam, ki bo imel kot podatke elemente seznama sez.'''
    if len(sez) == 0:
        return Vozel()
    prvi = v = Vozel(sez[0])
    for i in range(1, len(sez)):
        v.naslednji = Vozel(sez[i])
        v = v.naslednji
    return prvi

def podvoji_verigo(vozel):
    """ Vrne seznam, v katerem se vsak element seznama prvi pojavi dvakrat zaporedoma. """
    p = vozel
    podvojen = None
    while p is not None:
        if podvojen is None:
            podvojen = Vozel(p.podatek)
            zadnji = podvojen
        else:
            zadnji.naslednji = Vozel(p.podatek)
            zadnji = zadnji.naslednji
        p = p.naslednji
    return podvojen
# =====================================================================@010456=
# 4. podnaloga
# Sestavite funkcijo `stakni_verigi(v1, v2)`, ki kot argumenta prejme referenci
# na dva vozla in sestavi _novo verigo_, ki jo dobi tako, da stakne obe verigi.
# Na primer:
# 
#     >>> v1 = iz_seznama([1, 2, 3])
#     >>> v2 = iz_seznama([4, 5, 6])
#     >>> v = stakni_verigi(v1, v2)
#     >>> v.vrni_seznam()
#     [1, 2, 3, 4, 5, 6]
# =============================================================================
def stakni_verigi(v1, v2):
    '''stakne verige'''
    vozel = podvoji_verigo(v1)
    prvi = vozel
    while prvi.naslednji is not None: #se sprehodimo do konca
        prvi = prvi.naslednji
    prvi.naslednji = podvoji_verigo(v2) #na konec prve verige dodamo kopijo druge verige
    return vozel
# =====================================================================@010458=
# 5. podnaloga
# Sestavite funkcijo `na_zadrgo(v1, v2)`, ki kot argumenta prejme referenci
# na dva vozla. Funkcija naj vrne verigo, ki jo dobi tako, da "na zadrgo"
# združi obe verigi. Funkcija naj vrne referenco na prvi vozel tako dobljene
# verige. Na primer:
# 
#     >>> v1 = iz_seznama([7, 5, 2])
#     >>> v2 = iz_seznama([1, 3, 4, 9, 8])
#     >>> v = na_zadrgo(v1, v2)
#     >>> v.vrni_seznam()
#     [7, 1, 5, 3, 2, 4, 9, 8]
# =============================================================================
def na_zadrgo(v1, v2):
    '''naredi zadrgo iz verig'''
    if v2 is None:
        return v1
    if v1 is None:
        return v2
    vozel = na_zadrgo(v1.naslednji, v2.naslednji)
    v2.naslednji = vozel
    v1.naslednji = v2
    return v1
# =====================================================================@010459=
# 6. podnaloga
# Sestavite funkcijo `odpni_zadrgo(v)`, ki kot argument prejme referenco na
# vozel ter vrne dve verigi, ki jih dobi tako, da "odpne zadrgo", tj. vozle
# naj razdeli med dve verigi. Funkcija naj vrne par in sicer referenci na
# začetna vozla v obeh verigah. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])
#     >>> v1, v2 = odpni_zadrgo(v)
#     >>> v1.vrni_seznam()
#     [7, 2, 3, 9]
#     >>> v2.vrni_seznam()
#     [5, 1, 4, 8]
# =============================================================================
def odpni_zadrgo(v):
    '''iz ene verige zadrge razbije na 2 verige'''
    if v is None:
        return (None, None)
    v_nasl = v.naslednji
    if v_nasl is None:
        return (v, None)
    v1, v2 = odpni_zadrgo(v_nasl.naslednji)
    v_nasl.naslednji = v2
    v.naslednji = v1
    return v, v_nasl

