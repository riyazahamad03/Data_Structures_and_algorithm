# 392. Is Subsequence
class solution:
    def isSubsequence(self,s:str,t:str):
        j = 0
        if not s:
            return True
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if j == len(s):
                return True
        return False
        
    def isSubsequence2(self,s:str,t:str):
        i,j = 0,0
        while( i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False
x = solution()
print(x.isSubsequence("","ahbgdc"))
print(x.isSubsequence2("agt","ahbgdc"))