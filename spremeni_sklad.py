from sklad import Sklad

def odstrani_naj_sklad(s):
    '''Odstrani najkrajši niz iz sklada
    če je takih elementov več odstrani le vrhnjega'''
    dolzina = float('inf')
    sk = Sklad() #pomožni sklad
    prvi = True
    while not s.prazen():
        niz = s.vrh()
        dolzina = min(len(niz),dolzina)
        s.odstrani()
        sk.vstavi(niz)
    while not sk.prazen():
        niz = sk.vrh()
        sk.odstrani()
        s.vstavi(niz)
    while not s.prazen():
        if prvi and len(s.vrh()) == dolzina:
            prvi = False
        else:
            sk.vstavi(s.vrh())
        s.odstrani()
    while not sk.prazen():
        s.vstavi(sk.vrh())
        sk.odstrani()
    return

