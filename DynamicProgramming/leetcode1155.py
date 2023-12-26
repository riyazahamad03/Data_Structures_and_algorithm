class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        mod = 10**9 + 7

        def dfs(idx, pts):
            if idx == n:
                return 1 if target == pts else 0
            if pts > target:
                return 0
            if (idx, pts) in dp:
                return dp[(idx, pts)]
            res = 0
            for i in range(1, k + 1):
                res += dfs(idx + 1, pts + i)
            dp[(idx, pts)] = res % mod
            return dp[(idx, pts)]

        return dfs(0, 0)


x = Solution()
print(x.numRollsToTarget(n=30, k=30, target=500))
