# =============================================================================
# Branje verig vozlov
#
# Za spodnje naloge morate uvoziti vse definicije iz naloge _Veriga vozlov_.
# To storite z:
# 
#     from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
# =====================================================================@010448=
# 1. podnaloga
# Sestavite funkcijo `dolzina(prvi)`, ki vrne število vozlov v verigi vozlov,
# ki se začne z vozlom `prvi`. Zgled:
# 
#     >>> v = Vozel('sobota')
#     >>> v = dodaj_na_konec(v, 'nedelja')
#     >>> v = dodaj_na_zacetek(v, 'petek')
#     >>> dolzina(v)
#     3
# =============================================================================

def dolzina(prvi):
    '''vrne dolzino'''
    p = prvi
    dolzina = 0
    while p is not None:
        dolzina+=1
        p = p.naslednji
    return dolzina

# =====================================================================@010453=
# 2. podnaloga
# Sestavite funkcijo `zadnji_vozel(prvi)`, ki vrne referenco na
# zadnji vozel v verigi vozlov, ki se začne z vozlom `prvi`. Zgled:
# 
#     >>> v = iz_seznama(['sreda', 'četrtek', 'petek', 'sobota'])
#     >>> zadnji_vozel(v).podatek
#     'sobota'
# =============================================================================

def zadnji_vozel(prvi):
    '''Vrne referenco na zadnji vozel'''
    if prvi is None:
        return None
    p = prvi
    while p.naslednji is not None:
        p = p.naslednji
    x = Vozel(p)
    return x.podatek

# =====================================================================@010450=
# 3. podnaloga
# Sestavite funkcijo `seznam_sodih(prvi)`, ki vrne seznam vseh sodih elementov
# v verigi vozlov, ki se začne z vozlom `prvi`. Predpostavite lahko, da so vsi
# podatki cela števila. Zgled:
# 
#     >>> v = iz_seznama([3, 4, 5, 6, 7, 8, 9, 10, 11])
#     >>> seznam_sodih(v)
#     [4, 6, 8, 10]
# =============================================================================

def seznam_sodih(vozel):
    '''vrne seznam sodih'''
    sez = []
    if vozel is not None:
        p=vozel
        while p is not None:
            st = p.podatek
            p = p.naslednji
            if st%2==0:
                sez.append(st)
    else:
        return []
    return sez

# =====================================================================@010452=
# 4. podnaloga
# Sestavite funkcijo `pogojni_seznam(prvi, pogoj)`, ki kot argument dobil
# verigo vozlov, ki se začne z vozlom `prvi`, ter funkcijo `pogoj`, ki sprejme
# en element in vrne logično vrednost. Funkcija `pogojni_seznam` naj sestavi
# in vrne seznam vseh podatkov, pri katerih funkcija `pogoj` vrne `True`. Zgled:
# 
#     >>> v = iz_seznama(['sreda', 'četrtek', 'petek', 'sobota'])
#     >>> pogojni_seznam(v, lambda s: s.endswith('ek'))
#     ['četrtek', 'petek']
# =============================================================================

def pogojni_seznam(vozel, pogoj):
    '''vrne pogojni seznam'''
    p = vozel
    sez = []
    while p is not None:
        el = p.podatek
        p = p.naslednji
        if pogoj(el):
            sez.append(el)
    return sez

# =====================================================================@010462=
# 5. podnaloga
# Sestavite funkcijo `je_urejen(prvi)`, ki vrne `True`, če so podatki v verigi
# vozlov urejeni naraščajoče in `False`, če niso. Zgled:
# 
#     >>> v = iz_seznama([1, 2, 4, 7, 8])
#     >>> je_urejen(v)
#     True
#     >>> v = iz_seznama([1, 2, 4, 3, 7])
#     >>> je_urejen(v)
#     False
# =============================================================================

def je_urejen(prvi):
    '''Preveri ali je verižni seznam urejen'''
    if prvi is None:
        return True
    if prvi.naslednji is None:
        return True
    if prvi.podatek > prvi.naslednji.podatek:
        return False
    return je_urejen(prvi.naslednji)

