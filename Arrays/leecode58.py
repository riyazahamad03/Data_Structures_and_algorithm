class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res,l = [],''
        for i in range(len(s)):
            if ((ord(s[i]) >= 97 and ord(s[i])<=122) or (ord(s[i])>=65 and ord(s[i])<=90)):
                l += s[i]
            if l and (i == len(s)-1 or ord(s[i]) == 32):
                res.append(l)
                l = ''
        return len(res[-1])
    def lengthOfLastWord1(self, s: str) -> int:
        i,res = len(s)-1,0
        while ord(s[i]) == 32:
            i-=1
        while i>=0 and ord(s[i])!=32:
            res+=1
            i-=1
        return res
x = Solution()
print(x.lengthOfLastWord1('   fly me   to   the moon  '))