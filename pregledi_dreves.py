from drevo import Drevo

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
        
from vrsta import Vrsta

def pregled_po_nivojih(zacetno_drevo):
    '''pregleda drevo po nivojih'''
    vrsta = Vrsta([zacetno_drevo])
    while not vrsta.prazna():
        drevo = vrsta.zacetek()
        if not drevo.prazno:
            vrsta.vstavi(drevo.levo)
            vrsta.vstavi(drevo.desno)
            yield drevo.podatek
        vrsta.odstrani()
        
        
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
