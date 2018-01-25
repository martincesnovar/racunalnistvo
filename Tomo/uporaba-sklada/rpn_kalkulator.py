# =============================================================================
# RPN kalkulator
#
# Ko z enostavnim kalkulatorjem želimo izračunati malo zapletenejši račun,
# vedno nastanejo težave z zapisom oklepajev. Izkaže pa se, da se lahko
# uporabi oklepajev v celoti izognemo z [obrnjenim poljskim zapisom](
#   http://wiki.fmf.uni-lj.si/wiki/Aritmetični_izrazi_v_obrnjenem_poljskem_zapisu
# ) (reverse Polish notation oz. na krajše RPN).
# 
# V tem zapisu operacij ne pišemo med argumenti, temveč za njimi. Tako namesto
# `4 + 5` pišemo `4 5 +`. Če želimo izračunati `(2 + 4) * 3`, pa napišemo
# `2 4 + 3 *`. Ko napišemo `2 4 +`, je to isto, kot če bi napisali `6`,
# in ko temu dodamo še `3 *`, dobimo iskani rezultat `18`.
# 
# V splošnem števila dajemo na sklad, z operacijo pa s sklada poberemo
# dve vrhnji števili, nanj pa vstavimo rezultat operacije.
# =====================================================================@010429=
# 1. podnaloga
# Sestavite funkcijo `izracunaj(a, b, op)`, ki dobi niza `a` in `b`,
# ki predstavljata celi števili, in operacijo `op`, ki je bodisi znak `'+'`
# (seštevanje) bodisi znak `'*'` (množenje).
# Funkcija naj vrne niz, ki predstavlja rezultat operacije na
# argumentih `a` in `b`.
# 
#     >>> izracunaj('10', '5', '+')
#     '15'
#     >>> izracunaj('5', '3', '*')
#     '15'
# =============================================================================
from sklad import Sklad

def izracunaj(a, b, op):
    a, b = int(a), int(b)
    if op == '+':
        return str(a+b)
    elif op == '*':
        return str(a*b)

# =====================================================================@010430=
# 2. podnaloga
# Sestavite funkcijo `vrednost_rpn(niz)`, ki dobi niz z veljavnim RPN izrazom ter
# izračuna in vrne njegovo vrednost.
# 
#     >>> vrednost_rpn('10 5 + 3 7 * +')
#     36
# 
# Namig: Pri izračunu si pomagajte s skladom. Niz razbijte po presledkih,
# nato pa po vrsti preglejte vse dele. Če pridete do števila, ga dajte na
# sklad, če pa pridete do operacije, s sklada vzemite vrhnji dve števili,
# izračunajte rezultat, ter ga postavite nazaj na sklad. Ko pridete do
# konca seznama, bi na skladu moralo ostati le eno število, ki predstavlja
# rezultat.
# =============================================================================

def vrednost_rpn(niz):
    sklad_stevil = Sklad()
    sez = niz.split()
    for c in sez:
        if c not in '+*':
            sklad_stevil.vstavi(c)
        else:
            st1 = sklad_stevil.vrh()
            sklad_stevil.odstrani()
            st2 = sklad_stevil.vrh()
            sklad_stevil.odstrani()
            rez = izracunaj(st1, st2, c)
            sklad_stevil.vstavi(rez)
    return int(sklad_stevil.vrh())
            
        

# =====================================================================@010431=
# 3. podnaloga
# Sestavite funkcijo `obicajni_zapis(izraz)`, ki sprejme izraz v RPN in vrne
# niz z istim izrazom v običajni obliki. Da ne bo težav z oklepaji, jih
# postavite okoli vsake uporabe operacije.
# 
#     >>> obicajni_zapis('2 4 +')
#     '(2 + 4)'
#     >>> obicajni_zapis('2 4 + 3 *')
#     '((2 + 4) * 3)'
#     >>> obicajni_zapis('10 5 + 3 7 * +')
#     '((10 + 5) + (3 * 7))'
# 
# Namig: Ali lahko nalogo rešite tako, da minimalno predelate funkcijo `vrednost_rpn`?
# =============================================================================


def obicajni_zapis(niz):
    sklad_stevil = Sklad()
    sez = niz.split()
    for c in sez:
        if c not in '+*':
            sklad_stevil.vstavi(c)
        else:
            st1 = sklad_stevil.vrh()
            sklad_stevil.odstrani()
            st2 = sklad_stevil.vrh()
            sklad_stevil.odstrani()
            sklad_stevil.vstavi("({} {} {})".format(st2, c, st1))
    return sklad_stevil.vrh()

