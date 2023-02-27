class solution:
    def isHappy(self,n:int)->bool:
        def soS(k):
            SoS = 0
            while k:
                SoS += (k%10) ** 2
                k//=10
            return SoS
        visitedSet = set()
        while n not in visitedSet:
            visitedSet.add(n)
            n = soS(n)
            if n==1:
                return True
        return False
x = solution()
print(x.isHappy(19))