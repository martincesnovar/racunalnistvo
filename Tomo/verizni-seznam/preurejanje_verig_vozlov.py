# =============================================================================
# Preurejanje verig vozlov
#
# Za spodnje naloge morate uvoziti vse definicije iz naloge _Veriga vozlov_.
# To storite z:
# 
#     from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
# =====================================================================@010464=
# 1. podnaloga
# Sestavite funkcijo `preuredi_parnost(v)`, ki kot argument prejme referenco na
# vozel ter verigo vozlov tako preuredi, da postavi vse vozle, ki vsebujejo lih
# podatek na začetek, vozle, ki vsebujejo sod podatek pa na konec. Funkcija naj
# vrne referenco na začetek preurejene verige. Na primer:
# 
#     >>> v = iz_seznama([7, 5, 2, 1, 3, 4, 9, 8])
#     >>> v = preuredi_parnost(v)
#     >>> v.vrni_seznam()
#     [7, 5, 1, 3, 9, 2, 4, 8]
# =============================================================================

def pridruzi(v1,v2):
    '''priduzi verigo'''
    p = v1
    while p.naslednji is not None:
        p = p.naslednji
    p.naslednji = v2
    return v1

def preuredi_parnost(v):
    '''lihe postavi pred sode'''
    sodi, lihi = sodi_in_lihi(v)
    return pridruzi(lihi,sodi)

# =====================================================================@010465=
# 2. podnaloga
# Pepi je sestavil verigo vozlov in ugotovil, da je elemente nizal v seznam
# v napačnem vrstnem redu. Zdaj je treba seznam obrniti, tako da obstoječih
# vozlov ne brišemo in ne dodajamo novih. Sestavite funkcijo `obrni_na_mestu(v)`,
# ki dobi verigo vozlov in jo obrne na mestu. Funkcijo mora vrniti referenco
# na prvi vozel. Zgled:
# 
#     >>> v = iz_seznama([7, 5, 2, 1])
#     >>> v = obrni_na_mestu(v)
#     >>> v.vrni_seznam()
#     [1, 2, 5, 7]
# =============================================================================

def obrni_na_mestu(v):
    '''obrne verižni seznam na mestu'''
    predhodni = None
    while v is not None:
        naslednji = v.naslednji
        v.naslednji = predhodni
        predhodni = v
        v = naslednji
    return predhodni
# =====================================================================@010466=
# 3. podnaloga
# Napišite funkcijo `uredi_z_izbiranjem(v)`, ki verigo vozlov uredi z izbiranjem.
# Funkcija naj deluje tako, da najprej ustvari novo prazno verigo. V seznamu
# `v` naj poišče največji element ter ga prestavi na začetek nove verige. To naj
# ponavlja, doker v seznamu `v` ne zmanjka elementov. Funkcija naj vrne referenco
# na prvi vozel v urejeni verigi. Zgled:
# 
#     >>> v = iz_seznama([4, 7, 3, 6, 5, 2, 1])
#     >>> v = uredi_z_izbiranjem(v)
#     >>> vrni_seznam(v)
#     [1, 2, 3, 4, 5, 6, 7]
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

def iz_seznama(sez):
    '''Vrni verižni seznam, ki bo imel kot podatke elemente seznama sez.'''
    if len(sez) == 0:
        return Vozel()
    prvi = v = Vozel(sez[0])
    for i in range(1,len(sez)):
        v.naslednji = Vozel(sez[i])
        v = v.naslednji
    return prvi

def uredi_z_izbiranjem(v):
    '''Uredi verižni seznam z izbiranjem'''
    vozel = None
    while v is not None:
        p = v
        naj = p.podatek
        vozel_pred_p = None
        pred = None #Vozel pred največjim
        while p is not None:
            if p.podatek > naj:
                naj = p.podatek
                pred = vozel_pred_p
            vozel_pred_p = p
            p = p.naslednji
        if pred is None:
            p = v
            v = p.naslednji
        else:
            p = pred.naslednji
            pred.naslednji = p.naslednji
        p.naslednji = vozel
        vozel = p
    return vozel

