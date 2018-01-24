class Sklad:

    def __init__(self):
        self.podatki = []

    def vstavi(self, x):
        self.podatki.append(x)

    def prazen(self):
        return len(self.podatki) == 0

    def odstrani(self):
        if self.prazen():
            raise ValueError('ODSTRANI: Sklad je prazen.')
        del self.podatki[-1]

    def vrh(self):
        if self.prazen():
            raise ValueError('VRH: Sklad je prazen.')
        return self.podatki[-1]

    def poberi(self):
        if self.prazen():
            raise ValueError('POBERI: Sklad je prazen.')
        stari_vrh = self.vrh()
        self.odstrani()
        return stari_vrh

    def __str__(self):
        opisi = ['DNO'] + [str(elt) for elt in self.podatki] + ['VRH']
        return ' : '.join(opisi)
