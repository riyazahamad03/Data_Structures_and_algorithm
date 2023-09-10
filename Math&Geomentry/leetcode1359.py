class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2 * n
        res = 1
        while slots > 0:
            res *= slots * (slots - 1)//2
            slots -= 2
        return res % (10 ** 9 + 7)
x = Solution()
print(x.countOrders(2))