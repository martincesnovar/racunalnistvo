from dvojisko_drevo import Drevo

def je_iskalno(drevo):
    ''' Vrne ali je dvojiško drevo iskalno.'''
    return je_iskalno_drevo_rek(drevo, mini=float('-inf'), maxi=float('inf'))


def je_iskalno_drevo_rek(drevo, mini, maxi):
    '''mini < drevo.podatek < maxi'''
    if drevo.prazno:
        return True
    
    if drevo.podatek < mini or drevo.podatek > maxi:
        return False

    return (je_iskalno_drevo_rek(drevo.levo, mini, drevo.podatek-1) and
          je_iskalno_drevo_rek(drevo.desno, drevo.podatek+1, maxi))


def vmesni_pregled(drevo):
    '''vmesni pregled dreves'''
    if not drevo.prazno:
        for levi in vmesni_pregled(drevo.levo):
            yield levi   
        yield drevo.podatek
        for desni in vmesni_pregled(drevo.desno):
            yield desni


def je_iskalno_vmesni(drevo):
    '''z vmesnim pregledom preveri ali je drevo iskalno'''
    prejsni = float('-inf')
    for podatek in vmesni_pregled(drevo):
        if prejsni >= podatek:
            return False
        prejsni = podatek
    return True #prišli smo do konca


if __name__ == '__main__':
    drevo_2 = Drevo(2,levo=Drevo(2),desno=Drevo(3))
    prazno = Drevo()
    en_el = Drevo(0)
    d = Drevo(5,
              levo=Drevo(3),
              desno=Drevo(6))
    
    ni_iskalno = Drevo(2,
                       levo=Drevo(3),
                       desno=Drevo(6))
    
    drevo_1 = Drevo(25,
                  levo=Drevo(13,
                             levo=Drevo(11,
                                        levo = Drevo(-4),desno=Drevo(12)),
                             desno = Drevo(17,
                                           levo=Drevo(15),
                                           desno = Drevo(20))),
                  desno=Drevo(42,
                              levo=Drevo(30,
                                         levo = Drevo(27),
                                         desno = Drevo(40)),
                              desno=Drevo(45)))
    
    print(je_iskalno(prazno))
    print(je_iskalno(d))
    print(je_iskalno(drevo_2))
    print(je_iskalno(en_el))
    print(je_iskalno(ni_iskalno))
    print(je_iskalno(drevo_1))
    print('----')
    print(je_iskalno_vmesni(prazno))
    print(je_iskalno_vmesni(drevo_2))
    print(je_iskalno_vmesni(en_el))
    print(je_iskalno_vmesni(ni_iskalno))
    print(je_iskalno_vmesni(drevo_1))
