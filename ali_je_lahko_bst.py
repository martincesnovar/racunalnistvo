from sklad import Sklad
 
def je_lahko_BST(pre):
    '''preveri ali premi pregled lahko predstavlja dvojiško iskalno drevo'''
    s = Sklad()
 
    # Trenutni koren = -inf
    koren = float('-inf')
 
    # Sprehodi se čez seznam
    for vrednost in pre: 
        #Opomba:vrednost = pre[i] po
        #danem algoritmu   
     
        # Če najdemo vrednost, ki je manjša od korena, vrni False
        if vrednost < koren :
            return False
     
        # Če je vrednost(pre[i]) v desnem poddrevesu
        # Odstrani elemente, ki so manjši kot je koren
        # in naredi zadnjega kot koren
        while not s.prazen() and s.vrh() < vrednost :
            koren = s.vrh()
            s.odstrani()
         
        # Na tej točki je sklad prazen ali je vrednost manjša
        # od korena, vstavi vrendost
        s.vstavi(vrednost)
 
    return True


pre1 = [40 , 30 , 35 , 80 , 100]

pre3 = [8,4,2,1,6,5,10,9,30,11]
pre4 = [1,2,3]
pre5 = [8,10,9,30,11]
pre6 = [3,2,1]
pre7 = [3,1,2]
pre2 = [40 , 30 , 35 , 20 ,  80 , 100]
pre8 = [8,4,10,2]
pre9 = [8,4,2,1,6,5,10,7,30,11]
pre10 = [1,2,4,1]

print (je_lahko_BST(pre1))
print (je_lahko_BST(pre7))
print (je_lahko_BST(pre3))
print (je_lahko_BST(pre4))
print (je_lahko_BST(pre5))
print (je_lahko_BST(pre6))
print (je_lahko_BST(pre2))
print (je_lahko_BST(pre8))
print (je_lahko_BST(pre9))
print (je_lahko_BST(pre10))

