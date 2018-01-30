from Vozel import *

def preveri_vsebovanost(v, w):
    '''preveri ali je v_s vsebovan v v_s1
    Naloga 2012/13-1.1'''
    if v is None: return True #v je vsebovan v w
    if w is None: return False #ne vsebuje
    if v.vrniPodatek() == w.vrniPodatek():
        #če se v obeh ujemata gremo v obeh naprej
        return preveri_vsebovanost(v.vrniNasled(), w.vrniNasled())
    else:
        #preverimo, če se naslednji ujema
        return preveri_vsebovanost(v, w.vrniNasled())
    
if __name__ == '__main__':
    v=Vozel('A',Vozel('B',Vozel('C',Vozel('D',Vozel('E')))))
    w=Vozel('A',Vozel('G',Vozel('D',Vozel('C',Vozel('B',Vozel('F',Vozel('E')))))))
    ww = Vozel('A',Vozel('G',Vozel('B',Vozel('C',Vozel('D',Vozel('E',Vozel('F')))))))
    print(preveri_vsebovanost(v,w)) #False
    print(preveri_vsebovanost(v,ww)) #True
