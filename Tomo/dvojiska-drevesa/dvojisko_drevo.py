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
