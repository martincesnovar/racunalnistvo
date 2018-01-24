# =============================================================================
# Največji podprodukt
# =====================================================================@011616=
# 1. podnaloga
# Sestavite funkcijo `najvecji_podprodukt(sez)`, ki izračuna največji produkt
# strnjenega podzaporedja pozitivnih števil v seznamu `sez`. Na primer:
# 
#     >>> najvecji_podprodukt([0.5, 2, 0.7, 3])
#     4.2
#     >>> najvecji_podprodukt([2, 3, 0, 4, 2])
#     8
# =============================================================================

def najvecji_podprodukt(sez):
        '''izracuna najvecji_podprodukt seznama'''
        naj = 1
        s = 0
        for el in sez:
                t = s*el
                if t>1:
                        s=t
                        if s>naj:
                                naj =s
                else:
                        s=1
        return naj

