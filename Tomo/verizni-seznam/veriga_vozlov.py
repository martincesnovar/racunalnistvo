# =============================================================================
# Veriga vozlov
#
# Ena najpogostejših predstavitev seznama uporablja verigo vozlov, od katerih
# vsak vsebuje podatek in kaže na morebitni naslednji vozel v verigi.
# Verigo vozlov bomo predstavili s pomočjo razreda `Vozel`:
# 
#     class Vozel:
#         """
#         Osnovni sestavni del verige vozlov.
#         """
#         
#         def __init__(self, podatek, naslednji=None):
#             self.podatek = podatek
#             self.naslednji = naslednji
#         
#         def __str__(self):
#             if self.naslednji is not None:
#                 return '{} -> {}'.format(self.podatek, self.naslednji)
#             else:
#                 return '{} -> X'.format(self.podatek)
# 
# Zadnji vozel v verigi ima za atribut `.naslednji` vrednost `None`. Prav tako
# z `None` predstavimo prazno verigo.
# 
#     >>> v = Vozel(1, Vozel(2, Vozel(3)))
#     >>> print(v)
#     1 -> 2 -> 3 -> X
# =====================================================================@010445=
# 1. podnaloga
# Sestavite funkcijo `vrni_seznam(prvi)`, ki vrne seznam vseh podatkov v verigi
# vozlov, ki se prične z vozlom `prvi`. Ne pozabite na prazno verigo! Zgled:
# 
#     >>> vrni_seznam(Vozel('petek', Vozel('sobota', Vozel('nedelja'))))
#     ['petek', 'sobota', 'nedelja']
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

# =====================================================================@010446=
# 2. podnaloga
# Sestavite funkcijo `dodaj_na_zacetek(prvi, x)`, ki doda nov vozel na
# začetek verige vozlov, ki se začne z vozlom `prvi`, ter vrne referenco na
# novi začetni vozel. Zgled:
# 
#     >>> v = Vozel('nedelja')
#     >>> v = dodaj_na_zacetek(v, 'sobota')
#     >>> v = dodaj_na_zacetek(v, 'petek')
#     >>> vrni_seznam(v)
#     ['petek', 'sobota', 'nedelja']
# =============================================================================

def dodaj_na_zacetek(prvi, x):
    '''doda na zacetek nov element'''
    v = Vozel(x, prvi)
    return v

# =====================================================================@010447=
# 3. podnaloga
# Sestavite funkcijo `dodaj_na_konec(prvi, x)`, ki doda nov vozel na konec
# verige vozlov, ki se začne z vozlom `prvi`, ter vrne referenco na _prvi_
# vozel v verigi. Ne pozabite na primer, ko je veriga prazna! Zgled:
# 
#     >>> v = Vozel('petek')
#     >>> v = dodaj_na_konec(v, 'sobota')
#     >>> v = dodaj_na_konec(v, 'nedelja')
#     >>> vrni_seznam(v)
#     ['petek', 'sobota', 'nedelja']
# =============================================================================

def dodaj_na_konec(prvi, x):
    '''doda na konec nov element'''
    if prvi is None:
        return Vozel(x)
    p = prvi
    while p.naslednji is not None:
        p = p.naslednji
    p.naslednji = Vozel(x)
    return prvi

# =====================================================================@010451=
# 4. podnaloga
# Sestavite funkcijo `iz_seznama(seznam)`, ki sestavi novo verigo, ki kot
# podatke v vozlih zaporedoma vsebuje elemente seznama `seznam`, ter vrne
# referenco na prvi vozel v tej verigi. Zgled:
# 
#     >>> v = iz_seznama(['torek', 'sreda', 'četrtek', 'petek'])
#     >>> v = dodaj_na_konec(v, 'sobota')
#     >>> vrni_seznam(v)
#     ['torek', 'sreda', 'četrtek', 'petek', 'sobota']
# =============================================================================

def iz_seznama(sez):
    '''Vrni verižni seznam, ki bo imel kot podatke elemente seznama sez.'''
    if len(sez) == 0:
        return Vozel()
    prvi = v = Vozel(sez[0])
    for i in range(1,len(sez)):
        v.naslednji = Vozel(sez[i])
        v = v.naslednji
    return prvi

