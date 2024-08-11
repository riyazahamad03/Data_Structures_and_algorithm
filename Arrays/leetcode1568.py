class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return
            visit.add((r, c))
            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in neighbors:
                dfs(nr, nc, visit)

        visit = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visit:
                    dfs(r, c, visit)
                    count += 1
        if count == 0 or count > 1:
            return 0
        land = list(visit)
        for r, c in land:
            grid[r][c] = 0

            visit = set()
            count = 0
            for r2 in range(rows):
                for c2 in range(cols):
                    if grid[r2][c2] and (r2, c2) not in visit:
                        dfs(r2, c2, visit)
                        count += 1
            if count != 1:
                return 1
            grid[r][c] = 1
        return 2


x = Solution()
print(x.minDays(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
