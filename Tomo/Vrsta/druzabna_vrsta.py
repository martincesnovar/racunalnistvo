# =============================================================================
# Družabna vrsta
# =====================================================================@010444=
# 1. podnaloga
# V zelo popularno menzo hodijo na kosilo ljudje iz različnih ustanov. Vljudno
# bi bilo, če bi se vsak, ki pride, postavil na konec vrste. Ampak v praksi se
# izkaže, da to ne drži. Prišlek namreč v vrsti poišče zadnjega, ki prihaja iz
# iste ustanove kot on, in se z njim zaplete v pogovor. Klepet izkoristi za to,
# da se vrine v vrsto za zadnjega iz svoje skupine. Sestavite razred `DruzabnaVrsta`,
# ki naj ima naslednje metode:
# 
# * `__init__(self)`, ki ustvari prazno vrsto;
# * `dodaj_prisleka(self, ime, skupina)`, ki doda osebo z imenom `ime`, ki
# pripada skupini `skupina`;
# * `ime_prvega(self)`, ki vrne ime osebe, ki je trenutno prva v vrsti;
# * `postrezi(self)`, ki iz vrste odstrani prvega (ta dobi svoje kosilo in gre
# sedet k mizi).
# 
# Primer:
# 
#     >>> menza = DruzabnaVrsta()
#     >>> menza.dodaj_prisleka('Marjan', 'FMF')
#     >>> menza.dodaj_prisleka('Petra', 'FKKT')
#     >>> menza.dodaj_prisleka('Borut', 'FDV')
#     >>> menza.dodaj_prisleka('Tanja', 'FMF')
#     >>> menza.dodaj_prisleka('Boris', 'FKKT')
#     >>> menza.ime_prvega()
#     'Marjan'
#     >>> menza.postrezi()
#     >>> menza.ime_prvega()
#     'Tanja'
#     >>> menza.postrezi()
#     >>> menza.ime_prvega()
#     'Petra'
#     >>> menza.postrezi()
#     >>> menza.ime_prvega()
#     'Boris'
# 
# Razred `DruzabnaVrsta` naj uporablja vrsto iz modula `Vrsta`.
# =============================================================================

from vrsta import Vrsta

class DruzabnaVrsta:
    def __init__(self):
        self.vrsta = Vrsta()
        
    def dodaj_prisleka(self, ime, skupina):
        '''doda prišleka, upošteva skupino'''
        pomozna_vrsta = Vrsta()
        zadnji_v_vrsti = None
        st = 0
        while not self.vrsta.prazna():
            ime1, skupina1 = self.vrsta.zacetek()
            self.vrsta.odstrani()
            pomozna_vrsta.vstavi((ime1, skupina1))
            st+=1
            if skupina == skupina1:
                zadnji_v_vrsti = st
        st=0
        while not pomozna_vrsta.prazna():
            ime1, skupina1 = pomozna_vrsta.zacetek()
            pomozna_vrsta.odstrani()
            self.vrsta.vstavi((ime1, skupina1))
            st+=1
            if st == zadnji_v_vrsti:
                self.vrsta.vstavi((ime, skupina))

        if zadnji_v_vrsti is None:
            self.vrsta.vstavi((ime, skupina))
            
            

    def ime_prvega(self):
        if not self.vrsta.prazna():
            return self.vrsta.zacetek()[0]

    def postrezi(self):
        if not self.vrsta.prazna():
            self.vrsta.odstrani()

