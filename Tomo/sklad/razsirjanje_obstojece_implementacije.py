# =============================================================================
# Razširjanje obstoječe implementacije
#
# V tej nalogi bomo razširili obstoječo implementacijo sklada v razredu `Sklad`.
# To storimo tako, da ob definiciji novega razreda `SuperSklad`, povemo, da naj
# podeduje vse obstoječe metode razreda `Sklad`:
# 
#     from sklad import Sklad
#     
#     class SuperSklad(Sklad):
#     
#         def nova_metoda(self):
#             ...
# 
# Če nočemo spreminjati imena novega razreda, ga lahko poimenujemo tako kot
# starega:
# 
#     class Sklad(Sklad):
#     
#         def nova_metoda(self):
#             ...
# 
# V tem primeru prvi `Sklad` predstavlja nov razred, drugi `Sklad` pa starega.
# 
# Morda ste definicije oblike
# 
#     class ImeRazreda(ImeRazreda):
#         ...
# 
# že videli pri uradnih rešitvah nalog z razredi na Projektu Tomo. Tu se je
# dedovanje uporabljalo za obvod okoli določenih omejitev testiranja na
# Projektu Tomo.
# =====================================================================@010534=
# 1. podnaloga
# Sestavite metodo `pop(s)`, ki vrne in izbriše vrhnji podatek v skladu.
# Zgled:
# 
#     >>> s = Sklad()
#     >>> s.vstavi(6)
#     >>> s.vstavi(3)
#     >>> s.vstavi(1)
#     >>> print(s)
#     DNO : 6 : 3 : 1 : VRH
#     >>> s.pop()
#     1
#     >>> print(s)
#     DNO : 6 : 3 : VRH
# =============================================================================
from sklad import Sklad
class Sklad(Sklad):
    def pop(self):
        '''Vrne vrhnji element in ga odstrani'''
        vrh = self.podatki[-1]
        self.odstrani()
        return vrh
        

# =====================================================================@010414=
# 2. podnaloga
# Sestavite metodo `prestej_elemente(s)`, ki izračuna in vrne število
# podatkov v skladu `s`. Sklad `s` mora ostati nespremenjen.
# Zgled:
# 
#     >>> s = Sklad()
#     >>> s.vstavi(6)
#     >>> s.vstavi(3)
#     >>> s.vstavi(1)
#     >>> s.prestej_elemente()
#     3
# 
# Namig: s pomočjo metode `pop` podatke preložite na pomožen sklad in nazaj.
# =============================================================================

class Sklad(Sklad):
    def prestej_elemente(self):
        '''Prešteje elemente s pomočjo metode pop in pomožnega sklada'''
        i=0
        pomozni = Sklad()
        while not self.prazen():
            pomozni.vstavi(self.pop())
            i+=1
        while not pomozni.prazen():
            self.vstavi(pomozni.pop())
        return i

