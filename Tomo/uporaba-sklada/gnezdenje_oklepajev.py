# =============================================================================
# Gnezdenje oklepajev
#
# Oklepaji so pravilno gnezdeni, če uklepaji in zaklepaji istega tipa nastopajo
# v parih in število zaklepajev nikoli ne preseže števila uklepajev, ko jih
# štejemo od leve proti desni. V spodnjih nalogah poznamo naslednje tipe
# oklepajev
# 
#     OKLEPAJI = {
#         '(': ')',
#         '{': '}',
#         '[': ']',
#         '<': '>'
#     }
# =====================================================================@010425=
# 1. podnaloga
# Sestavite funkcijo `oklepaji(niz)`, ki bo preverila, ali so v danem
# nizu oklepaji pravilno gnezdeni. Na ostale znake naj se funkcija ne
# ozira. Zgled:
# 
#     >>> oklepaji('(a + b)^2 = ({[a^2] + 2ab} + b^2)')
#     True
#     >>> oklepaji('[])({}')
#     False
# =============================================================================
OKLEPAJI = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

from sklad import Sklad

def oklepaji(niz):
    s = Sklad()
    for c in niz:
        if c in OKLEPAJI:
            s.vstavi(c)
        if c in OKLEPAJI.values():
            if s.prazen() or OKLEPAJI[s.vrh()] != c:
                return False
            s.odstrani()
    return s.prazen()

# =====================================================================@010426=
# 2. podnaloga
# Sestavite funkcijo `max_globina(niz)`, ki poišče globino najbolj globoko
# gnezdenega para oklepajev v izrazu `niz`. Funkcija naj bo dopolnitev funkcije
# iz prejšnje podnaloge. V primeru pravilno gnezdenih oklepajev naj torej vrne
# največjo globino, v nasprotnem primeru pa `None`. Zgled:
# 
#     >>> max_globina('(a + b)^2 = ({[a^2] + 2ab} + b^2)')
#     3
#     >>> max_globina('[])({}')
#     None
# =============================================================================

def max_globina(niz):
    s = Sklad()
    naj = 0
    trenutna = 0
    if not oklepaji(niz):
        return
    for c in niz:
        if c in OKLEPAJI:
            s.vstavi(c)
            trenutna+=1
            naj = max(trenutna,naj)
        if c in OKLEPAJI.values():
            if s.prazen() or OKLEPAJI[s.vrh()] != c:
                return
            s.odstrani()
            trenutna-=1
    return naj

