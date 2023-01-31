class solution:
    def __init__(self):
        self.res = []
    def plusOne(self,digits:list[int]):
        largeInt = 0
        for i in digits:
            largeInt = largeInt * 10 + i
        largeInt += 1
        self.resDig(largeInt)
        return self.res
    def resDig(self,n):
        if n==0:
            return
        r = n%10
        self.resDig(n//10)
        self.res.append(r)
x = solution()
print(x.plusOne([1,2,3]))