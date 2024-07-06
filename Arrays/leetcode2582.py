class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        row = time // (n - 1)
        pos = time % (n - 1)
        if row % 2 == 0:
            return pos + 1
        else:
            return n - pos


x = Solution()
print(x.passThePillow(n=4, time=5))
