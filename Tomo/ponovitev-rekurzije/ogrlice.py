# =============================================================================
# Ogrlice
#
# Takrat, ko je upokojenki Marti dolgčas, vzame svoji dve posodici z belimi
# in rdečimi kroglicami ter začne nizati ogrlice. Te ogrlice bomo predstavili
# z nizi, sestavljenimi iz znakov `B` in `R`.
# 
# Na primer: `'BBRBBRB'` in `'RRBBBBB'` sta dve izmed 21 možnih ogrlic,
# sestavljenih iz petih belih in dveh rdečih kroglic.
# =====================================================================@010381=
# 1. podnaloga
# Sestavite funkcijo `je_ogrlica(niz, b, r)`, ki preveri, ali `niz`
# predstavlja ogrlico iz `b` belih in `r` rdečih kroglic. Na primer:
# 
#     >>> je_ogrlica('BBRBBRB', 5, 2)
#     True
#     >>> je_ogrlica('RRBBBBB', 5, 2)
#     True
#     >>> je_ogrlica('BBRBBRB', 2, 5)
#     False
#     >>> je_ogrlica('BBRBBRBBB', 5, 2)
#     False
#     >>> je_ogrlica('BBRBBRBXY', 5, 2)
#     False
# =============================================================================

def je_ogrlica(niz, b, r):
    st_b = 0; st_r = 0
    for znak in niz:
        if znak == 'B':
            st_b+=1
        if znak == 'R':
            st_r+=1
        if znak not in 'BR':
            return False
    return st_b==b and st_r==r

# =====================================================================@010382=
# 2. podnaloga
# Z $O(b, r)$ označimo število različnih ogrlic, sestavljenih iz natanko
# $b$ belih in $r$ rdečih kroglic. Če je eno od števil $b$ ali $r$ enako
# nič, potem je $O(b, r) = 1$. Na primer, $O(5, 0) = 1$, saj iz petih
# belih kroglic lahko sestavimo le ogrlico `'BBBBB'`.
# 
# V nasprotnem primeru pa velja $O(b, r) = O(b - 1, r) + O(b, r - 1)$,
# saj se vsaka izmed ogrlic iz $b$ belih in $r$ rdečih kroglic:
# 
# * bodisi začne z belo kroglico, preostalih $b - 1$ belih in $r$ rdečih
#   kroglic pa lahko sestavimo na $O(b - 1, r)$ načinov,
# * bodisi začne z rdečo kroglico, preostalih $b$ belih in $r - 1$ rdečih
#   kroglic pa lahko sestavimo na $O(b, r - 1)$ načinov.
# 
# Sestavite funkcijo `stevilo_ogrlic(b, r)`, ki izračuna število vseh
# možnih ogrlic, sestavljenih iz natanko `b` belih in `r` rdečih kroglic.
# Na primer:
# 
#     >>> stevilo_ogrlic(5, 0)
#     1
#     >>> stevilo_ogrlic(5, 2)
#     21
#     >>> stevilo_ogrlic(4, 2)
#     15
#     >>> stevilo_ogrlic(5, 1)
#     6
# =============================================================================

def stevilo_ogrlic(b, r):
    '''koliko ogrlic lahko sestavimo'''
    if b==0: return 1
    if r==0: return 1
    return stevilo_ogrlic(b-1, r) + stevilo_ogrlic(b, r-1)

# =====================================================================@010383=
# 3. podnaloga
# Sestavite generator `ogrlice(b, r)`, ki zaporedoma generira vse nize,
# ki predstavljajo ogrlice, sestavljene iz `b` belih in `r` rdečih kroglic.
# Generator naj nize vrača v abecednem vrstnem redu.
# 
#     >>> for ogrlica in ogrlice(2, 2):
#     ...     print(ogrlica)
#     BBRR
#     BRBR
#     BRRB
#     RBBR
#     RBRB
#     RRBB
# =============================================================================


def ogrlice(b,r):
    '''generator'''
    if b==0 or r==0:
        yield 'B'*b + 'R'*r
    else:
        for ogrlica in ogrlice(b-1,r):
            yield 'B' + ogrlica
        for ogrlica in ogrlice(b, r-1):
            yield 'R' + ogrlica

