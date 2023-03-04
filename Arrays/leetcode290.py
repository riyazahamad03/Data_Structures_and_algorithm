class Solution:
    def wordPattern(self,pattern:str,s:str):
        words = s.split(" ")
        wToC = {}
        cToW = {}

        if len(pattern) != len(words):
            return False
        
        for c,w in zip(pattern , words):
            if w in wToC and wToC[w] != c:
                return False
            if c in cToW and cToW[c] != w:
                return False
            
            wToC[w] = c
            cToW[c] = w
        return True
x = Solution()
print(x.wordPattern("abba","dog cat cat dog"))