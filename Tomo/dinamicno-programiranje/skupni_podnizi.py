# =============================================================================
# Skupni podnizi
# =====================================================================@010515=
# 1. podnaloga
# Sestavi funkcijo `skupen_podniz(niz1, niz2)`, ki poišče in vrne najdaljši,
# ne nujno strnjen, skupen podniz nizov `niz1` in `niz2`. Pri tem je podniz
# poljubno zaporedje znakov iz prvega niza, ki v istem relativnem vrstnem redu
# nastopajo tudi v drugem nizu.
# 
#     >>> skupen_podniz("konkurenca", "komutativno")
#     'koua'
# =============================================================================
from functools import lru_cache

@lru_cache(maxsize=None)
def skupen_podniz(niz1, niz2):
    '''Vrne skupen podniz'''
    if niz1 == '' or niz2 == '':
        return ''
    elif niz1[0] == niz2[0]:
        return niz1[0] + skupen_podniz(niz1[1:], niz2[1:])
    else:
        prvi_podniz = skupen_podniz(niz1, niz2[1:])
        drugi_podniz = skupen_podniz(niz1[1:], niz2)
        return prvi_podniz if len(prvi_podniz) > len(drugi_podniz) else drugi_podniz

