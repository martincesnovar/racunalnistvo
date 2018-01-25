# =============================================================================
# Mafija
#
# V neki mafijski organizaciji so člani urejeni hierarhično. Vsakdo razen
# botra (vrhovnega šefa) ima natanko enega nadrejenega. Vsak mafijec ima
# lahko pod seboj največ dva podrejena (levega in desnega).
# Mafijci morajo zbirati denar s kriminalnimi dejavnostmi. Tisti, ki imajo
# podrejene, pa ga poleg tega poberejo še od svojih podrejenih. Ves
# “prisluženi” in prejeti denar morajo oddati svojemu nadrejenemu.
# 
# Boter je posumil, da nekateri člani goljufajo. Nekaj denarja, ki ga poberejo
# od podrejenih, zadržijo zase. Od vsakega člana je pridobil podatek o tem,
# koliko denarja je oddal naprej ter si podatke shranil v drevo, v katerih
# so podatki pari imena in količine oddanega denarja. Na primer:
# 
#     mafija = Drevo(('Salvatore', 320),
#                    levo=Drevo(('Bernardo', 200),
#                               levo=Drevo(('Matteo', 50)),
#                               desno=Drevo(('Carlo', 100),
#                                           levo=Drevo(('Rosalia', 70)),
#                                           desno=Drevo(('Tommaso', 50)))),
#                    desno=Drevo(('Francesco', 120),
#                                levo=Drevo(('Giuseppe', 70)),
#                                desno=Drevo(('Antonio', 60))))
# =====================================================================@010476=
# 1. podnaloga
# Botra zanima, koliko denarja zaradi goljufov “ponikne”. Želi, da
# sestavite funkcijo `koliko_ponikne(drevo)`, ki vrne skupno vsoto denarja,
# ki ponikne. Primer:
# 
#     >>> koliko_ponikne(mafija)
#     30
# =============================================================================


from sklad import Sklad

def pregled_po_skladu(zacetno_drevo):
    '''pregleda drevo s skladom'''
    sklad = Sklad()
    sklad.vstavi(zacetno_drevo)
    while not sklad.prazen():
        drevo = sklad.poberi()
        if not drevo.prazno:
            sklad.vstavi(drevo.levo)
            sklad.vstavi(drevo.desno)
            yield drevo.podatek
# =====================================================================@010477=
# 2. podnaloga
# Ko je boter dognal, koliko denarja ponikne, je totalno po████. Pri
# priči hoče imeti imena vseh goljufov! Napišite funkcijo `goljufi(drevo)`,
# ki vrne množico goljufov. Vsak goljuf naj bo predstavljen z naborom.
# Prva kompotenta naj bo ime goljufa, druga komponenta pa količina denarja,
# ki ga je utajil. Primer:
# 
#     >>> goljufi(mafija)
#     {(’Carlo’, 20), (’Francesco’, 10)}
# =============================================================================



def goljufi(mafija):
    '''vrne množico goljufov'''
    if mafija.prazno:
        return set()
    ukradel = max(denar(mafija.levo) + denar(mafija.desno) - denar(mafija),0)

    return ({(mafija.podatek[0], ukradel)} if ukradel > 0 else set()) | goljufi(mafija.levo) | goljufi(mafija.desno)

# =====================================================================@010478=
# 3. podnaloga
# Botru se dozdeva, da so najbolj pridne _majhne ribe_. To so tisti mafijci,
# ki nimajo pod seboj nobenega podrejenega. Tistim, ki imajo podrejene, se
# reče _velike ribe_. Napišite funkcijo `zasluzek(drevo)`, ki vrne par (nabor)
# dveh števili, pri čemer je:
# 
# * prvo število skupna vsota denarja, ki ga zaslužijo majhne ribe;
# * drugo število skupna vsota denarja, ki ga zaslužijo velike ribe (brez
#   pobirkov od podrejenih).
# 
# Primer:
# 
#     >>> zasluzek(mafija)
#     (300, 50)
# =============================================================================


def zasluzek(mafija):
    '''vrne nabor, koliko zaslužijo majhne ribe in koliko velike'''
    if mafija.prazno:
        return (0,0)
    ukradel = max(denar(mafija) - denar(mafija.levo) - denar(mafija.desno) ,0)
    l_mala, l_velika = zasluzek(mafija.levo)
    d_mala, d_velika = zasluzek(mafija.desno)
    m, v = l_mala + d_mala, l_velika + d_velika
    
    if mafija.levo.prazno and mafija.desno.prazno: #gre za "majhno ribo"
        m += mafija.podatek[1]
    else:
        v += ukradel
    return m, v
