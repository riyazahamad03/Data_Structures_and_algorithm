class solution:
    def numDistinct(self, s: str, t: str):
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        for idex in range(len(t) + 1):
            dp[len(s)][idex] = 0
        for idex in range(len(s) + 1):
            dp[idex][len(t)] = 1
        
        for r in range(len(s)-1 ,-1 ,-1):
            for c in range(len(t)-1, -1 ,-1):
                if s[r] == t[c]:
                    dp[r][c] = dp[r + 1][c +1] + dp[r +1][c]
                else:
                    dp[r][c] = dp[r + 1][c]
        return dp[0][0]
x = solution()
print(x.numDistinct("babgbag" , "bag"))
print(x.numDistinct("rabbbit" , "rabbit"))