class solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[float('inf') for _ in range(len(w2) + 1)]
              for _ in range(len(w1) + 1)]

        for idex in range(len(w2) + 1):
            dp[len(w1)][idex] = len(w2) - idex
        for idex in range(len(w1) + 1):
            dp[idex][len(w2)] = len(w1)-idex

        for r in range(len(w1)-1, -1, -1):
            for c in range(len(w2)-1, -1, -1):
                if w1[r] == w2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c + 1],
                                       dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]


x = solution()
print(x.minDistance("horse", "ros"))
