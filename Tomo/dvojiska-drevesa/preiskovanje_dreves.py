# =============================================================================
# Preiskovanje dreves
#
# V vseh spodnjih primerih naj bo `d` dvojiško drevo na spodnji sliki:
# 
#          5
#        /   \
#       3     2
#      /     / \
#     1     6   9
# =====================================================================@010470=
# 1. podnaloga
# Sestavite funkcijo `vsota(drevo)`, ki vrne vsoto vseh števil v
# drevesu `drevo`. Zgled:
# 
#     >>> vsota(d)
#     26
# =============================================================================
from dvojisko_drevo import Drevo

def vsota(drevo):
    '''vrne vsoto elementov drevesa'''
    if not drevo.prazno:
        vsota_levega = vsota(drevo.levo)
        vsota_desnega = vsota(drevo.desno)
        return drevo.podatek + vsota_levega + vsota_desnega
    else:
        return 0

    


# =====================================================================@010471=
# 2. podnaloga
# Dodajte funkcijo `stevilo_listov(drevo)`, ki vrne število listov v
# drevesu `drevo`. Zgled:
# 
#     >>> stevilo_listov(d)
#     3
# =============================================================================

def stevilo_listov(drevo):
    '''vrne število listov'''
    if drevo.prazno: #prazno drevo nima lista
        return 0
    if drevo.levo.prazno and drevo.desno.prazno:
        return 1
    return stevilo_listov(drevo.levo) + stevilo_listov(drevo.desno)



# =====================================================================@010472=
# 3. podnaloga
# Dodajte funkcijo `minimum(drevo)`, ki vrne najmanjše število v drevesu.
# Če je drevo prazno, naj funkcija vrne `None`. Zgled:
# 
#     >>> minimum(d)
#     1
#     >>> minimum(Drevo())
#     None
# =============================================================================

def minimum(drevo):
    '''Vrni najmanjše število v drevesu oziroma None, če je drevo prazno.'''
    if drevo.prazno: 
        return None
    else:
        levi_minimum = minimum(drevo.levo) or float('inf')
        desni_minimum = minimum(drevo.desno) or float('inf')
    return min(drevo.podatek, levi_minimum, desni_minimum)

def minimum_V1(drevo):
    '''Vrne minimalni element v drevesu
    minimum glede na vrednost drevesa'''
    mini = float('inf')
    if drevo.prazno:
        return None
    min_levi = minimum_V1(drevo.levo)
    min_desni = minimum_V1(drevo.desno)
    if min_levi is not None:
        mini = min(mini, min_levi, drevo.podatek)
    if min_desni is not None:
        mini = min(mini, min_desni,drevo.podatek)
    if min_desni is None and min_levi is None:
        return drevo.podatek
    if min_desni is not None and min_levi is not None:
        mini = min(mini, min_levi, min_desni, drevo.podatek)
    return mini

# =====================================================================@011189=
# 4. podnaloga
# Dodajte funkcijo `premer(drevo)`, ki vrne premer drevesa, torej dolžino
# najdaljše poti med katerima koli dvema vozliščema v drevesu. Zgled:
# 
#     >>> premer(Drevo('x', levo=Drevo('y'), desno=Drevo('z')))
#     2  # najdaljša pot je y-x-z
#     >>> premer(Drevo('x', levo=Drevo('y', levo=Drevo('z'), desno=Drevo('w'))))
#     2  # najdaljša pot je y-z-w
#     >>> premer(Drevo('x', levo=Drevo('y'), desno=Drevo('z', levo=Drevo('w'))))
#     3  # najdaljša pot je y-x-z-w
#     >>> premer(Drevo())
#     -inf  # v drevesu ni vozlišč
#     >>> premer(Drevo('x'))
#     0  # v drevesu je le eno vozlišče
# =============================================================================

def premer_visina(drevo):
    '''vrne premer in višino drevesa'''
    if drevo.prazno:
        return float('-inf'), 0
    else:
        premer_l, visina_l = premer_visina(drevo.levo)
        premer_d, visina_d = premer_visina(drevo.desno)
        visina = 1 + max(visina_l, visina_d)
        najdalsa_pot = visina_l + visina_d
        najdaljsa_pot_mimo = max(premer_l, premer_d)
        premer = max(najdalsa_pot, najdaljsa_pot_mimo)
        return premer, visina
    
def premer(drevo):
    '''vrne premer'''
    return premer_visina(drevo)[0]


def visina(drevo):
    '''vrne visino drevesa'''
    if drevo.prazno:
        return 0
        
    return 1 + max(visina(drevo.levo), visina(drevo.desno))

def premer_1(drevo):
    '''vrne dolzino najdaljse poti v drevsu
    ni učinkovita, ker vedno računamo višino'''
    if drevo.prazno:
        return float('-inf')
    visina_levega = visina(drevo.levo)
    visina_desnega = visina(drevo.desno)

    levi_premer = premer(drevo.levo)
    desni_premer = premer(drevo.desno)

    return max(visina_levega + visina_desnega, max(levi_premer, desni_premer))

