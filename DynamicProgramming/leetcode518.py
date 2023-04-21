class solution:
    def change(self, amount: int, coins: list[int]):
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0] 

        dp = {}

        def dfs(idex, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if idex == len(coins):
                return 0
            if (idex, a) in dp:
                return dp[(idex, a)]
            dp[(idex, a)] = dfs(idex, a + coins[idex]) + dfs(idex + 1, a)
            return dp[((idex, a))]
        return dfs(0, 0)


x = solution()
print(x.change(5, [1, 2, 5]))
