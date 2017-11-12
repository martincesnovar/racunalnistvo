def premi_pregled(d):
    '''premi pregled dreves'''
    if not d.prazno:
        yield d.podatek
        for levi in premi_pregled(d.levo):
            yield levi
        for desni in premi_pregled(d.desno):
            yield desni
            
def vmesni_pregled(d):
    '''vmesni pregled dreves'''
    if not d.prazno:
        for levi in vmesni_pregled(d.levo):
            yield levi
        yield d.podatek
        for desni in vmesni_pregled(d.desno):
            yield desni
            
def obratni_pregled(d):
    '''obratni pregled dreves'''
    if not d.prazno:
        for levi in obratni_pregled(d.levo):
            yield levi
        for desni in obratni_pregled(d.desno):
            yield desni
        yield d.podatek
        
