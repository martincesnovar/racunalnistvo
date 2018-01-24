# =============================================================================
# Strassenovo množenje
#
# Za kakršnokoli resno delo z matrikami v Pythonu uporabljamo knjižnico
# [NumPy](http://numpy.scipy.org) (bomo videli, zakaj). A zaradi
# preprostosti jih bomo vseeno predstavili kar s seznami seznamov.
# 
# Zaradi enostavnejšega računanja bomo pri tej nalogi prav tako
# predpostavili, da so dimenzije vseh matrik oblike $2^k \times 2^k$.
# V nasprotnem primeru bi matrike do želene velikosti dopolnili z ničlami.
# =====================================================================@011841=
# 1. podnaloga
# Sestavite funkcijo `strassenovo_mnozenje(a, b)`, ki po Strassenovem
# postopku zmnoži matriki `a` in `b`.
# =============================================================================
import time

def obicajno_mnozenje(a, b):
    """obicajno_mnozenje(a, b) po običajnem postopku zmnoži kvadratni matriki
       a in b."""
    assert len(a[0]) == len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
             for i in range(len(a))]

def primerjaj_case(k):
    """primerjaj_case(k) po običajnem in Strassenovem postopku zmnoži dve
       kvadratni matriki velikosti 2 ** k ter primerja čase množenja."""
    n = 2 ** k
    mat1 = [[i + j % 7 for i in range(n)] for j in range(n)]
    mat2 = [[i + j % 4 for i in range(n)] for j in range(n)]
    
    print("Množim...", end="")
    zac = time.time()
    zmn = obicajno_mnozenje(mat1, mat2)
    kon = time.time()
    print("Pomnoženo ({0:.6}s).".format(kon - zac))

    print("Množim po Strassenovo...", end="")
    zac = time.time()
    stras = strassenovo_mnozenje(mat1, mat2)
    kon = time.time()
    print("Pomnoženo ({0:.6}s).".format(kon - zac))

def na_bloke(a):
    '''Matriko razbije na 4 bloke'''
    n = len(a) // 2
    return ([vrs[:n] for vrs in a[:n]],
            [vrs[n:] for vrs in a[:n]],
            [vrs[:n] for vrs in a[n:]],
            [vrs[n:] for vrs in a[n:]])

def iz_blokov(a11, a12, a21, a22):
    '''Sestavi matriko iz blokov'''
    return ([vrs1 + vrs2 for vrs1, vrs2 in zip(a11, a12)] +
            [vrs1 + vrs2 for vrs1, vrs2 in zip(a21, a22)])

def sestej(a, b):
    '''Sešteje bloke'''
    return [[a[i][j] + b[i][j]
             for j in range(len(a[0]))]
             for i in range(len(b))]

def odstej(a, b):
    '''Odšteje bloke'''
    return [[a[i][j] - b[i][j]
             for j in range(len(a[0]))]
             for i in range(len(b))]

def _strassenovo_mnozenje(a, b):
    '''Strasnovo zmnozi matriko'''
    if len(a) == 1:
        return [[a[0][0] * b[0][0]]]

    a11, a12, a21, a22 = na_bloke(a)
    b11, b12, b21, b22 = na_bloke(b)

    m1 = strassenovo_mnozenje(sestej(a11, a22), sestej(b11, b22))
    m2 = strassenovo_mnozenje(sestej(a21, a22), b11)
    m3 = strassenovo_mnozenje(a11, odstej(b12, b22))
    m4 = strassenovo_mnozenje(a22, odstej(b21, b11))
    m5 = strassenovo_mnozenje(sestej(a11, a12), b22)
    m6 = strassenovo_mnozenje(odstej(a21, a11), sestej(b11, b12))
    m7 = strassenovo_mnozenje(odstej(a12, a22), sestej(b21, b22))


    c11 = sestej(odstej(sestej(m1, m4), m5), m7)
    c12 = sestej(m3, m5)
    c21 = sestej(m2, m4)
    c22 = sestej(sestej(odstej(m1, m2), m3), m6)

    return iz_blokov(c11, c12, c21, c22)


def strassenovo_mnozenje(a, b, n=50):
    '''Na majhnih problemih se ne splača strassnov'''
    if len(a) < n:
        return obicajno_mnozenje(a,b)
    return _strassenovo_mnozenje(a,b)
