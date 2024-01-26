class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        rows, cols = m, n
        mod = 10**9 + 7
        cache = {}

        def dfs(r, c, moves):
            if (r, c, moves) in cache:
                return cache[(r, c, moves)]

            if r == rows or c == cols or r < 0 or c < 0:
                return 1
            if moves == 0:
                return 0

            cache[(r, c, moves)] = (
                dfs(r + 1, c, moves - 1)
                + dfs(r, c + 1, moves - 1)
                + dfs(r - 1, c, moves - 1)
                + dfs(r, c - 1, moves - 1)
            ) % mod
            return cache[(r, c, moves)]

        return dfs(startRow, startColumn, maxMove)


x = Solution()
print(x.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
