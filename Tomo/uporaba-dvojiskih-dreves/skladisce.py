# =============================================================================
# Skladišče
#
# Neko podjetje ima skladišče svojih izdelkov organizirano v obliki drevesne
# strukture. Skladišče je sestavljeno iz več prostorov (vozlišč), vhod v
# skladišče je samo en (pri korenu), iz vsakega prostora pa vodita hodnika do
# največ dveh drugih prostorov (levo in desno poddrevo).
# 
# Oznaka prostora je kar opis poti, kako pridemo od vhoda do ustreznega
# prostora, pri čemer črka `L` pomeni levi hodnik, črka `D` pa desni hodnik.
# Oznaka `DLD` tako pomeni, da pri vhodu zavijemo desno, v naslednjem
# prostoru levo in nato še enkrat desno. V vhodu izdelkov ne hranimo.
# 
# Skladiščnik Stanko je pri zlaganju škatel z izdelki izjemno sistematičen, saj
# da novo škatlo vedno desno od zadnje škatle. Pri pobiranju pa Stanko malo bolj
# improvizira. Če v zadnjo sobo zavije na levo, bo tudi pobral najbolj levo
# škatlo, torej prvo, ki jo je odložil (tako kot pri vrsti). Če pa v zadnjo sobo
# zavije na desno, pa bo pobral najbolj desno, torej tisto, ki jo je odložil
# nazadnje (tako kot pri skladu).
# 
# Če bo v škatli več izdelkov, kot jih je treba, bo preostanek odložil nazaj na
# desno, če pa jih bo premalo, bo odprl še naslednjo škatlo. Če v sobi izdelkov
# ne bo dovolj, bo stvari pustil pri miru, vendar bo težavo zapisal v končno
# poročilo.
# =====================================================================@011432=
# 1. podnaloga
# Napišite funkcijo `stanko(narocila, porocilo)`, ki iz datoteke z imenom
# `narocila` prebere podatke o oznaki, cilju ter količini izdelkov (pozitivno
# za dobavo in negativno za naročilo), nato pa v datoteko z imenom `porocilo`
# najprej izpiše vsa naročila, ki jih ni mogel izvesti, na dnu pa še končno
# stanje v skladišču, urejeno po prostorih, kot si sledijo pri premem pregledu.
# V izpis naj vključi tudi vse prazne prostore, preko katerih dostopamo do
# nepraznih prostorov. Če so bila vsa naročila uspešno izvedena, naj program
# izpiše le končno stanje.
# 
# Na primer, za datoteko `narocila.txt` z vsebino
# 
#     D1 LL 2
#     D2 LD 3
#     D3 D 2
#     D4 D 4
#     N1 LL -3
#     N2 D -1
#     D5 D 1
#     D6 LL 4
#     N3 LL -1
# 
# naj `stanko('narocila.txt', 'porocilo.txt')` v datoteko `porocilo.txt` zapiše:
# 
#     OPOZORILA:
#     Naročilo N1: V prostoru LL je premalo izdelkov
# 
#     KONČNO STANJE:
#     L: /
#     LL: 1, 4
#     LD: 3
#     D: 2, 3, 1
# 
# Namig: kljub temu, da je treba napisati le eno funkcijo, bo dobro, če jo
# razbijete na pomožne funkcije.
# =============================================================================

from dvojisko_drevo import Drevo
from vrsta import Vrsta
from sklad import Sklad

# 8 pomožnih funkcij

def preberi_narocila_iz_dat(narocila_dat):
    '''prebere datoteko'''
    narocila = []
    with open(narocila_dat, 'r') as f:
        for vrstica in f:
            oznaka, pot, kolicina = vrstica.split()
            narocila.append((oznaka, pot, int(kolicina)))
    return narocila

def vzemi_vrsta(vrsta, kolicina):
    '''iz vrste vzame število izdelkov ali vrže izjemo'''
    vr = Vrsta()
    odv_kol = 0
    while odv_kol < kolicina and not vr.prazna():
        vr.vstavi(vrsta.zacetek())
        vrsta.odstrani()
        odv_kol += vr.zacetek()
    if odv_kol > kolicina:
        vrsta.vstavi(odv_kol-kolicina)
    elif odv_kol < kolicina:
        while not vr.prazna():
            vrsta.vstavi(vr.zacetek())
            vr.odstrani()
        raise IndexError

def vzemi_sklad(sklad, kolicina):
    '''iz sklada vzame število izdelkov ali vrže izjemo'''
    pom = Sklad()
    odv_kol = 0
    while odv_kol < kolicina and not sklad.prazen():
        pom.vstavi(sklad.vrh())
        sklad.odstrani()
        odv_kol += pom.vrh()
    if odv_kol > kolicina:
        sklad.vstavi(odv_kol - kolicina)
    elif odvzeta_kolicina < kolicina:
        while not pom.prazen():
            sklad.vstavi(pom.vrh())
            pom.odstrani()
        raise IndexError

def poisci_sobo(skladisce, pot, smer=None):
    '''Vrne iskano sobo ter skladišče s po potrebi dodanimi praznimi sobami.'''
    if skladisce.prazno:
        if smer == 'L':
            skladisce = Drevo(Vrsta())
        elif smer == 'D':
            skladisce = Drevo(Sklad())
    if pot == '':
        return skladisce, skladisce.podatek
    elif pot[0] == 'L':
        levo_skladisce, soba = poisci_sobo(skladisce.levo, pot[1:], smer='L')
        return Drevo(skladisce.podatek, levo=levo_skladisce, desno=skladisce.desno), soba
    elif pot[0] == 'D':
        desno_skladisce, soba = poisci_sobo(skladisce.desno, pot[1:], smer='D')
        return Drevo(skladisce.podatek, levo=skladisce.levo, desno=desno_skladisce), soba

def vzemi_iz_sobe(soba, kolicina):
    '''Vzame elemente iz sobe'''
    if isinstance(soba, Vrsta):
        vzemi_vrsta(soba, kolicina)
    elif isinstance(soba, Sklad):
        vzemi_sklad(soba, kolicina)

def izvedi_narocilo(skladisce, oznaka, pot, kolicina):
    '''Spremeni stanje sob in vrne po potrebi razširjeno skladišče.'''
    skladisce, soba = poisci_sobo(skladisce, pot)
    if kolicina > 0:
        soba.vstavi(kolicina)
    elif kolicina < 0:
        vzemi_iz_sobe(soba, -kolicina)
    return skladisce


def pregled_skladisca(skladisce, smer = None):
    '''Pregleda skladišče'''
    if not skladisce.prazno:
        soba = skladisce.podatek
        vs = []
        if smer == 'L':
            while not soba.prazna():
                vs.append(soba.zacetek())
                soba.odstrani()
        elif smer == 'D':
            while not soba.prazen():
                vs.append(soba.vrh())
                soba.odstrani()
            vs.reverse()
        yield '', vs
        for soba, vs in pregled_skladisca(skladisce.levo, smer ='L'):
            yield 'L' + soba, vs
        for soba, vs in pregled_skladisca(skladisce.desno, smer = 'D'):
            yield 'D' + soba, vs

def porocilo_zapisi(ime_dat, opozorila, skladisce):
    '''Na datoteko izpisi porocilo'''
    with open(ime_dat, 'w') as f:
        if opozorila:
            print('OPOZORILA: ', file = f)
        print(file=f)
        print('KONCNO STANJE:', file = f)
        for skladisce, smer in [(skladisce.levo, 'L'), (skladisce.desno, 'D')]:
            for soba, vsebina_sobe in pregled_skladisca(skladisce, smer=smer):
                print('{}{}: {}'.format(smer, soba, ', '.join(map(str, vsebina_sobe)) if vsebina_sobe else '/'), file=f)
    return


def stanko(narocila, porocilo):
    '''v datoteko porocilo zapise opozorila'''
    skladisce = Drevo(None)
    napake = []
    for (oznaka, pot, kolicina) in preberi_narocila_iz_dat(narocila):
        try: skladisce = izvedi_narocilo(skladisce, oznaka, pot, kolicina)
        except IndexError:
            napake.append('Naročilo {}: V prostoru {} je premalo izdelkov'.format(oznaka, pot))
    porocilo_zapisi(porocilo, napake, skladisce)


