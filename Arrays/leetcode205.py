class solution:
    def isIso(self,s:str,t:str):
        st,ts = {},{}
        for i in range(len(s)):
            c1,c2 = s[i],t[i]

            if((c1 in st and st[c1]!=c2 ) or (c2 in ts and ts[c2]!=c1)):
                return False
            st[c1] = c2
            ts[c2] = c1
        return True
x = solution()
print(x.isIso("egg","add"))