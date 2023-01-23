class solution:
    def countSubstring(self,s:str):
        res = 0
        for i in range(len(s)):
            res += self.countP(i,i,s)
            res += self.countP(i,i+1,s)
        return res

    def countP(self,l,r,s):
        res = 0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res += 1
            l -= 1
            r += 1
        return res
x = solution()
print(x.countSubstring('aaa'))