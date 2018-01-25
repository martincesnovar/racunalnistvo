# =============================================================================
# Vlečenje vrvi
#
# Udeleženci piknika bodo vlekli vrv. So različnih spolov, starosti in
# mas, zato sprva niso vedeli, kako bi se pravično razdelili v dve
# skupini. Sklenili so, da je najpravičnejša razdelitev takšna, da bosta
# imeli obe skupini enako skupno težo, na število članov skupin pa se
# sploh ne bodo ozirali. Včasih dveh skupin s popolnoma enakima masama
# ni mogoče sestaviti, zato iščejo takšno razdelitev, da bo razlika med
# masama skupin čim manjša. Vsak udeleženec nam je zaupal svojo  maso v
# kilogramih in sicer jo je zaokrožil na najbližje celo število.
# =====================================================================@010512=
# 1. podnaloga
# Sestavite funkcijo `razdeli(mase)`, ki dobi seznam mas udeležencev in
# vrne skupno maso manjše od skupin pri najbolj pravični delitvi. Ta funkcija
# naj bo rekurzivna in naj pregleda vse možnosti. (Kaj so vse možnosti in
# koliko jih je?) Zgled:
# 
#     >>> razdeli([95, 82, 87, 102, 75])
#     197
# 
# _Komentar_: Najbolj pravično razdelitev dosežemo, če damo udeleženca
# z masama 102 in 95 skupaj, vsi ostali pa tvorijo drugo skupino.
# =============================================================================
def razdeli(mase):
    '''Vrne vsoto mase manjše skupine.'''
    skupaj = sum(mase)
    def sestavi_nahrbtnik(l, m):
        """Za udeleženca se odločimo, ali ga bomo dodali v skupino ali
        ne, izberem boljšo možnost. Vrnem maso"""
        if l == len(mase):
            return m
        m_z = sestavi_nahrbtnik(l + 1, m + mase[l])  # Ga vzamemo v skupino.
        m_brez = sestavi_nahrbtnik(l + 1, m)  # Ga ne vzamemo v skupino.
        if abs((skupaj - m_z) - m_z) < abs((skupaj - m_brez) - m_brez):
            return m_z
        else:
            return m_brez
    resitev = sestavi_nahrbtnik(0, 0)
    return min(resitev, skupaj - resitev)

def razdeli_v(mase):
    '''Vrne vsoto mase večje skupine.'''
    skupaj = sum(mase)
    def sestavi_nahrbtnik(l, m):
        """Za udeleženca se odločimo, ali ga bomo dodali v skupino ali
        ne, izberem boljšo možnost. Vrnem maso"""
        if l == len(mase):
            return m
        m_z = sestavi_nahrbtnik(l + 1, m + mase[l])  # Ga vzamemo v skupino.
        m_brez = sestavi_nahrbtnik(l + 1, m)  # Ga ne vzamemo v skupino.
        if abs((skupaj - m_z) - m_z) < abs((skupaj - m_brez) - m_brez):
            return m_z
        else:
            return m_brez
    resitev = sestavi_nahrbtnik(0, 0)
    return max(resitev, skupaj - resitev)
# =====================================================================@010513=
# 2. podnaloga
# Če zgornjo rešitev preizkusite na seznamih dolžine 25 ali več, boste
# ugotovili, da deluje izjemno počasi. Kakšna je njena časovna zahtevnost?
# 
# Nalogo bomo rešili še z dinamičnim programiranjem. Gre za tako imenovani
# _problem 0-1 nahrbtnika_. Izkoristili bomo dejstvo, da mase ljudi ne
# morejo biti poljubno velike (največja dokumentirana masa človeka je 635 kg)
# in da so celoštevilske. Pri sestavljanju skupin lahko dosežemo enako
# maso na različne načine.
# 
# Sestavite funkcijo `razdeli_dinamicno(mase)`, ki naredi isto kot prejšnja
# funkcija, le da se reševanja tokrat lotite z dinamičnim programiranjem.
# Zgled:
# 
#     >>> razdeli_dinamicno([95, 82, 87, 102, 75])
#     197
# 
# Funkcijo preizkusite na seznamu dolžine 50 in na seznamu dolžine 100.
# =============================================================================
def razdeli_dinamicno(mase):
    '''Vrne vsoto mas.'''
    skupaj = sum(mase)
    nahrbtnik = [False for i in range(skupaj + 1)]
    nahrbtnik[0] = True
    for m in mase:
        for i in range(skupaj - m, -1, -1):
            if nahrbtnik[i]:
                nahrbtnik[i+m] = True
    p = skupaj // 2
    while not nahrbtnik[p]:
        p -= 1
    return p
# =====================================================================@010514=
# 3. podnaloga
# Prejšnja funkcija nam izračuna velikost skupine, nič pa ne izvemo o tem,
# kdo so udeleženci, ki tvorijo to skupino. Sestavite še funkcijo
# `razdeli_udelezence(mase)`, ki vrne seznam mas udeležencev, ki bodo
# tvorili manjšo od obeh skupin. Če je rešitev več, lahko funkcija vrne
# katerekoli rešitev. Zgled:
# 
#     >>> razdeli_udelezence([95, 82, 87, 102, 75])
#     [102, 95]
# 
# _Namig:_ Predelajte prejšnjo funkcijo, tako da bo iz nahrbtnika razvidno,
# kateri udeleženci morajo biti v skupini.
# =============================================================================
def razdeli_udelezence(mase):
    '''Vrne mase manjše skupine.'''
    skupaj = sum(mase)
    nahrbtnik = [False for i in range(skupaj + 1)]
    masa = [None for i in range(skupaj + 1)]
    nahrbtnik[0] = True
    for m in mase:
        for i in range(skupaj - m, -1, -1):
            if nahrbtnik[i] and not nahrbtnik[i+m]:
                nahrbtnik[i+m] = True
                masa[i+m] = m
    p = skupaj // 2
    while not nahrbtnik[p]:
        p -= 1
    rez = []
    while masa[p] is not None:
        rez.append(masa[p])
        p -= masa[p]
    return rez

def razdeli_udelezence_tezji(mase):
    '''Vrne mase večje skupine pri čimbolj enakomerni delitvi.'''
    skupaj = sum(mase)  # Skupna masa vseh.

    nahrbtnik = [False for i in range(skupaj + 1)]
    masa = [None for i in range(skupaj + 1)]
    nahrbtnik[0] = True
    for m in mase:
        for i in range(skupaj - m, -1, -1):
            if nahrbtnik[i] and not nahrbtnik[i+m]:
                nahrbtnik[i+m] = True
                masa[i+m] = m

    p = skupaj // 2
    while not nahrbtnik[p]:
        p += 1
    ret = []
    while masa[p] != None:
        ret.append(masa[p])
        p -= masa[p]
    return ret

