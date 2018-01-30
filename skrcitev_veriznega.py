from Vozel import *

def skrcitev(vozel):
    voz = zac = vozel
    while zac is not None:
        vsota = 0
        while zac.vrniPodatek() > 0:
            zac = zac.VrniNasled()
            vsota += zac.vrniPodatek()
        voz.naslednji = Vozel(podatek)
        while zac.vrniPodatek() < 0:
            zac = zac.VrniNasled()
            vsota -= zac.vrniPodatek
        voz.nastaviNasled(Vozel(podatek))
    return voz
