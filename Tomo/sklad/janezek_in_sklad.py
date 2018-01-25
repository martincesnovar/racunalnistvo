# =============================================================================
# Janezek in sklad
# =====================================================================@010411=
# 1. podnaloga
# Janezek je želel preveriti delovanje razreda `Sklad`. V ta namen je
# napisal program, ki v sklad vstavi nekaj števil, jih nato prebere
# nazaj ter izpiše na zaslon. Ima pa nekaj manjših napak. Program si oglejte
# ter ga popravite tako, da bo deloval pravilno.
# =============================================================================
from sklad import Sklad

moj_sklad = Sklad()
# V sklad vstavimo števila od 1 do 10
for i in range(1,11):
    moj_sklad.vstavi(i)

# Izpišemo podatke v skladu na zaslon
while not moj_sklad.prazen():
    print(moj_sklad.vrh())
    moj_sklad.odstrani()
# =====================================================================@010412=
# 2. podnaloga
# Premislite, kaj vse bi bilo pri razredu `Sklad` še potrebno preveriti,
# da bi bili prepričani, da deluje pravilno. Za rešitev te podnaloge
# napišite program za testiranje sklada.
# 
# (Ta podnaloga nima testnih primerov, saj avtomatično preverjanje ni možno.)
# =============================================================================

from sklad import Sklad

moj_sklad = Sklad()
assert moj_sklad.prazen()==True
moj_sklad.vstavi(1)
assert moj_sklad.prazen()==False
moj_sklad.odstrani()
assert moj_sklad.prazen()==True
try:
    moj_sklad.odstrani()
    moj_sklad.vrh()
except:
    Exception('Napaka')
moj_sklad.vstavi(0)

