class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        rowOnes, colOnes = [0] * rows, [0] * cols

        for r in range(rows):
            rOnes = 0
            for c in range(cols):
                rOnes += grid[r][c]
            rowOnes[r] = rOnes
        for c in range(cols):
            cOnes = 0
            for r in range(rows):
                cOnes += grid[r][c]
            colOnes[c] = cOnes
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                oneRow, oneCol = rowOnes[r], colOnes[c]
                zeroRow, zeroCol = rows - oneRow, cols - oneCol

                res[r][c] = oneRow + oneCol - zeroRow - zeroCol
        return res


x = Solution()
print(x.onesMinusZeros([[1, 1, 1], [1, 1, 1]]))
