class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.lastWord = False
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.maxlen = 0
    def addword(self,word):
        self.maxlen = max(self.maxlen,len(word))
        curr = self.root
        for e in word:
            if e not in curr.child:
                curr.child[e] = TrieNode()
            curr = curr.child[e]
        curr.lastWord = True

    def search(self,word):
        if self.maxlen > len(word):
            return False
        
        def dfs(j,root):
            curr = root

            for i in range(j,len(word)):
                # 46 in ascii '.'
                if ord(word[i]) == 46:
                    for element in curr.child.values():
                        if dfs(i+1,element):
                            return True
                    return False

                else:
                    if word[i] not in curr.child:
                        return False
                    curr = curr.child[word[i]]
            return curr.lastWord
        
        return dfs(0,self.root)

Obj = Trie()
Obj.addword('bad')
print(Obj.search('..d'))

Obj.addword("potato")
print(Obj.search("...ato"))