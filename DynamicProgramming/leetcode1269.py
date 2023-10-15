class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        res = 0
        dp = {}

        def dfs(i, ptr):
            if i > arrLen:
                return 0
            if ptr == steps:
                return 1 if i == 0 else 0
            if (i, ptr) in dp:
                return dp[(i, ptr)]
            res = 0
            if i > 0:
                res += dfs(i - 1, ptr + 1)
            if i < arrLen - 1:
                res += dfs(i + 1, ptr + 1)
            res += dfs(i, ptr + 1)
            dp[(i, ptr)] = res
            return dp[(i, ptr)]

        return dfs(0, 0) % (10 ** 9 + 7)


x = Solution()
print(x.numWays(steps=3, arrLen=2))
