class Solution:
    def countPaths(self, grid: list[list[int]]):
        ROWS, COLS = len(grid), len(grid[0])
        dp = {}
        mod = 10 ** 9 + 7

        def isValid(r, c, prev):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or prev >= grid[r][c]:
                return False
            return True
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1

            for dr, dc in directions:
                if isValid(dr + r, dc + c, grid[r][c]):
                    res += dfs(r + dr, c + dc)

            dp[(r, c)] = res % mod
            return dp[(r, c)]

        total_paths = 0
        for r in range(ROWS):
            for c in range(COLS):
                total_paths += dfs(r, c)

        return total_paths % mod


x = Solution()
print(x.countPaths([[1, 1], [3, 4]]))
