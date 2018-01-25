# =============================================================================
# Dvojiško drevo s pregledi
#
# Tako kot v prejšnji nalogi napišite implementacijo razreda `Drevo`, le da
# imate tokrat le en razred `Drevo`, vsak objekt pa ima atributa
# `_vmesni_pregled` in `_premi_pregled`, ki sta seznama vrednosti v vmesnem in
# premem pregledu drevesa. Predpostavite lahko, da bomo v drevo shranjevali le
# različne vrednosti, zato je drevo s tema dvema pregledoma natanko določeno.
# =====================================================================@011150=
# 1. podnaloga
# Sestavite razred `Drevo`, kot je opisano v navodilih.
# =============================================================================

class Drevo:
    def __init__(self, *args, **kwargs):
        if args:
            assert len(args) == 1
            podatek = args[0]
            levo = kwargs.pop('levo', None) or Drevo()
            desno = kwargs.pop('desno', None) or Drevo()
            self._vmesni_pregled = levo._vmesni_pregled + [podatek] + desno._vmesni_pregled
            self._premi_pregled = [podatek] + levo._premi_pregled + desno._premi_pregled
        else:
            self._premi_pregled = []
            self._vmesni_pregled = []
        assert not kwarqs

    def __repr__(self, zamik=''):
        if self.prazno:
            return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
            return 'Drevo({1})'.format(zamik, self.podatek)
        else:
            return 'Drevo({1},\n{0} levo = {2},\n{0} desno = {3})'.\
                format(
                  zamik,
                  self.podatek,
                  self.levo.__repr__(zamik + ' '),
                  self.desno.__repr__(zamik + ' ')
                  )

    def __eq__(self, other):
        return (self._vmesni_pregled, self._premi_pregled) == (other._vmesni_pregled, other._premi_pregled) 

    def __hash__(self):
        return hash(self._vmesni_pregled, self._premi_pregled)

    @property
    def prazno(self):
        return len(self._premi_pregled) == 0

    @property
    def podatek(self):
        return self._premi_pregled[0]

    @property
    def levo(self):
        vrednost_korena = self.podatek
        i = self._vmesni_pregled.index(vrednost_korena)
        levo = Drevo()
        levo._vmesni_pregled = self._vmesni_pregled[:i]
        levo._premi_pregled = self._premi_pregled[1:i + 1]
        return levo
    @property
    def desno(self):
        vrednost_korena = self.podatek
        i = self._vmesni_pregled.index(vrednost_korena)
        desno = Drevo()
        desno._vmesni_pregled = self._vmesni_pregled[i + 1:]
        desno._premi_pregled = self._premi_pregled[i + 1:]
        return desno

    
# =====================================================================@011154=
# 2. podnaloga
# Če ste strukturo pravilno implementirali, lahko sedaj v vseh nalogah že podano
# implementacijo nadomestite s svojo tako, da namesto
# 
#     from dvojisko_drevo import Drevo
# 
# pišete
# 
#     from dvojisko_drevo_s_pregledi import Drevo
# 
# Poskusite in kot rešitev naloge napišite, če ste imeli kje kakšne težave.
# =============================================================================
ali_je_vse_delalo = True
kaj_je_delalo_in_kaj_ni = '''
    Vse dela, kot je pričakovano
'''

