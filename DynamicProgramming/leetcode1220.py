class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
        mod = 10**9 + 7
        for idx in range(2, n + 1):
            newDp = dp.copy()
            newDp[0] = (dp[1] + dp[4] + dp[2]) % mod
            newDp[1] = (dp[0] + dp[2]) % mod
            newDp[2] = (dp[1] + dp[3]) % mod
            newDp[3] = (dp[2]) % mod
            newDp[4] = (dp[2] + dp[3]) % mod
            dp = newDp
        return sum(dp.values()) % mod


x = Solution()
print(x.countVowelPermutation(10))
