# =============================================================================
# Plače
#
# V nekem uspešnem slovenskem podjetju so zaposleni urejeni hierarhično. Vsakdo
# razen direktorja ima natanko enega nadrejenega. Vsak uslužbenec ima lahko pod
# seboj največ dva podrejena (levega in desnega). Primer takšne hierarhije (številke
# so njihove plače):
# 
#     lucka = Drevo(('Lučka', 800), levo=Drevo(('Peter', 900)), desno=Drevo(('Tadeja', 700)))
#     matjaz = Drevo(('Matjaž', 1100), levo=Drevo(('Simona', 700)), desno=Drevo(('Boris', 1000), levo=lucka))
#     branko = Drevo(('Branko', 900), desno=Drevo(('Benjamin', 1100)))
#     ales = Drevo(('Aleš', 1500), levo=matjaz, desno=branko)
# 
# V tem podjetju imajo zelo močen sindikat. Sindikalisti so ugotovili, da višine
# plač niso pravične. Nedopustno je, da imajo nekateri podrejeni višje plače od
# svojih nadrejenih! Zato sindikat zahteva, da mora imeti vsak zaposleni vsaj za
# 100 € višjo plačo od kateregakoli svojega podrejenega.
# 
# Direktor bi rad analiziral podatke, preden se spusti v pogajanja s sindikalisti.
# Podatke o plačah zaposlenih je shranil v dvojiško drevo, v katerem so v
# vozliščih shranjeni pari z imeni in plačami zaposlenih.
# =====================================================================@010479=
# 1. podnaloga
# Direktorja zanima, koliko dodatnega denarja bi potreboval vsak mesec, če bi
# ugodil zahtevam sindikata. Želi, da sestavite funkcijo `odprava_krivic(sef)`,
# ki vrne skupno vsoto denarja, ki bi ga potreboval za odpravo krivic. Primer
# (če `d` ustreza zgornji sliki):
# 
#     >>> odprava_krivic(d)
#     700
# 
# _Komentar:_ Lučka bi po novem prejemala 1000 €, ker dobiva Peter 900 €.
# Zaradi Lučke bi moral Boris prejemati 1100 €. Zaradi Borisa pa bi moral
# Matjaž prejemati 1200 €. Branko bi zaradi Benjamina moral prejemati 1200 €.
# Vsota vseh povišic znaša 700 €.
# 
# _Komentar 2:_ ne pozabite, da se plače nikomur ne znižajo. Torej če imata podrejena
# plačo 800 in 900, šef pa 1500 in se recimo zgodi, da bosta podrejena po novem imela
# plači 850 in 1100, bo šef obdržal plačo 1500 (in ne dobil recimo plačo 1200)
# =============================================================================
from dvojisko_drevo import *

def vsota_plac(d):
    '''vrne skupno vsoto denarja, ki bi ga potreboval za odpravo krivic'''
    vsota = 0
    if d.prazno:
        return 0, float('-inf')
    popravki_levo, levo_vsota = vsota_plac(d.levo)
    popravki_desno, desno_vsota = vsota_plac(d.desno)
    nova_placa = max(d.podatek[1], max(levo_vsota, desno_vsota ) + 100)
    return popravki_levo + popravki_desno + (nova_placa - d.podatek[1]), nova_placa

def odprava_krivic(d):
    '''Vrne vsoto vseh povišic.'''
    povisice, _ = vsota_plac(d)
    return povisice

# =====================================================================@010480=
# 2. podnaloga
# Direktor bi sindikaliste rad prepričal, da se razburjajo po nepotrebnem.
# Rad bi imel seznam imen vseh tistih uslužbencev, ki bi prejeli povišice.
# (Od vseh takih bo namreč pridobil pisne izjave, da so zadovoljni s svojo
# plačo.) Napišite funkcijo `pisne_izjave(sef)`, ki vrne množico imen vseh
# zaposlenih, ki bi prejeli povišico. Primer:
# 
#     >>> pisne_izjave(d)
#     {'Lučka', 'Boris', 'Branko', 'Matjaž'}
# =============================================================================

def imena_p(d):
    '''vrne imena'''
    if d.prazno:
        return set(), float('-inf')
    iml, pl = imena_p(d.levo)
    imd, pd = imena_p(d.desno)
    nov = max(d.podatek[1], max(pl,pd)+100)
    return imd|iml|({d.podatek[0]} if nov > d.podatek[1] else set()), nov

def pisne_izjave(d):
    '''vrne mnozico tistih, ki se bodo odpovedali visji placi'''
    imena, _ = imena_p(d)
    return imena


# =====================================================================@010481=
# 3. podnaloga
# Po večtedenskih pogajanjih s sindikatom je imel direktor poln k███ vsega,
# zato je udaril po mizi! Odločil se je, da bo najprej vsem plače zmanjšal
# na "minimalce", potem pa bo povišal plače na način, ki ga predlaga sindikat.
# Tako bo volk sit in koza cela. Napišite funkcijo `uravnilovka(sef)`, ki vrne
# skupno vsoto denarja, ki bi ga na ta način prihranil vsak mesec (glede na
# trenutne plače). "Minimalec" znaša 500 €. Primer:
# 
#     >>> uravnilovka(d)
#     3100
# =============================================================================

def vsota(d):
    '''Vrne vsoto vseh plač v drevesu'''
    if d.prazno:
        return 0
    return d.podatek[1] + vsota(d.levo) + vsota(d.desno)

def minimalci(d):
    '''Vrne par števil, kjer je prvi vsota minimalnih plač, druga nova plača'''
    if d.prazno:
        return 0, 400
    vl, pl = minimalci(d.levo)
    vd, pd = minimalci(d.desno)
    return vl + vd + max(pl, pd) + 100, max(pl,pd) + 100

def uravnilovka(d):
    '''Vrne količino denarja po uravnilovki'''
    prihranjen, _ = minimalci(d)
    return vsota(d) - prihranjen

