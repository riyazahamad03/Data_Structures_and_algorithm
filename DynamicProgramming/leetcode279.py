class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if i - (j * j) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - j * j])
                else:
                    break
                j += 1
        return dp[n]


x = Solution()
print(x.numSquares(12))
