class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        if k == 0:
            return 1
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for N in range(1, n + 1):
            tot = 0
            for K in range(k + 1):
                if K >= N:
                    tot -= dp[N - 1][K - N]
                tot += dp[N - 1][K]
                dp[N][K] = tot % mod
        return dp[n][k]


x = Solution()
print(x.kInversePairs(1000, 1000))
