# =============================================================================
# Verižni seznam
#
# Verižni seznam predstavimo z verigo vozlov ter kazalcema, ki kažeta na
# začetni in končni vozel v tej verigi. Za osnovo si bomo vzeli razred `Vozel`,
# kot ga poznamo že od prej:
# 
#     class Vozel:
#         '''
#         Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
#         '''
#         def __init__(self, podatek, naslednji=None):
#             self.podatek = podatek
#             self.naslednji = naslednji
# 
# ter razred `VerizniSeznam`:
# 
#     class VerizniSeznam:
#         '''
#         Razred, ki predstavlja verižni seznam z začetkom in koncem.
#         '''
#         def __init__(self):
#             self._zacetek = None
#             self._konec = None
#    
#         def __str__(self):
#             niz = ''
#             vozel = self._zacetek
#             while vozel is not None:
#                 niz += '{} -> '.format(repr(vozel.podatek))
#                 vozel = vozel.naslednji
#             return niz + '•'
# 
# Pozorni bodite, da se imeni atributov, v katerih sta shranjena kazalca na
# začetek in konec verige vozlov, začneta s podčrtajem, s čimer želimo povedati,
# da naj uporabnik podatkovne strukture do njih ne dostopa direktno. V ta namen
# bomo raje malo kasneje definirali metodi `zacetek` in `konec`.
# =====================================================================@011065=
# 1. podnaloga
# Dopolnite obstoječi razred `VerizniSeznam` tako, da dopišete še
# metodo `vstavi_na_zacetek(self, podatek)`, ki `podatek` vstavi na
# začetek seznama (pazite pri vstavljanju v prazen seznam).
# =============================================================================
class Vozel:
    '''
    Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
    '''
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

class VerizniSeznam:
    '''
    Razred, ki predstavlja verižni seznam z začetkom in koncem.
    '''
    def __init__(self):
        self._zacetek = None
        self._konec = None

    def __str__(self):
        niz = ''
        vozel = self._zacetek
        while vozel is not None:
            niz += '{} -> '.format(repr(vozel.podatek))
            vozel = vozel.naslednji
        return niz + '•'

    def vstavi_na_zacetek(self, podatek):
        '''vstavi podatek na zacetek'''
        if self._zacetek is None and self._konec is None: # če je prazen
            self._zacetek = Vozel(podatek)
            self._konec = Vozel(podatek)
        else:
            self._zacetek = Vozel(podatek, self._zacetek)
            
        
# =====================================================================@011066=
# 2. podnaloga
# Dopišite še metodo `zacetek(self)`, ki vrne podatek na začetku
# verižnega seznama. Če je seznam prazen, naj metoda sproži izjemo
# `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def zacetek(self):
        '''vrne podatek na začetku'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        return self._zacetek.podatek

# =====================================================================@011067=
# 3. podnaloga
# Dodajte še metodo `izbrisi_zacetek(self)`, ki izbriše element na začetku
# verižnega seznama (pazite na seznam dolžine 1). Če je seznam prazen, naj
# metoda sproži izjemo `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def izbrisi_zacetek(self):
        '''izbriše začetek'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        if self._zacetek == self._konec: #če je le 1 element ga odstranimo
            self._zacetek = self._konec = None
        self._zacetek = self._zacetek.naslednji

# =====================================================================@011068=
# 4. podnaloga
# Razred `VerizniSeznam` naj sedaj pozna še metodo
# `vstavi_na_konec(self, podatek)`, ki `podatek` vstavi na
# konec seznama (pazite pri vstavljanju v prazen seznam).
# =============================================================================

    def vstavi_na_konec(self, podatek):
        '''Vstavi na konec'''
        if self._konec: # če ni prazen
            self._konec.naslednji = Vozel(podatek)
            self._konec = self._konec.naslednji
        else:
            self._zacetek = self._konec = Vozel(podatek)

        

# =====================================================================@011069=
# 5. podnaloga
# Dopišite še metodo `konec(self)`, ki vrne podatek na koncu
# verižnega seznama. Če je seznam prazen, naj metoda sproži izjemo
# `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def konec(self):
        '''vrne konec'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        return self._konec.podatek

# =====================================================================@011070=
# 6. podnaloga
# Sestavite metodo `izbrisi_konec(self)`, ki izbriše element na koncu
# verižnega seznama (pazite na seznam dolžine 1). Če je seznam prazen, naj
# metoda sproži izjemo `IndexError('Verižni seznam je prazen')`.
# =============================================================================

    def izbrisi_konec_N(self):
        '''izbriše konec'''
        if self._zacetek is None and self._konec is None:
            raise IndexError('Verižni seznam je prazen')
        elif self._zacetek == self._konec: #če je le 1 element ga odstranimo
            self._zacetek = self._konec = None
        else:
            if self._zacetek.naslednji:
                prvi = self._zacetek
                while prvi.naslednji.naslednji is not None:
                    prvi = prvi.naslednji #smo na novem zadnjem
                self._konec = prvi
                prvi.naslenji = None
                self._konec = prvi
                self._konec.naslednji = None
    def izbrisi_konec(self):
        '''Izbriši podatek na koncu seznama.'''
        if self._zacetek and self._zacetek.naslednji:
            vozel = self._zacetek
            while vozel.naslednji.naslednji is not None:
                vozel = vozel.naslednji
            self._konec = vozel
            vozel.naslednji = None
        elif self._zacetek:
            self._zacetek = self._konec = None
        else: raise IndexError('Verižni seznam je prazen') 
        

# =====================================================================@011071=
# 7. podnaloga
# Definicijo razreda `VerizniSeznam` zaključimo z metodo `je_prazen(self)`,
# ki vrne `True`, če je verižni seznam prazen, in `False`, če ni.
# =============================================================================
    def je_prazen(self):
        '''Preverimo ali je prazen'''
        return self._zacetek is None and self._konec is None

def je_cikel(verizni_seznam):
    '''preveri ali ima verizni seznam cikel algoritem zajca in želve'''
    pocasen = hiter = verizni_seznam.zacetek()
    while hiter and hiter.naslednji:
        pocasen = pocasen.naslednji
        hiter = hiter.naslednji.naslednji
        if hiter == pocasen:
            return True
    return False

