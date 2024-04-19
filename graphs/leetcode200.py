class Solution:
    def numIslands(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, visit):
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            dfs(r - 1, c, visit)
            # visit.remove((r , c))
            return

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c, visit)
                    res += 1
        return res


x = Solution()
print(
    x.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
