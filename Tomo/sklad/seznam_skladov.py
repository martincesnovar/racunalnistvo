# =============================================================================
# Seznam skladov
# =====================================================================@010424=
# 1. podnaloga
# Sestavite funkcijo `locevanje(sklad)`, ki kot argument dobi sklad celih števil `sklad`
# in vrne seznam desetih skladov, pri čemer $i$-ti sklad ($i = 0, 1, \ldots, 9$)
# vsebuje tista števila s sklada `sklad`, ki dajo ostanek $i$ pri deljenju z 10.
# Zgled:
# 
#     >>> s = Sklad()
#     >>> s.vstavi(2)
#     >>> s.vstavi(13)
#     >>> s.vstavi(5)
#     >>> s.vstavi(4)
#     >>> s.vstavi(3)
#     >>> s.vstavi(14)
#     >>> s.vstavi(23)
#     >>> r = locevanje(s)
#     >>> all([r[0].prazen(), r[1].prazen(), r[6].prazen(), r[7].prazen(), r[8].prazen(), r[9].prazen()])
#     True
#     >>> print(r[2])
#     DNO : 2 : VRH
#     >>> print(r[3])
#     DNO : 13 : 3 : 23 : VRH
#     >>> print(r[4])
#     DNO : 4 : 14 : VRH
#     >>> print(r[5])
#     DNO : 5 : VRH
# =============================================================================


from sklad import Sklad

def locevanje(sklad):
    pomozen_sez = [Sklad() for i in range(10)]
    sez_skladov = [Sklad() for i in range(10)]
    while not sklad.prazen():
        x = sklad.vrh()
        sklad.odstrani()
        pomozen_sez[x%10].vstavi(x)
    for i in range(len(pomozen_sez)):
        while not pomozen_sez[i].prazen():
            x = pomozen_sez[i].vrh()
            pomozen_sez[i].odstrani()
            sez_skladov[i].vstavi(x)

    return sez_skladov

