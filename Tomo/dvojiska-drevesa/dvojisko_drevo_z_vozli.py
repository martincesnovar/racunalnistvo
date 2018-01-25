# =============================================================================
# Dvojiško drevo z vozli
#
# Podatkovno strukturo dvojiškega drevesa smo v Pythonu predstavili z razredom
# `Drevo`, ki ponuja:
# 
# * Inicializator `Drevo()`, ki ustvari prazno drevo.
# * Inicializator `Drevo(podatek, levo, desno)`, ki ustvari neprazno drevo z
#   danim podatkom ter levim in desnim otrokom, ki sta prav tako razreda `Drevo`.
#   Argumenta `levo` in `desno` sta neobvezna. Če ju ne podamo, namesto njiju
#   vstavimo prazno drevo.
# * Atribut `prazno`, ki vrne `True`, če je drevo prazno, in `False`, če ni.
# * Atribut `podatek`, ki vrne podatek v korenu drevesa.
# * Atributa `levo` in `desno`, ki vrneta levega oziroma desnega otroka, prav
#   prav tako razreda `Drevo`.
# 
# Ena izmed možnih implementacij takega razreda je na voljo na 
#   <https://gist.githubusercontent.com/matijapretnar/65d4d5f3eec609f4276155cb1cee892d/raw/dvojisko_drevo.py>.
# 
# Pri tej nalogi boste napisali malo bolj sistematično implementacijo, ki
# samodejno izključi nekatere nekonsistentne predstavitve podatkov, na primer
# to, da bi imelo drevo atribut `prazno` nastavljen na `True`, hkrati pa bi
# vsebovalo podatke.
# 
# Drevo bomo predstavili z objektom, ki ima zgolj en atribut po imenu `_koren`,
# ki vsebuje bodisi `None` za prazno drevo bodisi trojico
# `(podatek, levo, desno)`, pri čemer sta `levo` in `desno` zopet drevesi.
# Sestavite razred `Drevo`, ki podpira zgoraj naštete možnosti.
# Ker `prazno`, `podatek`, `levo` in `desno` niso več atributi, morate uporabiti
# dekorator `@property`, ki omogoča, da jih implementirate z metodami,
# uporabnikom vašega razreda pa so še vedno na voljo kot atributi.
# =====================================================================@011148=
# 1. podnaloga
# Sestavite razred `Drevo`, kot je opisano v navodilih.
# =============================================================================

class Drevo:
    '''Drevo() prazno drevo
    Drevo(podatek, levo = Drevo(...), desno = Drevo(...))'''
    def __init__(self, *args, **kwargs):
        if args:
             assert len(args) == 1
             podatek = args[0] #
             levo = kwargs.pop('levo', None) or Drevo()
             desno = kwargs.pop('desno', None) or Drevo()
             self._koren = (podatek, levo, desno)
        else:
            self._koren = None
        assert not kwargs #ni drugih argumentov

    def __repr__(self, zamik=''):
        if self.prazno:
            return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
            return 'Drevo({1})'.format(zamik, self.podatek)
        else:
           return 'Drevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
               format(
                   zamik,
                   self.podatek,
                   self.levo.__repr__(zamik + '             '),
                   self.desno.__repr__(zamik + '              ')
               )
    def __eq__(self, other): return self._koren == other._koren

    def __hash__(self): return hash(self._koren)
    
    @property
    def prazno(self): return self.podatek is None
    @property
    def podatek(self): return self._koren
    @property
    def levo(self): return self._koren.levo
    @property
    def desno(self): return self._koren.desno

# =====================================================================@011149=
# 2. podnaloga
# Če ste strukturo pravilno implementirali, lahko sedaj v vseh nalogah že podano
# implementacijo nadomestite s svojo tako, da namesto
# 
#     from dvojisko_drevo import Drevo
# 
# pišete
# 
#     from dvojisko_drevo_z_vozli import Drevo
# 
# Poskusite in kot rešitev naloge napišite, če ste imeli kje kakšne težave.
# =============================================================================
ali_je_vse_delalo = True
kaj_je_delalo_in_kaj_ni = '''
    Vse je delalo
'''

