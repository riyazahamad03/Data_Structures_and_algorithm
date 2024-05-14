class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            tmp = grid[r][c]
            grid[r][c] = 0
            res = tmp
            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nei_r, nei_c in neighbors:
                res = max(res, tmp + dfs(nei_r, nei_c))
            grid[r][c] = tmp
            return res

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))
        return ans


x = Solution()
print(x.getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
