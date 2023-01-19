import math
class solution:
    def minEatingSpeed(self,piles:list[list[int]],h:int):
        l,r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r)//2
            Sum = 0
            for i in range(len(piles)):
                Sum += math.ceil(piles[i]/m)
            if Sum <= h:
                res = min(res,m)
                r = m - 1
            else:
                l = m + 1
        return res
x = solution()
print(x.minEatingSpeed([3,6,7,11],8))