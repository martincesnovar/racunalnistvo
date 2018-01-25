# =============================================================================
# Permutacije s skladom
# =====================================================================@010416=
# 1. podnaloga
# Permutacije sestavljamo s pomočjo sklada tako, da vanj po vrsti
# vstavljamo števila od 1 do $n$, kadarkoli (če je to seveda možno) pa
# lahko z vrha sklada vzamemo eno ali več števil. Vrstni red števil, ki
# jih odstranjujemo s sklada, določa sestavljeno permutacijo. Spodnjo
# permutacijo sestavimo tako, da na sklad vstavimo 1, 2 in 3, odstranimo
# 3 in 2, nato vstavimo 4 in 5, odstranimo 5, vstavimo 6 in 7 ter odstranimo
# 7, 6, 4 in 1.
# 
# $$
# \begin{pmatrix}
# 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
# 3 & 2 & 5 & 7 & 6 & 4 & 1
# \end{pmatrix}
# $$
# 
# S skladom ne moremo sestaviti poljubne permutacije. Sestavite funkcijo
# `permutacija_s_skladom(perm)`, ki naj bo linearne časovne zahtevnosti.
# Funkcija naj preveri, ali lahko dano permutacijo sestavimo s pomočjo sklada.
# Permutacija je dana s premešanim seznamom števil od 1 do $n$. Zgled:
# 
#     >>> permutacija_s_skladom([3, 2, 5, 7, 6, 4, 1])
#     True
#     >>> permutacija_s_skladom([3, 5, 4, 7, 2, 6, 1])
#     False
# =============================================================================


from sklad import Sklad

def permutacija_s_skladom(sez):
    '''Ali lahko dano permutacijo sestavimo s skladom'''
    n=0
    s = Sklad()
    for el in sez:
        while n < el:
            n+=1
            s.vstavi(n)
        if s.prazen() or el != s.vrh():
            return False
        s.odstrani()
    return True


