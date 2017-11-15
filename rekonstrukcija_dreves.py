from dvojisko_drevo import Drevo

def drevo_vmesni_premi(vmesni, premi):
    '''iz seznama vmesni in premi rekonstruira drevo'''
    if len(premi) == 0:
        return Drevo()
    
    podatek = premi[0]

    i = vmesni.index(podatek)

    levo_vmesni = vmesni[:i]
    desno_vmesni = vmesni[i+1:]
    
    levi_premi = premi[1:i+1]
    desni_premi = premi[1+i:]
    
    drevo_levi = drevo_vmesni_premi(levo_vmesni,levi_premi)
    drevo_desni = drevo_vmesni_premi(desno_vmesni,desni_premi)
    
    drevo = Drevo(podatek, levo=drevo_levi, desno=drevo_desni)
    return drevo

def drevo_vmesni_obratni(vmesni, obratni):
    '''iz seznama vmesni in obratni rekonstruira drevo'''
    if len(obratni) == 0:
        return Drevo()
    podatek = obratni[-1]

    i = vmesni.index(podatek)

    desno_vmesni = vmesni[i+1:]
    levo_vmesni = vmesni[:i]
    
    levi_obratni = obratni[:i]
    desni_obratni = obratni[i:-1]
    
    drevo_levi = drevo_vmesni_obratni(levo_vmesni,levi_obratni)
    drevo_desni = drevo_vmesni_obratni(desno_vmesni,desni_obratni)
    
    drevo = Drevo(podatek, levo=drevo_levi, desno=drevo_desni)
    return drevo

def drevo_vmesni_nivojski(vmesni, nivojski):
    '''iz seznama vmesni in nivojski rekonstruira drevo'''
    if len(nivojski) == 0:
        return Drevo()
    podatek = nivojski[0]

    i = vmesni.index(podatek)

    desno_vmesni = vmesni[i+1:]
    levo_vmesni = vmesni[:i]

    
    drevo_levi = drevo_vmesni_nivojski(levo_vmesni,[t for t in nivojski if t in levo_vmesni])
    drevo_desni = drevo_vmesni_nivojski(desno_vmesni,[t for t in nivojski if t in desno_vmesni])
    
    drevo = Drevo(podatek, levo=drevo_levi, desno=drevo_desni)
    return drevo

def drevesa_premi_obratni(premi, obratni):
    '''vrne množico vseh možnih dreves, ki jih lahko dobimo z premim in obratnim pregledom'''
    if len(premi) == 0:
        return {Drevo()}
    elif len(premi) == 1:
        return {Drevo(premi[0])}
    podatek = premi[0]
    lk = obratni.index(premi[1])
    mozna_prva_poddrevesa = drevesa_premi_obratni(premi[1:lk + 2], obratni[:lk + 1])
    mnozica = set()
    if lk == len(obratni) - 2:
        for drevo in mozna_prva_poddrevesa:
            mnozica.add(Drevo(podatek, levo = drevo, desno = Drevo())) #prazno desno poddrevo
            mnozica.add(Drevo(podatek, levo = Drevo(), desno = drevo)) #prazno levo poddrevo
    else:
        mozna_leva = mozna_prva_poddrevesa
        mozna_desna = drevesa_premi_obratni(premi[lk+2:],obratni[lk + 1:-1])
        for levo in mozna_leva:
            for desno in mozna_desna:
                mnozica.add(Drevo(premi[0], levo=levo, desno=desno))
    return mnozica

def drevesa_vmesni_premi(vmesni, premi):
    '''vrne množico vseh možnih dreves, ki jih lahko dobimo z premim in obratnim pregledom'''
    if len(premi) == 0:
        return {Drevo()}
    mnozica = set()
    koreni = [i for i in range(len(vmesni)) if vmesni[i] == premi[0]]
    for i in koreni:
        for levo in drevesa_vmesni_premi(vmesni[:i], premi[1:i+1]):
            for desno in drevesa_vmesni_premi(vmesni[i+1:],premi[i+1:]):
                mnozica.add(Drevo(premi[0], levo = levo, desno=desno))
    return mnozica
