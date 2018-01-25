# =============================================================================
# Množice z iskalnimi drevesi
#
# Podatkovno strukturo množica lahko učinkovito predstavimo z iskalnim drevesom.
# V tej nalogi bomo najprej definirali nekaj pomožnih funkcij na drevesih, nato
# pa definirali razred `Mnozica`, ki podpira osnovne operacije na množicah.
# =====================================================================@011421=
# 1. podnaloga
# Sestavite funkcijo `vstavi_v_iskalno_drevo(drevo, x)`, ki v iskalno drevo na
# pravo mesto vstavi element `x` ter vrne novo drevo. Če je `x` enak podatku
# v korenu drevesa, naj funkcija vrne prvotno drevo.
# =============================================================================
from dvojisko_drevo import Drevo

def vstavi_v_iskalno_drevo(drevo, x):
    '''vstavi element v iskalno dvojiško drevo, drevo je še vedno iskalno'''
    if drevo.prazno:
        return Drevo(x)
    pod = drevo.podatek
    if x < pod:
        return Drevo(pod, levo = vstavi_v_iskalno_drevo(drevo.levo,x), desno = drevo.desno)
    elif x > pod:
        return Drevo(pod, levo = drevo.levo, desno = vstavi_v_iskalno_drevo(drevo.desno,x))
    else: #sta enaka
        return drevo

# =====================================================================@011422=
# 2. podnaloga
# Sestavite funkcijo `ali_vsebuje(drevo, x)`, ki vrne `True`, če dano iskalno
# drevo vsebuje podatek `x`, in `False`, če ga ne.
# =============================================================================


def ali_vsebuje(drevo,x):
    '''vrne True, če drevo vsebuje x'''
    if drevo.prazno:
        return False
    elif drevo.podatek == x:
        return True
    elif drevo.podatek > x:
        return ali_vsebuje(drevo.levo,x)
    elif drevo.podatek < x:
        return ali_vsebuje(drevo.desno,x)
    

# =====================================================================@011423=
# 3. podnaloga
# Z razredom `Mnozica` bomo predstavili nespremenljive množice, torej take, ki
# ne podpirajo metod za dodajanje in odstranjevanje elementov, le metode, ki
# izračunajo nove množice iz obstoječih. Vsako množico bomo predstavili z
# objektom, ki ima dva atributa: iskalnim drevesom elementov `_elementi` ter
# velikostjo `_velikost`.
# 
# Sestavite razred `Mnozica` z metodo `__init__`, ki mu za neobvezen prvi
# argument lahko podamo iterator začetnih elementov množice.
# =============================================================================

def vmesni_pregled(d):
    '''vmesni pregled dreves'''
    if not d.prazno:
        for levi in vmesni_pregled(d.levo):
            yield levi
        yield d.podatek
        for desni in vmesni_pregled(d.desno):
            yield desni


class Mnozica:
    def __init__(self, *args):
        self._elementi = Drevo()
        self._velikost = 0
        if args:
            for element in args[0]:
                if not ali_vsebuje(self._elementi, element):
                    self._elementi = vstavi_v_iskalno_drevo(self._elementi, element)
                    self._velikost += 1
        

# =====================================================================@011424=
# 4. podnaloga
# Dodajte metodo `__iter__`, ki vrne iterator, ki našteva elemente množice od
# najmanjšega do največjega.
# =============================================================================

    def __iter__(self):
        '''našteva elemente množice'''
        return vmesni_pregled(self._elementi)

# =====================================================================@011425=
# 5. podnaloga
# Za lepši prikaz dodajte še metodo `__str__`, ki vrne niz oblike
# `{el1, el2, ...}`, kjer so elementi množice našteti od najmanjšega do
# največjega.
# =============================================================================

    def __repr__(self):
        return '{{{}}}'.format(', '.join(repr(element) for element in self))

    def __str__(self):
        return '{{{}}}'.format(', '.join(repr(element) for element in self))


# =====================================================================@011426=
# 6. podnaloga
# Za dostop do velikosti množice `mn` in iskanja elementov v njej bi sicer lahko
# napisali metodi `mn.velikost()` in `mn.vsebuje(x)`, vendar je bolj Pythonovsko,
# da definiramo metodi `__len__` in `__contains__`, da lahko pišemo kar `len(mn)`
# in `x in mn` oz. `x not in mn`. Definirajte ju.
# =============================================================================

    def __len__(self):
        return self._velikost

    def __contains__(self, x):
        return ali_vsebuje(self._elementi, x)

# =====================================================================@011427=
# 7. podnaloga
# Definirajte še metodi `__or__` in `__and__`, ki sprejmeta dve množici ter
# vrneta njuno unijo in presek. Stvari naredite učinkovite tako, da upoštevate
# velikost množic.
# =============================================================================

    def __or__(self, other):
        if len(self) > len(other):
            return other | self
        unija = Mnozica()
        unija._velikost = other._velikost
        unija._elementi = other._elementi
        for element in self:
            if element not in unija:
                unija._elementi = vstavi_v_iskalno_drevo(unija._elementi, element)
                unija._velikost += 1
        return unija

    def __and__(self, other):
        if len(self) > len(other):
            return other & self
        presek = Mnozica()
        for element in self:
            if element in other:
                presek._elementi = vstavi_v_iskalno_drevo(presek._elementi, element)
                presek._velikost +=1
        return presek
    

# =====================================================================@011428=
# 8. podnaloga
# Kaj bi se zgodilo, če bi sestavili množico z `Mnozica(range(1000000))`? Ali
# bi bila taka podatkovna struktura učinkovita? Na vajah se bomo pogovorili o
# tem, kako lahko izboljšamo učinkovitost s tem, da uporabimo uravnotežena
# dvojiška drevesa.
# =============================================================================

'''Ne ni učinkovito - moramo narediti avl drevo
rotacije,...'''

