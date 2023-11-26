class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]
            curr = sorted(matrix[row], reverse=True)
            for i in range(cols):
                res = max(res, curr[i] * (i + 1))
        return res


x = Solution()
print(x.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
