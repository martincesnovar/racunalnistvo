# =============================================================================
# Aritmetični izraz
#
# Aritmetične izraze, kot je na primer $(9 * (2 - 7)) + (5 * 3)$, lahko zapišemo
# v obliki dvojiškega drevesa (glejte spodaj). V vsakem vozlišču je zapisano
# bodisi neko celo število bodisi nek aritmetični operator. (Da ne bi imeli
# problemov z deljenjem s številom $0$, se bomo omejili na operatorje $+$, $-$
# in $*$.) Če vozlišče predstavlja operator, potem ima nujno levega in desnega
# sina, ki predstavljata ustrezna podizraza. V nasprotnem primeru vozlišče
# predstavlja število in je nujno list drevesa. (Ste opazili, da je v korenu
# drevesa na spodnji sliki operator $+$, ki ga v tem izrazu izračunamo kot
# zadnjega?)
# 
#     zgled = Drevo('+',
#                   levo=Drevo('*',
#                              levo=Drevo(9),
#                              desno=Drevo('-',
#                                          levo=Drevo(2),
#                                          desno=Drevo(7))),
#                   desno=Drevo('*',
#                               levo=Drevo(5),
#                               desno=Drevo(3)))
# =====================================================================@010484=
# 1. podnaloga
# Sestavite funkcijo `vrednost(izraz)`, ki izračuna in vrne vrednost tega
# aritmetičnega izraza. Primer (če `d` ustreza zgornji sliki):
# 
#     >>> vrednost(d)
#     -30
# =============================================================================
from dvojisko_drevo import Drevo

def vrednost(izraz):
    '''izračuna vrednost izraza'''
    if izraz.podatek == '+':
        return vrednost(izraz.levo) + vrednost(izraz.desno)
    elif izraz.podatek == '-':
        return vrednost(izraz.levo) - vrednost(izraz.desno)
    elif izraz.podatek == '*':
        return vrednost(izraz.levo) * vrednost(izraz.desno)
    else:
        return izraz.podatek
        
# =====================================================================@010485=
# 2. podnaloga
# Napišite funkcijo `obicajni_zapis(izraz)`, ki vrne niz z običajnim zapisom
# tega izraza (glejte primer spodaj). Pred in za vsakim operatorjem naj bo po en
# presledek. Podizrazi naj bodo v oklepajih, razen kadar so le-ti števila.
# Sicer oklepajev ne smete opuščati (pa čeprav nam asociativnostni zakon to
# omogoča). Primer (če `d` ustreza zgornji sliki):
# 
#     >>> obicajni_zapis(d)
#     '(9 * (2 - 7)) + (5 * 3)'
# =============================================================================
def je_stevilo(izraz):
    '''preveri ali je število'''
    return isinstance(izraz.podatek, int)

def obicajni_zapis(d, oklepaji=False):
    '''Vrne običajni zapis'''
    if je_stevilo(d):
        return str(d.podatek)
    zapis = '{0} {1} {2}'.format(obicajni_zapis(d.levo, oklepaji=True),
                                 d.podatek,
                                 obicajni_zapis(d.desno, oklepaji=True))
    return '(' + zapis + ')' if oklepaji else zapis

# =====================================================================@010486=
# 3. podnaloga
# Sestavite funkcijo `poenostavi(izraz)`, ki vrne poenostavljen izraz, tako da
# odpravi "najbolj notranje" operatorje, tj. tiste operatorje, kjer sta oba
# podizraza števili. Primer (če `d` ustreza zgornjemu izrazu):
# 
#     >>> poenostavi(d)
#     Drevo('+', levo=Drevo('*', levo=Drevo(9), desno=Drevo(-5)), desno=Drevo(15))
# =============================================================================

def poenostavi(d):
    '''poenostavi najbolj notranje operacije'''
    if je_stevilo(d):
        return d
    elif je_stevilo(d.levo) and je_stevilo(d.desno):
        return Drevo(vrednost(d))
    else:
        return Drevo(d.podatek, levo = poenostavi(d.levo), desno = poenostavi(d.desno))

