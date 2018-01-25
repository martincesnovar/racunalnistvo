# =============================================================================
# Spreminjanje verig vozlov
#
# Za spodnje naloge morate uvoziti vse definicije iz naloge _Veriga vozlov_.
# To storite z:
# 
#     from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
# =====================================================================@010454=
# 1. podnaloga
# Sestavite funkcijo `vstavi_na_mesto(prvi, n, x)`, ki na `n`-to mesto v verigi
# vozlov, ki se začne z vozlom `prvi`, vstavi vozel s podatkom `x`. Funkcija
# naj vrne referenco na prvi vozel v spremenjeni verigi vozlov. Če veriga vozlov
# ni dovolj dolga, dodajte ustrezno število vozlov, ki imajo kot podatek `None`.
# Zgled:
# 
#     >>> v = iz_seznama(['sreda', 'četrtek', 'sobota'])
#     >>> v = vstavi_na_mesto(v, 2, 'petek')
#     >>> vrni_seznam(v)
#     ['sreda', 'četrtek', 'petek', 'sobota']
# =============================================================================

def vstavi_na_mesto(prvi, n, x):
    '''Vstavi na n-to mesto podatek'''
    if n==0:
        return Vozel(x, prvi)
    p = prvi
    while n-1 > 0:
        if p.naslednji is None:
            p.naslednji = Vozel()
        p = p.naslednji
        n-=1
    p.naslednji = Vozel(x, p.naslednji)
    return prvi
# =====================================================================@010463=
# 2. podnaloga
# Sestavite funkcijo `vstavi_v_urejenega(prvi, x)`, ki podatek `x`
# vstavi na primerno mesto v urejeno verigo vozlov, ki se začne z vozlom `prvi`.
# Funkcija naj vrne začetni vozel spremenjene verige. Zgled:
# 
#     >>> v = iz_seznama([1, 2, 4, 7, 8])
#     >>> v = vstavi_v_urejenega(v, 3)
#     >>> vrni_seznam(v)
#     [1, 2, 3, 4, 7, 8]
# =============================================================================

def vstavi_v_urejenega(prvi, x):
    '''Vstavi element x v urejen verižni seznam'''
    if prvi is None:
        return Vozel(x)
    if x<=prvi.podatek:
        return Vozel(x, prvi)
    if prvi.naslednji is None:
        prvi.naslednji = Vozel(x)
    else:
        prvi.naslednji = vstavi_v_urejenega(prvi.naslednji, x)
    return prvi

# =====================================================================@010460=
# 3. podnaloga
# Sestavite funkcijo `odstrani(v, x)`, ki kot argumenta prejme referenco na
# vozel ter element `x`. Funkcija naj verigo popravi, tako da odstrani vozle,
# ki kot podatek vsebujejo element `x`. Funkcija naj vrne referenco na
# začetni vozel verige. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2, 5, 3, 5])
#     >>> v = odstrani(v, 5)
#     >>> v.vrni_seznam()
#     [7, 2, 3]
# =============================================================================

def odstrani(v,x):
    '''odstrani element x iz vozla'''
    if v is None:
        return None
    if x != v.podatek:
        v.naslednji = odstrani(v.naslednji,x)
        return v
    return odstrani(v.naslednji, x)


# =====================================================================@010457=
# 4. podnaloga
# Sestavite funkcijo `multipliciraj_verigo(v, n)`, ki kot argumenta prejme
# referenco na vozel in naravno število `n` ter verigo spremeni tako, da
# iz vsakega vozla naredi `n` zaporednih kopij. Funkcija naj vrne referenco
# na prvi vozel. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2])
#     >>> v = multipliciraj_verigo(v, 3)
#     >>> v.vrni_seznam()
#     [7, 7, 7, 5, 5, 5, 2, 2, 2]
# =============================================================================

def multipliciraj_verigo(v,n):
    '''naredi n zaporednih kopij vozla'''
    if v is None:
        return None
    prvi=v
    while prvi is not None:
        i = 0
        while i < n-1: #do enega manj
            prvi.naslednji = Vozel(prvi.podatek, prvi.naslednji)
            prvi = prvi.naslednji
            i+=1
        prvi = prvi.naslednji
    return v

