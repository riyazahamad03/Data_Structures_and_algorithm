class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = [grid[0][i] for i in range(n)]

        for r in range(1, n):
            curr = dp.copy()
            for c in range(n):
                elem = grid[r][c]
                mini = float("inf")
                for k in range(n):
                    if k != c:
                        mini = min(mini, elem + dp[k])
                curr[c] = mini
            dp = curr
        return min(dp)


x = Solution()
print(x.minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
