class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4],
        ]

        mod = 10**9 + 7
        # cache = {}
        # def dfs(rem , sq):
        #     if rem == 0:
        #         return 1
        #     if (rem , sq) in cache:
        #         return cache[(rem , sq)]
        #     ans = 0
        #     for next_square in jumps[sq]:
        #         ans = (ans + dfs(rem - 1, next_square)) % mod
        #     cache[(rem , sq)] = ans
        #     return ans

        # res = 0
        # for idx in range(10):
        #     res = (res + dfs(n - 1 , idx))% mod
        # return res
        dp = [1] * (10)
        for _ in range(n - 1):
            nextDp = [0] * (10)
            for i in range(10):
                for j in jumps[i]:
                    nextDp[j] = (nextDp[j] + dp[i]) % mod
            dp = nextDp
        return sum(dp) % mod


x = Solution()
print(x.knightDialer(3131))