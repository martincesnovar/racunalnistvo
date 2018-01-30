from verizni_seznam import *

def fun(vs1, vs2):
    tren1 = zac1 = vs1.zacetek()
    tren2 = zac2 = vs2.zacetek()
    while tren1 and tren2:
        while tren2 != tren1.naslednji:
            tren1 = tren1.naslednji
        tren1.naslednji=tren1.naslednji.naslednji
        while tren2.naslednji != tren1:
            tren2 = tren2.naslednji
            tren1.naslednji=tren1.naslednji.naslednji
    return zac1, zac2
