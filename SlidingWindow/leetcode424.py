class solution:
    def charReplacement(self,s:str,k:int):
        d,l = {},0
        maxf,res = 0,0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r],0)
            maxf = max(maxf,d[s[r]])

            if (r-l+1) - maxf > k:
                d[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
        return res
x = solution()
print(x.charReplacement("ABAB",2))