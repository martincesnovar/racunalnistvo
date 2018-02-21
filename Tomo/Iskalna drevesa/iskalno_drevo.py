# =============================================================================
# Iskalno drevo
#
# Dan je razred 'Vozlisce', ki predstavlja vozlišča dvojiškega drevesa
# s kazalci. Poleg vrednosti ključa za vsako vozlišče hranimo še kazalce
# na očeta ter levega in desnega sina.  Za osnovo iskalnega dvojiškega
# drevesa bomo vzeli razred 'Vozlisce', razred 'IskalnoDrevo' pa bo hranil
# kazalec na koren drevesa:
# 
#        class Vozlisce:
# 
#            def __init__(self, kljuc=None, levi=None, desni=None, oce=None):
#                self.kljuc = kljuc
#                if kljuc:
#                    if levi:
#                        self.levi = levi
#                    else:
#                        self.levi = Vozlisce()
#                    if desni:
#                        self.desni = desni
#                    else:
#                        self.desni = Vozlisce()
#                    self.oce = oce
# 
#            def prazno(self):
#                return self.kljuc == None
# 
#            def __repr__(self, zamik = ''):
#                if self.prazno():
#                  return 'Vozlisce()'.format(zamik)
#                elif self.levi.prazno() and self.desni.prazno():
#                  return 'Vozlisce({1})'.format(zamik, self.kljuc)
#                else:
#                  return 'Vozlisce({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
#                    format(
#                      zamik,
#                      self.kljuc,
#                      self.levi.__repr__(zamik + '             '),
#                      self.desni.__repr__(zamik + '              ')
#                    )
# 
#        class IskalnoDrevo:
# 
#            def __init__(self, koren=None):
#                self.koren = koren
# 
#            def __repr__(self):
#                if self.prazno():
#                    return "Vozlisce()"
#                else:
#                    return str(self.koren)                                  
# 
#            def prazno(self):
#                return self.koren == None
# 
#            def vstavi(self, kljuc):
#                if self.prazno():
#                    self.koren = Vozlisce(kljuc)
#                else:
#                    self.vstavi_vozlisce(self.koren, kljuc)
# =====================================================================@012750=
# 1. podnaloga
# Sestavite metodo `vstavi(self, kljuc)`, ki v iskalno drevo vstavi
# podatek 'kljuc'.
# Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d
#     Vozlisce(6,
#         levo = Vozlisce(4,
#                     levo = Vozlisce(1,
#                                     levo = Vozlisce(),
#                                     desno = Vozlisce(3)),
#                     desno = Vozlisce(5)),
#         desno = Vozlisce(9,
#                         levo = Vozlisce(7),
#                         desno = Vozlisce()))
# =============================================================================

def vmesni_pregled(vozlisce):
    '''vmesni pregled dreves'''
    if not vozlisce.prazno():
        for levi in vmesni_pregled(vozlisce.levi):
            yield levi
        yield vozlisce.kljuc
        for desni in vmesni_pregled(vozlisce.desni):
            yield desni

class Vozlisce:

    def __init__(self, kljuc=None, levi=None, desni=None, oce=None):
        self.kljuc = kljuc
        if kljuc:
            if levi:
                self.levi = levi
            else:
                self.levi = Vozlisce()
            if desni:
                self.desni = desni
            else:
                self.desni = Vozlisce()
            self.oce = oce

    def prazno(self):
        return self.kljuc == None

    def __repr__(self, zamik = ''):
        if self.prazno():
          return 'Vozlisce()'.format(zamik)
        elif self.levi.prazno() and self.desni.prazno():
          return 'Vozlisce({1})'.format(zamik, self.kljuc)
        else:
          return 'Vozlisce({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
            format(
              zamik,
              self.kljuc,
              self.levi.__repr__(zamik + '             '),
              self.desni.__repr__(zamik + '              ')
            )

class IskalnoDrevo:

    def __init__(self, koren=None):
        self.koren = koren

    def __repr__(self):
        if self.prazno():
            return "Vozlisce()"
        else:
            return str(self.koren)                                        

    def prazno(self):
        return self.koren == None

    def vstavi(self, kljuc):
        if self.prazno():
            self.koren = Vozlisce(kljuc)
        else:
            self.vstavi_vozlisce(self.koren, kljuc)
        
    def vstavi_vozlisce(self, vozlisce, kljuc):
        if kljuc < vozlisce.kljuc:
            if vozlisce.levi.prazno():
                vozlisce.levi = Vozlisce(kljuc, oce=vozlisce)
            else:
                self.vstavi_vozlisce(vozlisce.levi, kljuc)
        else:
            if vozlisce.desni.prazno():
                vozlisce.desni = Vozlisce(kljuc, oce=vozlisce)
            else:
                self.vstavi_vozlisce(vozlisce.desni, kljuc)
        

# =====================================================================@012751=
# 2. podnaloga
# Sestavite metodo `vrni(self, podatek)`, ki v iskalnem drevesu poišče
# `podatek`. Vrne naj drevo, ki ga vsebuje v korenu, oziroma prazno drevo, če
# ga ni v drevesu. Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.vrni(9)
#     Vozlisce(9,
#           levo = Vozlisce(7),
#           desno = Vozlisce())
#     >>> d.vrni(11)
#     Vozlisce()
# =============================================================================
    def vrni(self, podatek, vozlisce=None):
        '''vrne poddrevo, ki vsebuje v korenu podatek'''
        if self.prazno(): return IskalnoDrevo()
        if not vozlisce: vozlisce = self.koren
        if vozlisce.prazno(): return IskalnoDrevo()
        elif vozlisce.kljuc == podatek: return vozlisce
        elif vozlisce.kljuc > podatek: return self.vrni(podatek, vozlisce.levi)
        else: return self.vrni(podatek, vozlisce.desni)
        
# =====================================================================@012829=
# 3. podnaloga
# Sestavite metodo `maksimum(self)`, ki v iskalnem drevesu poišče
# največji ključ. Če je drevo prazno naj vrne niz "Drevo je prazno." Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.mmaksimum()
#     9
# 
#     >>> d = IskalnoDrevo()
#     >>> d.maksimum()
#     "Drevo je prazno."
# =============================================================================
    def maksimum(self,vozlisce=None):
        '''vrne maksimim, če obstaja'''
        if self.prazno():
            return "Drevo je prazno."
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.desni.prazno():
            return vozlisce.kljuc
        else:
            return self.maksimum(vozlisce.desni)
# =====================================================================@012830=
# 4. podnaloga
# Sestavite metodo `minimum(self)`, ki v iskalnem drevesu poišče
# najmanjši ključ. Če je drevo prazno naj vrne niz "Drevo je prazno." Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.minimum()
#     1
# 
#     >>> d = IskalnoDrevo()
#     >>> d.minimum()
#     "Drevo je prazno."
# =============================================================================
    def minimum(self,vozlisce=None):
        '''vrne minimum, če obstaja'''
        if self.prazno():
            return "Drevo je prazno."
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.levi.prazno():
            return vozlisce.kljuc
        else:
            return self.minimum(vozlisce.levi)
# =====================================================================@012831=
# 5. podnaloga
# Sestavite metodo `prednik(self, kljuc)`, ki v iskalnem drevesu poišče
# prednika vozlisca z vrednostjo 'kljuc'. Če prednika ni, naj vrne 'None'.
# Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.prednik(7)
#     6
#     >>> d.prednik(1)
#     None
# =============================================================================
    def prednik(self, kljuc):
        '''vrne prednika ključa'''
        vozlisce = self.vrni(kljuc, self.koren)
        if not vozlisce.levi.prazno():
            return self.maksimum(vozlisce.levi)
        return

    def prednik_alt(self,kljuc):
        '''vrne prednika z vmesnim pregledom'''
        prejsni = None
        vozlisce = self.vrni(kljuc,self.koren)
        for el in vmesni_pregled(vozlisce):
            if el == vozlisce.kljuc:
                return prejsni
            prejsni = el
        return
# =====================================================================@012832=
# 6. podnaloga
# Sestavite metodo `naslednik(self, kljuc)`, ki v iskalnem drevesu poišče
# naslednika vozlisca z vrednostjo 'kljuc'. Če naslednika ni, naj vrne 'None'.
# Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.naslednik(7)
#     9
#     >>> d.naslendik(9)
#     None
# =============================================================================
    def naslednik(self, kljuc):
        '''vrne naslednjika kljuca'''
        vozlisce = self.vrni(kljuc, self.koren)
        if not vozlisce.desni.prazno():
            return self.minimum(vozlisce.desni)
        return

    def naslednik_alt(self,kljuc):
        '''vrne naslednika z vmesnim pregledom'''
        vozlisce = self.vrni(kljuc,self.koren)
        naslednji = None
        najd = False
        for el in vmesni_pregled(vozlisce):
            if el == vozlisce.kljuc:
                najd = True
            elif najd:
                return el
        return
# =====================================================================@012833=
# 7. podnaloga
# Sestavite metodo `floor(self, podatek)`, ki v iskalnem drevesu poišče
# največji ključ, ki je manjši ali enak danemu številu 'podatek'. Če
# takega števila ni, naj metoda vrne 'inf'. Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.floor(2)
#     1
#     >>> d.floor(0)
#     inf
# =============================================================================
    def floor(self, podatek, vozlisce=None):
        '''vrne podatek ali prvega manjšega'''
        if self.prazno():
            return float('inf')
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.prazno():
            return float('inf')
        elif vozlisce.kljuc == podatek:
            return podatek
        elif vozlisce.kljuc > podatek:
            return self.floor(podatek, vozlisce.levi)
        else:
            vrednost = self.floor(podatek, vozlisce.desni)
            if vrednost is not None and vrednost <= podatek:
                return vrednost
            else:
                return vozlisce.kljuc
# =====================================================================@012834=
# 8. podnaloga
# Sestavite metodo `ceil(self, podatek)`, ki v iskalnem drevesu poišče
# najmanjsi ključ, ki je večji ali enak danemu številu 'podatek'. Če
# takega števila ni, naj metoda vrne '-inf'. Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.ceil(2)
#     3
#     >>> d.ceil(10)
#     -inf
# =============================================================================
    def ceil(self, podatek, vozlisce=None):
        '''vrne podatek ali prvega večjega'''
        if self.prazno():
            return float('-inf')
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.prazno():
            return float('-inf')
        if vozlisce.kljuc == podatek:
            return podatek
        elif vozlisce.kljuc < podatek:
            return self.ceil(podatek, vozlisce.desni)
        else:
            vrednost = self.ceil(podatek, vozlisce.levi)
            if vrednost is not None and vrednost >= podatek:
                return vrednost
            else:
                return vozlisce.kljuc
# =====================================================================@012835=
# 9. podnaloga
# Sestavite metodo `izbrisi_minimum(self)`, ki v iskalnem drevesu
# izbriše najmanjši ključ. Če je drevo prazno, naj metoda ne naredi
# ničesar. Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.izbrisi_minimum()
#     >>> d
#     Vozlisce(6,
#         levo = Vozlisce(4,
#                     levo = Vozlisce(3),
#                     desno = Vozlisce(5)),
#         desno = Vozlisce(9,
#                         levo = Vozlisce(7),
#                         desno = Vozlisce()))
# =============================================================================
    def izbrisi_minimum(self,vozlisce=None):
        '''izbrise minimum'''
        if self.prazno(): return
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.levi.prazno():
            if not vozlisce.oce:
                if vozlisce.desni.prazno():
                    self.koren = None
                else:
                    self.koren = vozlisce.desni
            else:
                vozlisce.oce.levi = vozlisce.desni
            return
        else:
            return self.izbrisi_minimum(vozlisce.levi)
# =====================================================================@012836=
# 10. podnaloga
# Sestavite metodo `izbrisi_maksimum(self)`, ki v iskalnem drevesu
# izbriše največji ključ. Če je drevo prazno, naj metoda ne naredi
# ničesar. Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.izbrisi_maksimum()
#     >>> d
#     Vozlisce(6,
#         levo = Vozlisce(4,
#                     levo = Vozlisce(1,
#                                     levo = Vozlisce(),
#                                     desno = Vozlisce(3)),
#                     desno = Vozlisce(5)),
#         desno = Vozlisce(7))
# =============================================================================
    def izbrisi_maksimum(self,vozlisce=None):
        '''izbrise maksimalen element'''
        if self.prazno(): return
        if not vozlisce:
            vozlisce = self.koren
        if vozlisce.desni.prazno():
            if not vozlisce.oce:
                if vozlisce.levi.prazno():
                    self.koren = None
                else:
                    self.koren = vozlisce.levi
            else:
                vozlisce.oce.desni = vozlisce.levi
            return
        else:
            return self.izbrisi_maksimum(vozlisce.desni)
# =====================================================================@012837=
# 11. podnaloga
# Sestavite metodo `izbrisi(self, podatek)`, ki v iskalnem drevesu
# izbriše ključ 'podatek' po Hibbardovemu algoritmu. Zgled:
# 
#     >>> d = IskalnoDrevo()
#     >>> for x in [6, 9, 4, 7, 5, 1, 3]:
#     >>>     d.vstavi(x)
#     >>> d.izbrisi(6)
#     >>> d
#     Vozlisce(7,
#         levo = Vozlisce(4,
#                     levo = Vozlisce(1,
#                                     levo = Vozlisce(),
#                                     desno = Vozlisce(3)),
#                     desno = Vozlisce(5)),
#         desno = Vozlisce(9))
# =============================================================================
    def izbrisi(self, podatek):
        '''izbriše podatek po hibbardovem algoritmu'''
        vozlisce = self.vrni(podatek)
        if vozlisce.prazno():
            return
        if not vozlisce.oce:
            sin = None
        elif vozlisce.oce.levi == vozlisce:
            sin = 'l'
        else:
            sin = 'd'
        if vozlisce.levi.prazno() and vozlisce.desni.prazno():
            if not sin:
                self.koren = None
            elif sin == 'l':
                vozlisce.oce.levi = Vozlisce()
            else:
                vozlisce.oce.desni = Vozlisce()
        elif vozlisce.levi.prazno():
            if not sin:
                self.koren = vozlisce.desni
            elif sin == 'l':
                vozlisce.oce.levi = vozlisce.desni
            else:
                vozlisce.oce.desni = vozlisce.desni
        elif vozlisce.desni.prazno():
            if not sin:
                self.koren = vozlisce.levi
            elif sin == 'l':
                vozlisce.oce.levi = vozlisce.levi
            else:
                vozlisce.oce.desni = vozlisce.levi
        else:
            nasl_kljuc = self.naslednik(vozlisce.kljuc)
            nasl = self.vrni(nasl_kljuc)
            if nasl.oce == self.koren:
                self.koren.desni = nasl.desni
            else:
                nasl.oce.levi = nasl.desni
            if not sin:
                self.koren.kljuc = nasl_kljuc
            elif sin == 'l':
                vozlisce.oce.levi.kljuc = nasl_kljuc
            else:
                vozlisce.oce.desni.kljuc = nasl_kljuc
