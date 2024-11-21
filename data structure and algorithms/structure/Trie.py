class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
    
    def startsWith(self, prefix: str):
        cur = self.root

        for c in prefix : 
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

word = "test"
obj = Trie()
obj.insert(word)
param2 = obj.search(word)
print(param2)
print(obj.startsWith("t")) #True, cz test's predix = t