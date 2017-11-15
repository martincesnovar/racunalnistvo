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
