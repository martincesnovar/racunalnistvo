# =============================================================================
# Kovanci
# =====================================================================@010516=
# 1. podnaloga
# Znesek $z$ moramo plačati s kovanci z vrednostmi $v_1$, $v_2$, ..., $v_n$.
# Uporabimo lahko poljubno število kovancev iste vrednosti. Kako jih izbrati,
# da jim bomo porabili najmanj.
# 
# Sestavi funkcijo `placilo(z, v)`, ki za dani znesek `z` in vrednosti kovancev `v` (seznam)
# poišče in vrne števila posameznih kovancev (seznam), s katerimo lahko plačamo
# dani znesek in pri tem porabimo najmanj kovancev.
# 
#     >>> placilo(11, (1, 3, 4))
#     [0, 1, 2]
# =============================================================================

def placilo(z, v):
    '''poišče vrednosti kovancev, da porabimo čim manj kovancev'''
    if z <= 0:
        return [0 for _ in range(len(v))]
    sez = []
    for i in range(len(v)):
        preostanek = placilo(z - v[i], v[i:])
        if preostanek is not None:
            sez.append(i * [0] + [preostanek[0] + 1] + preostanek[1:])
    return min(sez, key=sum, default=None)

