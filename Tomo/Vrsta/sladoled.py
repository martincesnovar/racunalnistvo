# =============================================================================
# Sladoled
# =====================================================================@010443=
# 1. podnaloga
# Pred kioskom v ravni vrsti stojijo otroci, ki kupujejo sladoled. Za vsakega
# otroka vemo, kako močan je. Večja številka pomeni, da je otrok močnejši. Ko
# pride nek otrok na vrsto, najprej pogleda, če v vrsti stoji še kdo, ki je
# močnejši. V tem primeru se ustraši in se vljudno umakne na konec vrste, sicer
# pa si kupi sladoled.
# 
# Denimo, da je na začetku vrsta takšna:
# 
#     KIOSK 2 1 3 2 3 1 3
# 
# Otrok, ki je prvi na vrsti, opazi, da je za njim močnejši, zato se umakne
# na konec:
# 
#     KIOSK 1 3 2 3 1 3 2
# 
# Otrok, ki je zdaj prvi v vrsti, se tudi vljudno umakne na konec, saj za njim
# stoji močnejši otrok. Novo stanje je takšno:
# 
#     KIOSK 3 2 3 1 3 2 1
# 
# Otrok, ki je zdaj na začetku vrste, kupi sladoled in gre, v vrsti pa ostanejo:
# 
#     KIOSK 2 3 1 3 2 1
# 
# Tako nadaljujejo, dokler vsi otroci ne dobijo sladoleda.
# 
# Sestavite funkcijo `kdaj_pridem_na_vrsto(otroci)`, ki kot argument dobi seznam
# moči otrok in vrne nov seznam, ki vsebuje števila od 1 naprej. Pri tem naj
# $i$-to število v izhodnem seznamu pomeni, kateri po vrsti kupi sladoled otrok,
# ki je bil na začetku $i$-ti v vrsti. Zgled:
# 
#     >>> kdaj_pridem_na_vrsto([2, 1, 3, 2, 3, 1, 3])
#     [4, 7, 1, 5, 2, 6, 3]
# 
# Namig: V vrsti lahko hranite pare dveh števil, kjer je prvo število zaporedna
# številka otroka (kje je stal na začetku), drugo pa je njegova moč. Če vam je
# lažje, si definirajte pomožno funkcijo, ki kot argument dobi vrsto, vrne pa
# moč najmočnejšega otroka v vrsti. Pri tem naj vrste ne spremeni.
# =============================================================================

from vrsta import Vrsta

def moc_najmocnejsega_v_vrsti(vrs):
    '''Vrne moč otroka, ki ima v vrsti največjo moč'''
    vr = Vrsta()
    st = 0
    naj_st = 0
    while not vrs.prazna():
        st = vrs.zacetek()[1]
        naj_st = max(naj_st, st)
        vr.vstavi(vrs.zacetek())
        vrs.odstrani()
    while not vr.prazna():
        vrs.vstavi(vr.zacetek())
        vr.odstrani()
    return naj_st

def kdaj_pridem_na_vrsto(otrok):
    '''Sprejme seznam otrok- "vrsto" pred kioskom in
    vrne seznam, v katerem je izračunano, koliko
    časa bo moral otrok čakati na sladoled'''
    sez = [0]*len(otrok)
    vrsta = Vrsta()
    cas=1
    for i, el in enumerate(otrok):
        vrsta.vstavi((i,el))
    while not vrsta.prazna():
        st = vrsta.zacetek()[1]
        moč = moc_najmocnejsega_v_vrsti(vrsta)
        if st < moč:
            vrsta.vstavi(vrsta.zacetek()) #vstavi na konec
            vrsta.odstrani()
        else:
            sez[vrsta.zacetek()[0]] = cas
            vrsta.odstrani()
            cas+=1
    return sez

