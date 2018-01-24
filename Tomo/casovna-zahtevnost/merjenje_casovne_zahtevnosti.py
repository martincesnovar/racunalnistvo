# =============================================================================
# Merjenje časovne zahtevnosti
#
# Če za algoritem nimamo na voljo izvorne kode, časovne zahtevnosti ne moremo
# oceniti drugače, kot da jo poskušamo izmeriti. Če odkomentirate vrstico
# 
#     # import zlib, base64; exec(zlib.decompress(base64.b64decode('eJwll7eu...
# 
# v priloženi kodi, naložite definicijo 14 funkcij, katerih časovno zahtevnost
# boste merili pri tej nalogi.
# =====================================================================@011610=
# 1. podnaloga
# Funkcije `f1a`, `f1b`, `f1c`, `f1d` in `f1e` imajo časovne zahtevnosti oblike
# $O(n^k)$ za nek neznani $k$. V spremenljivko `potence1` shranite nabor potenc
# časovnih zahtevnosti posameznih funkcij. Na primer, če bi imele funkcije
# časovne zahtevnosti $O(n^3)$, $O(n)$, $O(n^4)$, $O(n)$ in $O(n^2)$, bi v
# spremenljivko `potence1` shranili nabor `(3, 1, 4, 1, 2)`.
# =============================================================================
import zlib, base64; exec(zlib.decompress(base64.b64decode('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')))

import time
import math

try:
    import matplotlib.pyplot as plt
except:
    pass

def stopaj(f,n):
    zacetek = time.time()
    f(n)
    konec = time.time()
    return konec - zacetek

def narisi_graf(f,velikosti,loglog=False):
    cas = [stopaj(f,x) for x in velikosti]
    if loglog:
        log_casi = [math.log(casi) for casi in cas]
        log_velikosti = [math.log(vel) for vel in velikosti]
        plt.plot(log_velikosti, log_casi)
    else:
        plt.plot(velikosti, cas)
    plt.show()
        


niz = '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'
def dekodiraj(niz):
    '''dekodira besedilo'''
    dekodiraj_1 = zlib.decompress(base64.b64decode(niz))
    while b'import zlib,base64\nexec' in dekodiraj_1:
        dekodiraj_1 = zlib.decompress(base64.b64decode(dekodiraj_1[58:-4]))
    return dekodiraj_1.decode()

def zapisi_na_dat(ime, niz=niz):
    '''zapiše dekodirano nalogo na datoteko'''
    dekodiran = dekodiraj(niz)
    with open(ime,'w') as f:
        print(dekodiran, file=f)
    
    
potence1=(3, 0, 4, 1, 4)
# =====================================================================@011611=
# 2. podnaloga
# V spremenljivko `potence2` shranite nabor potenc časovnih zahtevnosti funkcij
# `f2a`, `f2b`, `f2c`, `f2d` in `f2e`.
# =============================================================================
potence2 = (2,2,1,3,2)
# =====================================================================@011612=
# 3. podnaloga
# V spremenljivko `potence3` shranite nabor potenc časovnih zahtevnosti funkcij
# `f3a`, `f3b`, `f3c` in `f3d`.
# =============================================================================
potence3=(5,1,0,4)

