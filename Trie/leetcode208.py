'''
208. Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) : Inserts the string word into the trie.
boolean search(String word) : Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) : Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.



input : ["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

output : [null,null,true,false,true,null,true]
'''

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.lastWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for e in word:
            indices = ord(e) - ord('a')
            if curr.child[indices] == None:
                curr.child[indices] = TrieNode()
            curr = curr.child[indices]
        curr.lastWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for e in word:
            indices = ord(e) - ord('a')
            if curr.child[indices] == None:
                return False
            curr = curr.child[indices]
        return curr.lastWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for e in prefix:
            indices = ord(e) - ord('a')
            if curr.child[indices] == None:
                return False
            curr = curr.child[indices]
        return True


Obj = Trie()
Obj.insert('apple')
print(Obj.search('apple'))
print(Obj.startsWith("app"))


