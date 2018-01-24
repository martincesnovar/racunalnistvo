class Vozel:
  ''' Osnovni element verižnega seznama '''
  def __init__(self, kaj=None, kam=None):
     self.podatek = kaj
     self.naslednji  = kam

def dodajNaZačetek(zacVerige, kajDodamo):
    '''V verigo z začetkom zacVerige dodamo 
       na začetek nov vozel s podatkom kajDodamo'''
    novVozel = Vozel()
    novVozel.podatek = kajDodamo
    novVozel.naslednji = zacVerige
    zacVerige = novVozel
    return zacVerige
    
def izpisVerige(prvi):
    '''Izpiši verigo z začetkom prvi'''
    kjeSem = prvi
    while kjeSem != None:
        print(kjeSem.podatek)
        kjeSem = kjeSem.naslednji
    
prvi = Vozel()
prvi.podatek = 'A'

drugi = Vozel()
drugi.podatek = 'B'

tretji = Vozel()
tretji.podatek = 'C'

prvi.naslednji = drugi
drugi.naslednji = tretji

drugi = None
tretji = None 
začetek = prvi
prvi = None

# izpiši vsebino verige

izpisVerige(začetek)

# na začetek dodamo vozel s podatkom J

začetek = dodajNaZačetek(začetek, 'J')


# izpiši vsebino spremenjene verige
print('Spremenjena')
izpisVerige(začetek)

začetek = dodajNaZačetek(začetek, 'X')

# izpiši vsebino spremenjene verige
print('Spremenjena')
izpisVerige(začetek)

