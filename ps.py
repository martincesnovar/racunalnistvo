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

class Drevo: 
        
    def __init__(self, *args, **kwargs):
        '''Ustvari dvojiško drevo.

        - Drevo() ustvari prazno dvojiško drevo
        - Drevo(podatek, levo, desno) ustvari dvojiško drevo z
          danim podatkom v korenu ter levim in desnim sinom. Če kakšen od sinov
          manjka, se privzame, da je prazen.
        '''
        if args:
            assert len(args) == 1
            self.prazno = False
            self.podatek = args[0]
            # če levega ali desnega sina ne podamo, ustvarimo prazno drevo
            self.levo = kwargs.pop('levo', None) or Drevo()  
            self.desno = kwargs.pop('desno', None) or Drevo()
        else:
            self.prazno = True
        # poleg že obdelanih konstruktor ne sme sprejeti drugih argumentov
        assert not kwargs

    @staticmethod            
    def iz_tabele(podatki, polozaj_korena=1):
        '''Sestavi drevo iz tabelarične predstavitve, podane s tabelo podatki.'''
        if polozaj_korena > len(podatki) or podatki[polozaj_korena - 1] is None:
            return Drevo()
        else:
            levo = Drevo.iz_tabele(podatki, 2 * polozaj_korena)
            desno = Drevo.iz_tabele(podatki, 2 * polozaj_korena + 1)
            return Drevo(podatki[polozaj_korena - 1], levo=levo, desno=desno)

    def __repr__(self, zamik=''):
        if self.prazno:
            return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
            return 'Drevo({1})'.format(zamik, self.podatek)
        else:
           return 'Drevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
               format(
                   zamik,
                   self.podatek,
                   self.levo.__repr__(zamik + '             '),
                   self.desno.__repr__(zamik + '              ')
               )

    def __eq__(self, other):
        if self.prazno and other.prazno:
            return True
        elif not self.prazno and not other.prazno:
            return (
                self.podatek == other.podatek and
                self.levo == other.levo and
                self.desno == other.desno
            )
        else:
            return False

    def __hash__(self):
        if self.prazno:
            return hash(())
        else:
            return hash((self.podatek, self.levo, self.desno))

class Vozel:
  ''' Osnovni element verižnega seznama '''
  def __init__(self, kaj=None, kam=None):
     self._podatek = kaj
     self._naslednji  = kam

  def __str__(self):
     return str(self._podatek)
    
  def nastaviPodatek(self, pod):
      '''Vozlu spremeni podatek na pod'''
      self._podatek = pod

  def vrniPodatek(self):
     ''' vrne podatek, ki je v vozlu'''
     return self._podatek

  def nastaviNasled(self, mojNasled) :
     '''Vozlu nastavi novega naslednika'''
     self._naslednji = mojNasled

  def vrniNasled(self):
     ''' Vrne kazalec na naslednji vozel '''
     return self._naslednji
