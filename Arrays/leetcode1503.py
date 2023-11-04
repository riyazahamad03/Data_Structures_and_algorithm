class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        res = 0
        for num in left:
            res = max(res, num)
        for num in right:
            res = max(res, n - num)
        return res


x = Solution()
print(x.getLastMoment(n=4, left=[4, 3], right=[0, 1]))
