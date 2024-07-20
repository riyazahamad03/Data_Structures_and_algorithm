class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        rows, cols = len(rowSum), len(colSum)
        res = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            res[r][0] = rowSum[r]

        for c in range(cols):
            curr_col_sum = 0
            for r in range(rows):
                curr_col_sum += res[r][c]
            r = 0
            while curr_col_sum > colSum[c]:
                diff = curr_col_sum - colSum[c]
                mx_shift = min(res[r][c], diff)
                res[r][c] -= mx_shift
                res[r][c + 1] += mx_shift
                curr_col_sum -= mx_shift
                r += 1
        return res


x = Solution()
print(x.restoreMatrix(rowSum=[3, 8], colSum=[4, 7]))
