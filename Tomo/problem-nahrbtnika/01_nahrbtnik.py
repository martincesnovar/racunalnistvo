# =============================================================================
# 0/1 nahrbtnik
#
# Pri reševanju problema 0/1 nahrbtnika imamo opravka z množicami $S_i$ in $Z_i$.
# Predstavili jih bomo s seznami parov, ki so urejeni naraščajoče po prvih komponentah.
# =====================================================================@010501=
# 1. podnaloga
# Sestavi funkcijo `preveri(s)`, ki za parameter `s` dobi seznam parov.
# Funkcija naj ugotovi, ali ta seznam lahko (teoretično) predstavlja
# neko množico $S$ za nek problem 0/1 nahrbtnika.
# 
#     >>> preveri([(0,0),(3,7),(4,9),(8,12),(11,17),(20,33)])
#     True
# =============================================================================

def preveri(s):
    '''Preveri ali lahko seznam teoretično predstavlja problem 01 nahrbtnika
    s = [(0,0),(x,y),....]'''
    if s==[] or (0,0) != s[0]:
        return False
    for i in range(1, len(s)):
        if s[i-1][0]>= s[i][0]: return False
        if s[i-1][1]>= s[i][1] < 0: return False
    return True

# =====================================================================@010502=
# 2. podnaloga
# Sestavi funkcijo `sestaviZ(s, predmet)`, ki za neko množico $S_i$ in predmet,
# podan s parom `(velikost, vrednost)`, sestavi in vrne množico $Z_{i+1}$.
# 
#     >>> sestaviZ([(0,0),(1,1),(2,2),(3,3)], (4,4))
#     [(4,4),(5,5),(6,6),(7,7)]
# =============================================================================
def sestaviZ(s, predmet):
    '''Sestavi množico z'''
    vel,vred = predmet
    sez = []
    for veli,vre in s:
        sez.append((vel+veli,vred+vre))
    return sez
        
# =====================================================================@010503=
# 3. podnaloga
# Sestavi funkcijo `sestaviS(s, z)`, ki iz množic $S_i$ in $Z_{i+1}$
# sestavi in vrne množico $S_{i+1}$.
# 
#     >>> sestaviS([(0,0),(11,6),(40,9),(51,15)], [(16,4),(27,10),(56,13),(67,19)])
#     [(0,0),(11,6),(27,10),(51,15),(67,19)]
# 
# Bi lahko kaj "poenostavil", če bi poznal velikost nahrbtnika?
# =============================================================================
def sestaviS(s, z):
    '''Sestavi in vrne množico S(i+1)'''
    sez = []
    n = len(s)
    m = len(z)
    i=j=0
    while i < n and j < m:
        if s[i][0] <z[j][0]: #napišemo tistega z manjšo komponento
            sez.append(s[i])
            i+=1
        elif s[i][0] > z[j][0]:
            sez.append(z[j])
            j += 1
        else: #enaka komponenta, tistega z večjo vrednostjo
            if s[i][1] > z[j][1]:
                sez.append(s[i])
            else:
                sez.append(z[j])
            i += 1
            j += 1
        #preskočimo elemente s premajhno komponento
        while i < n and s[i][1] <= sez[-1][1]:
            i += 1
        while j < m and z[j][1] <= sez[-1][1]:
            j += 1
    #dodamo še preostanek
    sez += s[i:]
    sez += z[j:]

    return sez
    
# =====================================================================@010504=
# 4. podnaloga
# Sestavi funkcijo `mnoziceS(predmeti)`, ki za dani seznam predmetov,
# pri čemer je vsak predmet predstavljen s parom `(velikost, vrednost)`,
# sestavi in vrne seznam vseh množic $S$.
# 
#     >>> mnoziceS([(2,3),(4,5),(4,7),(6,8)])
#     [[(0,0)],[(0,0),(2,3)],[(0,0),(2,3),(4,5),(6,8)],[(0,0),(2,3),(4,7),
#        (6,10),(8,12),(10,15)],[(0,0),(2,3),(4,7),(6,10),(8,12),(10,15),
#        (12,18),(14,20),(16,23)]]
# =============================================================================

def mnoziceS(predmeti):
    '''Vrne množice vseh elementov'''
    sez = [[(0,0)]]
    for predmet in predmeti:
        z = sestaviZ(sez[-1],predmet)
        sez.append(sestaviS(sez[-1],z))
    return sez

# =====================================================================@010505=
# 5. podnaloga
# Sestavi funkcijo `nahrbtnik01(predmeti, velikost)`, ki reši problem
# 0/1 nahrbtnika, kjer je `predmeti` seznam predmetov, predstavljen kot prej,
# `velikost` pa velikost nahrtnika. Funkcija naj vrne skupno velikost in vrednost
# predmetov, ki jih damo v nahrbtnik.
# 
#     >>> nahrbtnik01([(2,3),(4,5),(4,7),(6,8)], 9)
#     (8,12)
# =============================================================================

def nahrbtnik01(sez, velikost):
    '''Sestavi nahrbtnik'''
    s = mnoziceS(sez)[-1]
    i=0
    while i <len(s) and s[i][0] <= velikost:
        i+=1
    return s[i-1]

# =====================================================================@010506=
# 6. podnaloga
# Sestavi funkcijo `resitev01(predmeti, velikost)`, ki reši problem 0/1
# nahrbtnika kot pri prejšnji podnalogi, le da vrne seznam ničel in enic,
# ki določajo, katere predmete moramo izbrati. Če je rešitev več, naj vrne
# katerokoli izmed njih.
# 
#     >>> resitev01([(2,3),(4,5),(4,7),(6,8)], 9)
#     [0, 1, 1, 0]
# =============================================================================

def resitev01(predmeti, velikost):
    '''Vrne seznam vrednosti elementov, ki jih dodamo v nahrbtnik'''
    s = mnoziceS(predmeti)
    n = len(predmeti)
    sez = [0]*n
    i=0
    while i < len(s[-1]) and s[-1][i][0] <= velikost:
        i += 1
        vel, cena = s[-1][i - 1]
    for k in range(len(predmeti) - 1, -1, -1):
        #zmanjšamo velikost in ceno elementov
        vel0 = vel - predmeti[k][0]
        cena0 = cena - predmeti[k][1]
        if (vel0, cena0) in s[k]:
            sez[k] = 1
            vel, cena = vel0, cena0
    return sez

# =====================================================================@010507=
# 7. podnaloga
# Sestavi funkcijo `resitve01(predmeti, velikost)`, ki reši problem 0/1
# nahrbtnika kot pri prejšnji podnalogi, le da vrne seznam vseh možnih rešitev.
# Vrstni red rešitev v seznamu ni pomemben.
# 
#     >>> resitve01([(2,4),(4,5),(4,7),(6,8)], 9)
#     [[0, 1, 1, 0], [1, 0, 0, 1]]
# =============================================================================

def pomozna(predmeti, s, n, v, c):
    if n == 0:
        return [[]]
    v0 = v - predmeti[n - 1][0]
    c0 = c - predmeti[n - 1][1]
    resitve = []

    if (v, c) in s[n - 1]:
        resitve0 = pomozna(predmeti, s, n - 1, v, c)
        for resitev in resitve0:
            resitev.append(0)
        resitve += resitve0

    if (v0, c0) in s[n - 1]:
        v, c = v0, c0
        resitve1 = pomozna(predmeti, s, n - 1, v0, c0)
        for resitev in resitve1:
            resitev.append(1)
        resitve += resitve1

    return resitve

def resitve01(predmeti, velikost):
    '''poiščemo optimalno rešitev'''
    s = mnoziceS(predmeti)
    i = 0
    while i < len(s[-1]) and s[-1][i][0] <= velikost:
        i += 1
    v, c = s[-1][i - 1]

    return pomozna(predmeti, s, len(predmeti), v, c)

# =====================================================================@010508=
# 8. podnaloga
# Sestavi funkcijo `resitev0n(predmeti, velikost)`, ki reši malo spremenjen
# problem nahrbtnika. Vzamemo lahko več enakih predmetov, koliko posameznih
# predmetov imamo na voljo pa je dodano pri opisu posameznega predmeta.
# Namesto para (velikost, cena) imamo torej trojko (velikost, cena, količina).
# Funkcija naj vrne seznam celih števil, ki določajo, koliko katerih predmetov
# moramo vzeti. Če je rešitev več, naj vrne katerokoli izmed njih.
# Namig: pretvori problem na običajen problem 0/1 nahrbtnika.
# 
#     >>> resitev0n([(2,3,2),(4,5,3),(4,7,1),(6,8,2)], 15)
#     [2, 0, 1, 1]
# =============================================================================

def resitev0n(predmeti, velikost):
    '''pretvori poseben 01 nahrbtnik v običajnega'''
    sez = []
    for v, c, k in predmeti:
        for i in range(k):
            sez.append((v, c))

    resitev = resitev01(sez, velikost) #prevedemo na običajen 01 nahrbtnik

    rez = []
    i = 0
    for v, c, k in predmeti:
        rez.append(sum(resitev[i:i+k]))
        i += k
    return rez
