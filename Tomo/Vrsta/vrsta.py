class Elt:

    def __init__(self, vsebina, dummy=False):
        self.dummy = dummy
        if not dummy:
            self.vsebina = vsebina


class Vrsta:

    def __init__(self, zacetni_elti=None):
        '''Ustvari vrsto z danimi začetnimi elementi zacetni_elti.'''
        self.zacetni = Elt(None, dummy=True)
        self.koncni = self.zacetni
        if zacetni_elti:
            for x in zacetni_elti:
                self.vstavi(x)

    def prazna(self):
        '''Vrne True, če je vrsta prazna, sicer vrne False.'''
        return self.zacetni.dummy

    def vstavi(self, vsebina):
        '''Na konec vrste vstavi podatek vsebina.'''
        self.koncni.naslednji = Elt(None, dummy=True)
        self.koncni.vsebina = vsebina
        self.koncni.dummy = False
        self.koncni = self.koncni.naslednji

    def zacetek(self):
        '''Vrne začetni podatek v vrsti. Če ga ni, sproži izjemo.'''
        if self.prazna():
            raise IndexError('ZACETEK: Vrsta je prazna.')
        return self.zacetni.vsebina

    def odstrani(self):
        '''Iz vrste odstrani začetni podatek. Če ga ni, sproži izjemo.'''
        if self.prazna():
            raise IndexError('ODSTRANI: Vrsta je prazna.')
        self.zacetni = self.zacetni.naslednji

    def __repr__(self):
        '''Vrne predstavitev vrste z nizom "Vrsta([x1, ..., xn])".'''
        seznam = []
        p = self.zacetni
        while not p.dummy:
            seznam.append(repr(p.vsebina))
            p = p.naslednji
        return 'Vrsta([{0}])'.format(', '.join(seznam))

    def __str__(self):
        '''Vrne predstavitev vrste z nizom "ZACETEK : x1 : ... : xn : Konec".'''
        if self.prazna():
            return 'ZACETEK : KONEC'
        seznam = []
        p = self.zacetni
        while not p.dummy:
            seznam.append(str(p.vsebina))
            p = p.naslednji
        return 'ZACETEK : ' + ' : '.join(seznam) + ' : KONEC'
