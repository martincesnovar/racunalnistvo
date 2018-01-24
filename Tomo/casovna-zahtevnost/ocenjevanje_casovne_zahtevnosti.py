# =============================================================================
# Ocenjevanje časovne zahtevnosti
#
# Dostikrat lahko časovno zahtevnost algoritma ocenimo že iz njegove izvorne
# kode.
# =====================================================================@011618=
# 1. podnaloga
# Dane naj bodo sledeče funkcije:
# 
#     def vsota1(n):
#         vsota = 0
#         for i in range(n):
#             for j in range(n):
#                 vsota += i + j
#         return vsota
#  
#     def vsota2(n):
#         vsota = 0
#         for i in range(n):
#             for j in range(100):
#                 vsota += i + j
#         return vsota
#  
#     def vsota3(n):
#         vsota = 0
#         for i in range(n):
#             for j in range(n):
#                 vsota += sum(range(i))
#         return vsota
# 
# V spremenljivko `potence1` shranite nabor potenc njihovih časovnih zahtevnosti
# v odvisnosti od vhoda $n$. Na primer, če bi imele funkcije časovne zahtevnosti
# $O(n^3)$, $O(n)$ in $O(n^4)$, bi v spremenljivko `potence1` shranili
# nabor `(3, 1, 4)`.
# =============================================================================
potence1 = (2, 1, 3)
# =====================================================================@011617=
# 2. podnaloga
# Dane naj bodo sledeče funkcije na seznamih:
# 
#     def poisci_max1(sez):
#         return sez.index(max(sez))
# 
#     def poisci_max2(sez):
#         najvecji = None
#         for i in range(len(sez)):
#             if najvecji is None or sez[i] > najvecji:
#                 najvecji_i = i
#                 najvecji = sez[i]
#         return najvecji_i
# 
#     def poisci_max3(sez):
#         for i in range(len(sez)):
#             if sez[i] == max(sez):
#                 return i
# 
# V spremenljivko `potence2` shranite nabor potenc njihovih časovnih zahtevnosti
# v odvisnosti od dolžine vhodnega seznama.
# =============================================================================
potence2 = (1,1,2)
# =====================================================================@011728=
# 3. podnaloga
# Dane naj bodo sledeče funkcije, ki izračunajo sled kvadratne matrike
# velikosti $n \times n$:
# 
#     def sled1(mat):
#         sled = 0
#         for i in range(len(mat)):
#              for j in range(len(mat)):
#                  if i == j:
#                      sled += mat[i][j]
#         return sled
# 
#     def sled2(mat):
#         sled = 0
#         for i in range(len(mat)):
#              sled += mat[i][i]
#         return sled
# 
#     def sled3(mat):
#         sled = 0
#         for i, vrstica in enumerate(mat):
#              sled += vrstica[i]
#         return sled
# 
# V spremenljivko `potence3` shranite nabor potenc njihovih časovnih zahtevnosti
# v odvisnosti od števila $n$.
# =============================================================================
potence3=(2,1,1)
# =====================================================================@011729=
# 4. podnaloga
# Dane naj bodo sledeče funkcije, ki iščejo dani element v urejenem seznamu:
# 
#     def poisci1(sez, x):
#         return x in sez
# 
#     def poisci2(sez, x):
#         for y in sez:
#             if x == y:
#                 return True
#         return False
#     
#     def poisci3(sez, x):
#         od, do = 0, len(sez)
#         while od < do:
#             sredina = (od + do) // 2
#             sredinski = sez[sredina]
#             if x == sredinski:
#                 return True
#             elif x < sredinski:
#                 do = sredina
#             elif x > sredinski:
#                 od = sredina + 1
#         return False
#     
#     def poisci4(sez, x, od=0, do=None):
#         if do is None:
#             do = len(sez)
#         if od == do:
#             return False
#         else:
#             sredina = (od + do) // 2
#             sredinski = sez[sredina]
#             if x == sredinski:
#                 return True
#             elif x < sredinski:
#                 return poisci4(sez, x, od, sredina)
#             elif x > sredinski:
#                 return poisci4(sez, x, sredina + 1, do)
#     
#     def poisci5(sez, x):
#         if not sez:
#             return False
#         else:
#             sredina = len(sez) // 2
#             sredinski = sez[sredina]
#             if x == sredinski:
#                 return True
#             elif x < sredinski:
#                 return poisci5(sez[:sredina], x)
#             elif x > sredinski:
#                 return poisci5(sez[sredina + 1:], x)
# 
# V spremenljivko `zahtevnosti4` shranite nabor njihovih časovnih zahtevnosti,
# v odvisnosti od dolžine seznama. Časovne zahtevnosti opišite z enim od nizov
#     'O(1)', 'O(n)', 'O(n^2)', 'O(log n)', 'O(n log n)', 'O(n^3)'.
# =============================================================================
zahtevnosti4 = ('O(n)', 'O(n)', 'O(log n)', 'O(log n)', 'O(n)')

