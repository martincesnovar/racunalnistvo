from dvojisko_drevo import Drevo

def vsota(drevo):
    '''vrne vsoto elementov drevesa'''
    if not drevo.prazno:
        vsota_levega = vsota(drevo.levo)
        vsota_desnega = vsota(drevo.desno)
        return drevo.podatek + vsota_levega + vsota_desnega
    else:
        return 0
        
def stevilo_listov(drevo):
    '''vrne število listov'''
    if drevo.prazno: #prazno drevo nima lista
        return 0
    if drevo.levo.prazno and drevo.desno.prazno:
        return 1
    return stevilo_listov(drevo.levo) + stevilo_listov(drevo.desno)
    
def minimum_V1(drevo):
    '''Vrne minimalni element v drevesu
    minimum glede na vrednost drevesa'''
    mini = float('inf')
    if drevo.prazno:
        return None
    min_levi = minimum_V1(drevo.levo)
    min_desni = minimum_V1(drevo.desno)
    if min_levi is not None:
        mini = min(mini, min_levi, drevo.podatek)
    if min_desni is not None:
        mini = min(mini, min_desni,drevo.podatek)
    if min_desni is None and min_levi is None:
        return drevo.podatek
    if min_desni is not None and min_levi is not None:
        mini = min(mini, min_levi, min_desni, drevo.podatek)
    return mini

def minimum(drevo):
    '''Vrni najmanjše število v drevesu oziroma None, če je drevo prazno.'''
    if drevo.prazno: 
        return None
    else:
        levi_minimum = minimum(drevo.levo) or float('inf')
        desni_minimum = minimum(drevo.desno) or float('inf')
        return min(drevo.podatek, levi_minimum, desni_minimum)


def visina(drevo):
    '''vrne visino drevesa'''
    if drevo.prazno:
        return 0
        
    return 1 + max(visina(drevo.levo), visina(drevo.desno))

def premer(drevo):
    '''vrne dolzino najdaljse poti v drevsu'''
    if drevo.prazno:
        return float('-inf')
    visina_levega = visina(drevo.levo)
    visina_desnega = visina(drevo.desno)

    levi_premer = premer(drevo.levo)
    desni_premer = premer(drevo.desno)

    return max(visina_levega + visina_desnega, max(levi_premer, desni_premer))
