class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] = 0 if grid[r][c] else 1
        for c in range(cols):
            one = 0
            for r in range(rows):
                one += grid[r][c]
            if one < rows - one:
                for r in range(rows):
                    grid[r][c] = 0 if grid[r][c] else 1
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    res += 2 ** (cols - c - 1)
        return res


x = Solution()
print(x.matrixScore(grid=[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
