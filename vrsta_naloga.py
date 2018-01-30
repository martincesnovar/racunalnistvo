from vrsta import *
def spremeni(vrsta):
    '''odstrani sode elemente iz vrste'''
    vrsta.vstavi(0)
    while vrsta.zacetek() != 0:
        if vrsta.zacetek() % 2:
            zac = vrsta.zacetek()
            vrsta.vstavi(zac)
        vrsta.odstrani()
    vrsta.odstrani()
            
