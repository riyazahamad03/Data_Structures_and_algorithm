# 5. Longest Palindromic Substring
class solution:
    def longestPalindrom(self,s:str):
        res = ""
        Len = 0
        for i in range(len(s)):
            # odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l + 1) > Len:
                    res = s[l : r+1]
                    Len = r-l+1
                l -= 1
                r += 1
            # even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > Len:
                    res = s[l : r+1]
                    Len = r-l+1
                l -= 1
                r += 1
        return res

x = solution()
print(x.longestPalindrom('ccc'))