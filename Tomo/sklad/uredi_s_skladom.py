from sklad import Sklad

def uredi_s_skladom(sklad):
    s=Sklad()
    skl=Sklad()
    while not sklad.prazen():
        vrh=sklad.vrh()
        sklad.odstrani()
        while not s.prazen() and s.vrh()>vrh:
            sklad.vstavi(s.vrh())
            s.odstrani()
        s.vstavi(vrh)
    while not s.prazen():
        skl.vstavi(s.vrh())
        s.odstrani()
    while not skl.prazen():
        sklad.vstavi(skl.vrh())
        skl.odstrani()
    return
        
