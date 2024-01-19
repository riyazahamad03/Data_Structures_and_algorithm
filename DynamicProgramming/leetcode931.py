class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = [matrix[0][i] for i in range(n)]
        for i in range(1, n):
            newDp = [0] * (n)
            for j in range(n):
                v1 = dp[j]
                if j - 1 >= 0:
                    v1 = min(v1, dp[j - 1])
                if j + 1 < n:
                    v1 = min(v1, dp[j + 1])
                newDp[j] = v1 + matrix[i][j]
            dp = newDp

        return min(dp)


x = Solution()
print(x.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
