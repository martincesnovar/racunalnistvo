#https://brilliant.org/wiki/tries/
class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, value):
        '''vstavi besedo in vrednost'''
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            else:
                newNode = Node()
                newNode.key = currentWord[0]
                if len(currentWord) == 1:
                    newNode.value = value
                currentNode.children[currentWord[0]] = newNode
                currentNode = newNode
                currentWord = currentWord[1:]

    def lookup(self, word):
        '''išči - vrne vrednost, če je v trie'''
        currentWord = word
        currentNode = self.root
        while len(currentWord) > 0:
            if currentWord[0] in currentNode.children:
                currentNode = currentNode.children[currentWord[0]]
                currentWord = currentWord[1:]
            else:
                return "Not in trie"
        if currentNode.value == None:
            return "None"
        return currentNode.value

    def yieldAllNodes(self):
        '''sprehodi se čez vozlišča'''
        nodes = [self.root]
        while len(nodes) > 0:
            for letter in nodes[0].children:
                nodes.append(nodes[0].children[letter])
            yield nodes.pop(0).key

def makeTrie(words):
    '''vrne trie'''
    trie = Trie()
    for word, value in words.items():
        trie.insert(word, value)
    return trie

if __name__=='__main__':
    trie = makeTrie({'hello': 5, 'hat': 7})
    print(trie.lookup('nope'),
          trie.lookup('hello'),
          list(trie.yieldAllNodes()),
          sep='\n')
