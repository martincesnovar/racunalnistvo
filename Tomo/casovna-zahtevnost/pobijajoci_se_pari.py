# =============================================================================
# Pobijajoči se pari
#
# Na začetku naslednjih vaj bomo pogledali vse oddane rešitve in med njimi
# priredili tekmovanje. Nagrade bodo bajne!
# 
# Kdor želi, lahko rešitev napiše tudi v drugem programskem jeziku, vendar bomo
# zaradi poštenosti rešitve pomnožili z ustreznim časovnim faktorjem.
# =====================================================================@011730=
# 1. podnaloga
# Sestavite funkcijo `nicelni_pari_v_urejenem(seznam)`, ki vrne `True`, če v
# urejenem seznamu celih števil obstaja par elementov, ki se sešteje v 0,
# in `False` sicer.
# =============================================================================
def nicelni_pari_v_urejenem(seznam):
    '''O(n)'''
    slo = {}
    stevilo0=0
    for i in range(len(seznam)):
        slo[seznam[i]] = 0
        if seznam[i] == 0:
            stevilo0+=1
        if stevilo0 > 1:
            return True
        if seznam[i] in slo and -seznam[i] in slo and seznam[i] != 0:
            return True
    return False

def nicelni_pari_v_urejenem(seznam):
    '''O(n^2)'''
    for i in range(len(seznam)):
        for j in range(len(seznam)):
            if i != j and seznam[i] + seznam[j] == 0:
                return True
    return False
# =====================================================================@011731=
# 2. podnaloga
# Sestavite funkcijo `nicelni_pari_v_neurejenem(seznam)`, ki vrne `True`, če v
# neurejenem seznamu celih števil obstaja par elementov, ki se sešteje v 0,
# in `False` sicer.
# =============================================================================

def nicelni_pari_v_neurejenem(seznam):
    '''O(n)'''
    slo = {}
    stevilo0=0
    for i in range(len(seznam)):
        slo[seznam[i]] = 0
        if seznam[i] == 0:
            stevilo0+=1
        if stevilo0 > 1:
            return True
        if seznam[i] in slo and -seznam[i] in slo and seznam[i] != 0:
            return True
    return False

def nicelni_pari_v_neurejenem(seznam):
    '''O(n^2)'''
    for i in range(len(seznam)):
        for j in range(len(seznam)):
            if i != j and seznam[i] + seznam[j] == 0:
                return True
    return False
