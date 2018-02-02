from sklad import Sklad
from dvojisko_drevo import Drevo
from vrsta import Vrsta
 
def je_lahko_BST(pre):
    '''preveri ali premi pregled lahko predstavlja dvojiško iskalno drevo'''
    s = Sklad()
    koren = float('-inf')
    for vrednost in pre: 
        if vrednost < koren :
            return False
        while not s.prazen() and s.vrh() < vrednost :
            koren = s.vrh()
            s.odstrani()
        s.vstavi(vrednost)
    return True

def indeks(premi):
    '''Vrne indeks, kjer je 1. večji element od korena'''
    if len(premi)==0:
        return
    koren = premi[0]
    for i, e in enumerate(premi):
        if koren < e:
            return i
    return len(premi)

def konstruiraj(premi):
    '''iz premega pregleda vrne iskalno dvojiško drevo, če obstaja'''
    if len(premi) == 0:
        return Drevo()
    if len(premi) == 1:
        return Drevo(premi[0])
    if not je_lahko_BST(premi):
        raise Exception('Ni iskalno drevo')
    i = indeks(premi)
    levi = konstruiraj(premi[1:i])
    desni = konstruiraj(premi[i:])
    return Drevo(premi[0], levo=levi,desno=desni)

def obrni_sode(vrsta):
    '''v vrsti obrne sode elemente, lihe pusti pri miru'''
    sklad = Sklad()
    vrsta.vstavi(None)
    while vrsta.zacetek() is not None:
        if vrsta.zacetek() % 2 == 1:
            vrsta.vstavi(vrsta.zacetek())
        if vrsta.zacetek() % 2 == 0:
            sklad.vstavi(vrsta.zacetek())
            vrsta.vstavi('')
        vrsta.odstrani()
    vrsta.vstavi(vrsta.zacetek())
    vrsta.odstrani()
    while vrsta.zacetek() is not None:
        if vrsta.zacetek() == '':
            vrsta.odstrani()
            vrsta.vstavi(sklad.vrh())
            sklad.odstrani()
        else:
            vrsta.vstavi(vrsta.zacetek())
            vrsta.odstrani()
    vrsta.odstrani()
    return
    
