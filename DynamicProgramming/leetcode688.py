class solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]
        dp = {}

        def dfs(moves, r, c):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if moves == 0:
                return 1

            key = str(r) + "ri" + str(c) + "ya" + str(moves)
            if key in dp:
                return dp[key]

            prob = 0
            for dr, dc in directions:
                prob += dfs(moves - 1, r + dr, c + dc)

            dp[key] = prob/8.0
            return dp[key]
        return dfs(k, row, column)


x = solution()
print(x.knightProbability(n=3, k=2, row=0, column=0))
