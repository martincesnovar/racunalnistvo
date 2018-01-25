# =============================================================================
# Vstavljanje iz tabele v sklad
# =====================================================================@010413=
# 1. podnaloga
# Sestavite funkcijo `vstavi_vec(s, tabela)`, ki bo v sklad `s` po vrsti
# vstavila vse elemente iz seznama `tabela`, začenši z elementom na mestu 0.
# Zgled:
# 
#     >>> s = Sklad()
#     >>> s.vstavi(5)
#     >>> s.vstavi(3)
#     >>> print(s)
#     DNO : 5 : 3 : VRH
#     >>> vstavi_vec(s, [11, 2, 5])
#     >>> print(s)
#     DNO : 5 : 3 : 11 : 2 : 5 : VRH
# =============================================================================

from sklad import *

def vstavi_vec(s,tabela):
    '''s -sklad, tabela -sez'''
    for el in tabela:
        s.vstavi(el)

        
