# =============================================================================
# Vlak
# =====================================================================@010428=
# 1. podnaloga
# Na neki vaški železniški postaji imamo poleg glavnega tira še en slepi
# tir, s pomočjo katerega lahko spremenimo vrstni red vagonov. Slepi
# tir lahko sprejme poljubno število vagonov. Na primer, vlak 321 s tremi vagoni
# pripelje z leve in nadaljuje z vožnjo proti desni. Če vagonov ne bi
# prerazporejali, bi vožnjo nadaljevali kot 321. Lahko pa vagon 1 preusmerimo na
# slepi tir, vagon 2 spustimo naprej, s slepega tira spustimo 1 in nazadnje mimo
# spustimo še vagon 3, s čimer dobimo zaporedje 312. Vseh zaporedij se na
# tak način ne da dobiti. Na primer, če bi želeli dobiti zaporedje 213, bi
# morali vagona 1 in 2 zadržati na slepem tiru ter mimo najprej spustiti vagon 3.
# To bi še šlo, vendar bi potem morali najprej spustiti vagon 2, saj je na slepi
# tir zapeljal za vagonom 1 in mu tako zapira pot.
# 
# Napišite funkcijo `vagoni(prihod, odhod)`, ki dobi dva seznama z opisom
# vagonov in vrne `True`, če jih lahko ustrezno permutiramo s pomočjo slepega
# tira, in `False` sicer. Zgled:
# 
#     >>> vagoni('321', '312')
#     True
#     >>> vagoni('321', '213')
#     False
# =============================================================================


from sklad import Sklad

def vagoni(prihod, odhod):
    '''Ali se lahko vlaki prerazporedijo'''
    vhod, izhod, slepi = Sklad(), Sklad(), Sklad()
    for el in prihod:
        vhod.vstavi(el)
    for el in odhod:
        izhod.vstavi(el)
    while not izhod.prazen():
        nasl = izhod.vrh()
        izhod.odstrani()
        while slepi.prazen() or slepi.vrh() != nasl:
            if vhod.prazen():
                return False
            slepi.vstavi(vhod.vrh())
            vhod.odstrani()
        slepi.odstrani()
    return True

