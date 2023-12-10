class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows, cols = len(matrix), len(matrix[0])
        tmp = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                tmp[c][r] = matrix[r][c]
        return tmp


x = Solution()
print(x.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
