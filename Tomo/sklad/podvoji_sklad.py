# =============================================================================
# Podvoji sklad
# =====================================================================@010415=
# 1. podnaloga
# Sestavi funkcijo `podvoji_sklad(s)`, ki kot argument dobi sklad `s` in
# _sestavi ter vrne nov sklad_, ki ga dobi tako, da "podvoji" vsak element
# na skladu `s`. Na koncu mora biti sklad `s` v enakem stanju kot na začetku.
# Zgled:
# 
#     >>> s = Sklad()
#     >>> s.vstavi(1)
#     >>> s.vstavi(3)
#     >>> s.vstavi(5)
#     >>> podvojen = podvoji_sklad(s)
#     >>> print(s)
#     DNO : 1 : 3 : 5 : VRH
#     >>> print(podvojen)
#     DNO : 1 : 1 : 3 : 3 : 5 : 5 : VRH
# =============================================================================
from sklad import Sklad

def podvoji_sklad(s):
    '''Podvoji sklad'''
    podvojen = Sklad()
    pomozen = Sklad()
    while not s.prazen():
        x = s.vrh()
        s.odstrani()
        pomozen.vstavi(x)
    while not pomozen.prazen():
        x = pomozen.vrh()
        pomozen.odstrani()
        podvojen.vstavi(x)
        podvojen.vstavi(x)
        s.vstavi(x)
    return podvojen

