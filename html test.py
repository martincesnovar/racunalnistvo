from sklad import Sklad

def znacke(ime_dat):
    return [('html',1),('head',1),('head',2),('body',1),('img',3),('br',3),('body',2),('html',2)]

def preveri_HTML(ime_dat=''):
    '''preveri ali je html datoteka pravilno sestavljena'''
    s = Sklad()
    for znacka, st in znacke(ime_dat):
        if st == 1:
            s.vstavi((znacka,st))
        if st == 2:
            if s.prazen() or znacka!= s.vrh()[0]:
                return False
            s.odstrani()
    return s.prazen()            
