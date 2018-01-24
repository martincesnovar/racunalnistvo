# =============================================================================
# Zavetišče
# =====================================================================@010440=
# 1. podnaloga
# V nekem živalskem zavetišču sprejemajo pse in mačke (bolj eksotičnih živali
# pa ne sprejemajo). Pravila zavetišča določajo, da dobi posvojitelj vedno
# tisto žival, ki je najdlje časa varovanec zavetišča. Pri tem lahko izbira
# med psom in mačko, lahko pa mu je vseeno glede vrste. Sestavite razred
# `Zavetisce`, ki bo upravniku v pomoč pri vodenju zavetišča.
# 
# Razred naj ima naslednje metode:
# 
# * `__init__(self)`, ki ustvari prazno zavetišče;
# * `sprejmi(self, ime, vrsta)`, ki evidentira novo žival z imenom `ime`, ki
#   je pripadnik vrste `vrsta` (ta ima lahko vrednost `'pes'` ali `'mačka'`);
# * `oddaj_psa(self)`, ki vrne ime psa, ki je na vrsti za posvojitev (in ga
#   tudi odstrani iz evidence);
# * `oddaj_macko(self)`, ki deluje podobno kot `oddaj_psa`, vendar za mačke;
# * `oddaj_zival(self)`, ki deluje podobno kot `oddaj_psa` in `oddaj_macko`,
#   vendar vrne žival tiste vrste, ki je prva na vrsti za posvojitev.
# 
# Metode `oddaj_psa`, `oddaj_macko` in `oddaj_zival` naj vrnejo `None`, če
# ustrezne živali ni na voljo. Primer:
# 
#     >>> z = Zavetisce()
#     >>> z.sprejmi('Taček', 'pes')
#     >>> z.sprejmi('Šarki', 'pes')
#     >>> z.oddaj_macko()
#     None
#     >>> z.sprejmi('Tom', 'mačka')
#     >>> z.oddaj_psa()
#     'Taček'
#     >>> z.sprejmi('Nyan', 'mačka')
#     >>> z.oddaj_zival()
#     'Šarki'
# 
# _Namig_: Uporabite dve vrsti, tako da v eni hranite pse, v drugi pa mačke.
# V vrsti hranite pare, ki vsebujejo ime in čas prihoda, npr. `('Taček', 1)`.
# =============================================================================

from vrsta import *


class Zavetisce:
    def __init__(self):
        self.macki = Vrsta()
        self.psi = Vrsta()
        self.cas_prihoda = 0
        
    def sprejmi(self, ime, vrsta):
        self.ime = ime
        if vrsta == 'pes':
            self.psi.vstavi((self.ime, self.cas_prihoda))
        elif vrsta == 'mačka':
            self.macki.vstavi((self.ime, self.cas_prihoda))
        else:
            raise ValueError('Eksotična vrsta')
        self.cas_prihoda += 1
            
    def oddaj_psa(self):
        if self.psi.prazna():
            return None
        pes = self.psi.zacetek()[0]
        self.psi.odstrani()
        return pes

    def oddaj_macko(self):
        if self.macki.prazna():
            return None
        maček = self.macki.zacetek()[0]
        self.macki.odstrani()
        return maček

    def oddaj_zival(self):
        if self.macki.prazna():
            return self.oddaj_psa()
        if self.psi.prazna():
            return self.oddaj_macko()
        macek_ime, macek_cas = self.macki.zacetek()
        pes_ime, pes_cas = self.psi.zacetek()
        if pes_cas < macek_cas:
            self.psi.odstrani()
            return pes_ime
        else:
            self.macke.odstrani()
            return macek_ime
    
    
    

# =====================================================================@010441=
# 2. podnaloga
# Zavetišče je obiskala informacijska pooblaščenka, ki je prepovedala hranjenje
# časa prihoda živali. Zdaj morate napisati nov razred `ZavetiscePoPredpisih`,
# ki naj deluje enako kot `Zavetisce`, le da ne hrani časov prihoda živali.
# 
# _Namig_: Živali hranite v eni sami vrsti, ki naj vsebuje pare podatkov in
# sicer ime živali ter vrsto, npr. `('Taček', 'pes')`.
# =============================================================================

class ZavetiscePoPredpisih:
    def __init__(self):
        self.zivali = Vrsta()
        
    def sprejmi(self, ime, vrsta):
        self.ime = ime
        if vrsta in {'pes', 'mačka'}:
            self.vrsta = vrsta
            self.zivali.vstavi((self.ime, self.vrsta))
            
    def oddaj_psa(self):
        zivali_temp = Vrsta()
        prvi = True
        pes = None
        if self.zivali.prazna():
            return None
        while not self.zivali.prazna():
            if self.zivali.zacetek()[1] != 'pes' or not prvi:
                zivali_temp.vstavi(self.zivali.zacetek())
            if self.zivali.zacetek()[1] == 'pes' and prvi:
                pes = self.zivali.zacetek()[0]
                prvi = False
            self.zivali.odstrani()
        while not zivali_temp.prazna():
            self.zivali.vstavi(zivali_temp.zacetek())
            zivali_temp.odstrani()
        return pes

    def oddaj_macko(self):
        if self.zivali.prazna():
            return None
        maček = None
        zivali_temp = Vrsta()
        prvi = True
        if self.zivali.prazna():
            return None
        while not self.zivali.prazna():
            if self.zivali.zacetek()[1] != 'mačka' or not prvi:
                zivali_temp.vstavi(self.zivali.zacetek())
            if self.zivali.zacetek()[1] == 'mačka' and prvi:
                maček = self.zivali.zacetek()[0]
                prvi = False
            self.zivali.odstrani()
        while not zivali_temp.prazna():
            self.zivali.vstavi(zivali_temp.zacetek())
            zivali_temp.odstrani()
        return maček
        

    def oddaj_zival(self):
        if self.zivali.prazna():
            return None
        vrh = self.zivali.zacetek()[0]
        self.zivali.odstrani()
        return vrh


