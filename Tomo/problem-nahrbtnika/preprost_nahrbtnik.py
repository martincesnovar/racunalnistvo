# =============================================================================
# Preprost nahrbtnik
# =====================================================================@010500=
# 1. podnaloga
# Dan je osnutek funkcije, ki naj bi poiskala rešitev preprostega nahrbtnika.
# Dopolni funkcijo ter odpravi morebitne napake. Pri tem je `predmeti` seznam
# parov, ki opisujejo posamezne predmete (vsak par je oblike `(velikost, vrednost)`),
# parameter `velikost` pa določa velikost nahrbtnika (število).
# 
#     def nahrbtnik(predmeti, velikost):
#         p = list(enumerate(predmeti))
#         p.sort(key=lambda t: t[1] / t[0])
#         v = 0
#         x = [0] * len(predmeti)
#         for i in range(len(p)):
#             k =
#             vel =
#             if v + vel <= velikost:
#                 x[k] = 1
#                 v += vel
#             else:
#                 if v != velikost:
#                     x[k] =
#                 break
#         return x
# 
# Primer:
# 
#     >>> nahrbtnik([(30,57),(27,60),(35,105),(40,113),(50,100),(51,108)], 60)
#     [0, 0, 1, 0.625, 0, 0]
# =============================================================================


def nahrbtnik(predmeti, velikost):
    '''reši problem preprostega nahrbtnika'''
    p = list(enumerate(predmeti))
    p.sort(key=lambda t: t[1][1] / t[1][0],reverse=True)
    v = 0
    x = [0] * len(predmeti)
    for i in range(len(p)):
        k = p[i][0]
        vel = p[i][1][0]
        if v + vel <= velikost:
            x[k] = 1
            v += vel
        else:
            if v != velikost:
                x[k] = (velikost-v)/vel
            break
    return x
