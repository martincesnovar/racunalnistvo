from vrsta import Vrsta

def uredi_s_vrsto(vrsta):
    v=Vrsta()
    if not vrsta.prazna():
        vrsta.vstavi('Straža')
        while vrsta.zacetek() != 'Straža':
            mini = vrsta.zacetek()
            while not vrsta.prazna() and vrsta.zacetek() != 'Straža':
                mini = min(mini,vrsta.zacetek())
                vrsta.odstrani()
            v.vstavi(mini)
    return v
            
