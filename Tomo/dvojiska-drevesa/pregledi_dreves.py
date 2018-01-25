# =============================================================================
# Pregledi dreves
#
# V vseh spodnjih primerih naj bo `d` dvojiško drevo na spodnji sliki:
# 
#          5
#        /   \
#       3     2
#      /     / \
#     1     6   9
# =====================================================================@010473=
# 1. podnaloga
# Sestavite generator `premi_pregled(drevo)`, ki vrača podatke v vozliščih
# drevesa v _premem vrstnem redu_ (pre-order). To pomeni, da najprej obiščemo
# koren drevesa, nato levo poddrevo in na koncu še desno poddrevo. Vozlišča
# poddreves obiskujemo po enakem pravilu. Zgled:
# 
#     >>> [x for x in premi_pregled(d)]
#     [5, 3, 1, 2, 6, 9]
# =============================================================================
from dvojisko_drevo import *

def premi_pregled(d):
    '''premi pregled dreves'''
    if not d.prazno:
        yield d.podatek
        for levi in premi_pregled(d.levo):
            yield levi
        for desni in premi_pregled(d.desno):
            yield desni
    
    

# =====================================================================@010474=
# 2. podnaloga
# Sestavite generator `vmesni_pregled(self)`, ki vrača podatke v vozliščih
# drevesa v _vmesnem vrstnem redu_ (in-order). To pomeni, da najprej obiščemo
# levo poddrevo, nato koren drevesa in na koncu še desno poddrevo. Vozlišča
# poddreves obiskujemo po enakem pravilu. Zgled:
# 
#     >>> [x for x in vmesni_pregled(d)]
#     [1, 3, 5, 6, 2, 9]
# =============================================================================

def vmesni_pregled(d):
    '''vmesni pregled dreves'''
    if not d.prazno:
        for levi in vmesni_pregled(d.levo):
            yield levi
        yield d.podatek
        for desni in vmesni_pregled(d.desno):
            yield desni

# =====================================================================@011079=
# 3. podnaloga
# Sestavite generator `obratni_pregled(self)`, ki vrača podatke v vozliščih
# drevesa v _obratnem vrstnem redu_ (post-order). To pomeni, da najprej obiščemo
# levo poddrevo, nato desno poddrevo in na koncu še koren drevesa. Vozlišča
# poddreves obiskujemo po enakem pravilu. Zgled:
# 
#     >>> [x for x in obratni_pregled(d)]
#     [1, 3, 6, 9, 2, 5]
# =============================================================================

def obratni_pregled(d):
    '''obratni pregled dreves'''
    if not d.prazno:
        for levi in obratni_pregled(d.levo):
            yield levi
        for desni in obratni_pregled(d.desno):
            yield desni
        yield d.podatek


# =====================================================================@010475=
# 4. podnaloga
# Sestavite generator `pregled_po_nivojih(self)`, ki vrača podatke v vozliščih
# drevesa _po nivojih_ (level-order). To pomeni, da najprej obiščemo koren, nato
# vsa vozlišča, ki so na globini 1, nato vsa vozlišča, ki so na globini 2 itn.
# Vsa vozlišča na isti globini naštejemo od leve proti desni. Zgled:
# 
#     >>> [x for x in pregled_po_nivojih(d)]
#     [5, 3, 2, 1, 6, 9]
# =============================================================================
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

#=============================================

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

