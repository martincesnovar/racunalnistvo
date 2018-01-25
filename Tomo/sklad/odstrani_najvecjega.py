# =============================================================================
# Odstrani največjega
#
# Sestavili bomo tri funkcije, ki spremenijo sklad celih števil tako, da v njem
# odstranijo največji podatek. Seveda je potrebno uporabljati le metode nad skladom,
# na koncu mora pa biti vrstni red elementov (tistih, ki ostanejo v skladu)
# nespremenjen. Če je v skladu le en največji podatek, se vse tri funcije obnašajo
# enako. Če pa sta dva ali celo več enakih največjih elementov, lahko postopamo
# na več možnih načinov:
# 
#  * odstranimo le najstarejšega (tistega, ki smo ga prvega vstavili v sklad) največjega;
#  * odstranimo vse največje;
#  * odstranimo le najmlajšega največjega.
# 
# Obstoječo implementacijo sklada bomo razširili tako kot v prejšnji nalogi.
# =====================================================================@010417=
# 1. podnaloga
# Sestavite metodo `odstrani_najvecje(self)`, ki iz sklada odstrani vse
# največje elemente. Sklad
# 
#     DNO : 8 : 6 : 14 : 10 : 14 : 13 : VRH
# 
# metoda spremeni v
# 
#     DNO : 8 : 6 : 10 : 13 : VRH
# 
# Zgled:
# 
#     >>> s = Sklad()
#     >>> for x in [8, 6, 14, 10, 14, 13]:
#     ...     s.vstavi(x)
#     >>> print(s)
#     DNO : 8 : 6 : 14 : 10 : 14 : 13 : VRH
#     >>> s.odstrani_najvecje()
#     >>> print(s)
#     DNO : 8 : 6 : 10 : 13 : VRH
# =============================================================================

from sklad import Sklad

class Sklad(Sklad):
    def odstrani_najvecje(self):
        '''Odstrani vse največje'''
        if self.prazen():
            return None
        naj = float('-inf')
        pomozni = Sklad()
        while not self.prazen():
            el = self.vrh()
            self.odstrani()
            naj = max(el,naj)
            pomozni.vstavi(el)
        while not pomozni.prazen():
            if naj != pomozni.vrh():
                self.vstavi(pomozni.vrh())
            pomozni.odstrani()
        

# =====================================================================@010418=
# 2. podnaloga
# Sestavite metodo `odstrani_najstarejsega_najvecjega(self)`, ki iz sklada
# odstrani najstarejši največji element. Zgled:
# 
#     >>> s = Sklad()
#     >>> for x in [8, 6, 14, 10, 14, 13]:
#     ...     s.vstavi(x)
#     >>> s.odstrani_najstarejsega_najvecjega()
#     >>> print(s)
#     DNO : 8 : 6 : 10 : 14 : 13 : VRH
# =============================================================================

class Sklad(Sklad):
    def odstrani_najstarejsega_najvecjega(self):
        '''Odstrani najstarejšega največjega'''
        if self.prazen():
            return None
        naj = float('-inf')
        prvi = False
        pomozni = Sklad()
        while not self.prazen(): #preložim v pomožnega
            el = self.vrh()
            self.odstrani()
            naj = max(el,naj)
            pomozni.vstavi(el)
        while not pomozni.prazen():
            if prvi or naj != pomozni.vrh() :
                self.vstavi(pomozni.vrh())
            else:
                prvi = True
                
            pomozni.odstrani()

# =====================================================================@010419=
# 3. podnaloga
# Sestavite metodo `odstrani_najmlajsega_najvecjega(self)`, ki iz sklada
# odstrani najmlajši največji element. Zgled:
# 
#     >>> s = Sklad()
#     >>> for x in [8, 6, 14, 10, 14, 13]:
#     ...     s.vstavi(x)
#     >>> s.odstrani_najmlajsega_najvecjega()
#     >>> print(s)
#     DNO : 8 : 6 : 14 : 10 : 13 : VRH
# =============================================================================


class Sklad(Sklad):
    def odstrani_najmlajsega_najvecjega(self):
        '''odstrani najmlajsega najvecjega'''
        if self.prazen():
            return None
        st=0
        naj = float('-inf')
        pomozni = Sklad()
        while not self.prazen(): #preložim v pomožnega
            el = self.vrh()
            pomozni.vstavi(el)
            if self.vrh()> naj:
                naj = self.vrh()
                st = 1
            elif self.vrh() == naj:
                st+=1
            self.odstrani()
        while not pomozni.prazen():
            if naj == pomozni.vrh():
                st-=1
                if st > 0:
                    self.vstavi(pomozni.vrh())
            else:
                self.vstavi(pomozni.vrh())                
            pomozni.odstrani()

