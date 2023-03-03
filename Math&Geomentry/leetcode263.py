class Solution:
    def isUglyNumber(self,n:int):
        if n <= 0:
            return False
        pFac,i = [2,3,5],0
        while n>1:
            if i >= len(pFac):
                return False
            if n%pFac[i]==0:
                n = n//pFac[i]
            else:
                i += 1
        return True
x = Solution()
print(x.isUglyNumber(5))