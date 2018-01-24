# =============================================================================
# Delo z vrsto
# =====================================================================@010435=
# 1. podnaloga
# Napišite funkcijo `prestej_elemente(v)`, ki kot argument dobi vrsto `v` in
# vrne število elementov v vrsti. Ko funkcija konča, mora biti vrsta `v` enakem
# stanju kot na začetku.
# 
# Zgled:
# 
#     >>> v = Vrsta([4, 5, 6])
#     >>> v.vstavi(7)
#     >>> prestej_elemente(v)
#     4
#     >>> v
#     Vrsta([4, 5, 6, 7])
# =============================================================================
from vrsta import *


# Spodnja funkcija sicer prešteje elemente, ampak jih pri tem tudi vse zavrže.
def prestej_elemente(v):
    '''presteje elemente'''
    stevec = 0
    pomozna = Vrsta(None)
    while not v.prazna():
        stevec += 1
        pomozna.vstavi(v.zacetek())
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()
    return stevec
# =====================================================================@010436=
# 2. podnaloga
# Sestavite funkcijo `prestej_pogojno(v, p)`, ki kot argument dobi vrsto `v`
# in funkcijo `p` (funkcija `p` dobi en argument in vrne logično vrednost) ter
# prešteje koliko je takih elementov v vrsti, za katere funkcija `p` vrne True.
# Ko funkcija konča, mora biti vrsta `v` enakem stanju kot na začetku.
# 
# Zgled:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])
#     >>> prestej_pogojno(v, lambda x: x % 2 == 0)
#     4
# =============================================================================

def prestej_pogojno(v, p):
    '''presteje tiste elemente vrste, ki vrnejo true'''
    stevec = 0
    pomozna = Vrsta(None)
    while not v.prazna():
        if p(v.zacetek()):
            stevec+=1
        pomozna.vstavi(v.zacetek())
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()
    return stevec

# =====================================================================@010437=
# 3. podnaloga
# Sestavite funkcijo `odstrani_ntega(v, n)`, ki kot argumenta dobi vrsto `v`
# in celo število `n`. Funkcija naj iz vrste `v` odstrani $n$-ti zaporedni
# element (šteti začnemo pri 0). Če vrsta ne vsebuje $n$-tega (ker je prekratka),
# naj je funkcija ne spremeni.
# 
# Primer:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5, 6, 7])
#     >>> odstrani_ntega(v, 3)
#     >>> v
#     Vrsta([1, 2, 3, 5, 6, 7])
# =============================================================================

def odstrani_ntega(v, n):
    '''odstrani n-ti element vrste štejemo z 0'''
    stevec = 0
    pomozna = Vrsta(None)
    while not v.prazna():
        if stevec!=n:
            pomozna.vstavi(v.zacetek())
        stevec += 1
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()
    return stevec

# =====================================================================@010438=
# 4. podnaloga
# Sestavite funkcijo `odstrani_pogojno(v, p)`, ki kot argumenta dobi vrsto `v`
# in funkcijo `p` (funkcija `p` dobi en argument in vrne logično vrednost) ter
# odstrani tiste elemente v vrsti, za katere funkcija `p` vrne `True`.
# 
# Primer:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5, 6, 7, 8])
#     >>> odstrani_pogojno(v, lambda x: x % 2 == 0)
#     >>> v
#     Vrsta([1, 3, 5, 7])
# =============================================================================

def odstrani_pogojno(v, p):
    '''odstrani tiste elemente, kjer vrne fukncija p True'''
    pomozna = Vrsta(None)
    while not v.prazna():
        if not p(v.zacetek()):
            pomozna.vstavi(v.zacetek())
        v.odstrani()
    while not pomozna.prazna():
        v.vstavi(pomozna.zacetek())
        pomozna.odstrani()

# =====================================================================@010439=
# 5. podnaloga
# Sestavite funkcijo `obrni(v)`, ki obrne vrsto `v`. Pri tem si pomagajte s
# skladom.
# 
# Zgled:
# 
#     >>> v = Vrsta([1, 2, 3, 4, 5])
#     >>> obrni(v)
#     >>> v
#     Vrsta([5, 4, 3, 2, 1])
# =============================================================================
from sklad import *
def obrni(v):
    '''s pomočjo sklada obrne vrsto'''
    s = Sklad()
    while not v.prazna(): #damo na sklad
        s.vstavi(v.zacetek())
        v.odstrani()
    while not s.prazen(): #vrnemo nazaj v vrsto -obratni vrstni red
        v.vstavi(s.vrh())
        s.odstrani()

        
