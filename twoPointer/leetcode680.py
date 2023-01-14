# 680. Valid Palindrome II
class solution:
    def validPalindrome(self,s:str):
        def checkValid(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l,r = l+1,r-1
            return True
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return (checkValid(l+1,r) or checkValid(l,r-1))
            l,r=l+1,r-1
        return True
x = solution()
print(x.validPalindrome("aaabbbaaabbb"))