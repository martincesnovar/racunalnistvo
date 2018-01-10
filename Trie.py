class TrieVozel:
    '''
    Trie vozel
    '''
    def __init__(self):
        self.naslednji  = [None] * 26
        self.vrednost = 0
 
    def list_vozel(self):
        '''Preveri, ali je list (konec besede)'''
        return self.vrednost != 0
 
    def je_prosti_vozel(self):
        '''ali vozel nima naslednjega'''
        for c in self.naslednji:
            if c:return False
        return True
 
 
class Trie:
    '''
    Trie
    '''
    def __init__(self):
        self.root = self.ustvari_vozel()
        self.stej = 0 #stevilo kljucev vstavljenih v Trie
 
    def _Index(self,ch):
        '''pretvori znak v index, dovoljeni znaki a-z'''
        return ord(ch)-ord('a')
 
    def ustvari_vozel(self):
        '''Ustvari nov prazen vozel'''
        return TrieVozel()
 
    def vstavi(self, kljuc):
        '''ce kljuc ne obstaja, ga ustvari'''
        dolzina = len(kljuc)
        vrh = self.root
        self.stej += 1
 
        for level in range(dolzina):
            index = self._Index(kljuc[level])
 
            if vrh.naslednji[index]:
                # preskoci trenutni vozel
                vrh = vrh.naslednji[index]
            else:
                # doda nov vozel
                vrh.naslednji[index] = self.ustvari_vozel()
                vrh = vrh.naslednji[index]
 
        # oznaci zadnji vozel kot list (!=0)
        vrh.vrednost = self.stej
 
    def isci(self, kljuc):
        '''
        Išče ključ v trie
        vrne true če ključ obstaja sicer false
        '''
        dolzina = len(kljuc)
        vrh = self.root
        for level in range(dolzina):
            index = self._Index(kljuc[level])
            if not vrh.naslednji[index]:
                return False
            vrh = vrh.naslednji[index]
 
        return vrh != None and vrh.vrednost != 0
 
 
    def _zbrisi_kljuc(self, vozel, kljuc, level, dolzina):
        '''Rekruzivno izbrisi dovoljene vozle'''
        if vozel:
            if level == dolzina:
                if vozel.vrednost:
                    # odznaci list
                    vozel.vrednost = 0
 
                # vozel bo izbrisan
                return vozel.je_prosti_vozel()
            else:
                index = self._Index(kljuc[level])
                if self._zbrisi_kljuc(vozel.naslednji[index], \
                                      kljuc, level + 1, dolzina):
 
                    #odstrani zadnji vozel 
                    del vozel.naslednji[index]
 
                    # rekruzivno se pomikaj gor in izbrisi dovoljene vozle
                    return (not vozel.list_vozel() and \
                            vozel.je_prosti_vozel())
 
        return False
 
    def zbrisi(self, kljuc):
        '''Zbrisi kljuc iz trie'''
        dolzina = len(kljuc)
        if dolzina > 0:
            self._zbrisi_kljuc(self.root, kljuc, 0, dolzina)

 
def main():
    keys = ["sells","sheer", "code", "le", "leet", "komutativno", "konkurenca"]
    trie = Trie()
    for key in keys:
        trie.vstavi(key)
 
    trie.zbrisi(keys[0])
 
    print("{} {}".format(keys[0],\
        "Je v Trie" if trie.isci(keys[0]) \
                        else "ni v trie"))
 
    print("{} {}".format(keys[6],\
        "Je v trie" if trie.isci(keys[6]) \
                        else "ni v trie"))
 
if __name__ == '__main__':
    main()
