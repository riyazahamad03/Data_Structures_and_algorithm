class solution:
    def LongestIncreasingPath(self , matrix : list[list[int]]):
        rows , cols = len(matrix) , len(matrix[0])
        dp = {}
        def dfs(r , c , prev):
            if (r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev):
                return 0
            if (r,c) in dp:
                return dp[(r , c)]
            resMax = 1
            resMax = max(resMax , 1 + dfs(r + 1 , c , matrix[r][c]))
            resMax = max(resMax , 1 + dfs(r - 1 , c , matrix[r][c]))
            resMax = max(resMax , 1 + dfs(r  , c + 1, matrix[r][c]))
            resMax = max(resMax , 1 + dfs(r  , c - 1, matrix[r][c]))
            dp[(r , c)] = resMax
            return dp[(r , c)]
        LIS = 0
        for r in range(rows):
            for c in range(cols):
                LIS = max(LIS , dfs(r , c , -1))
        return LIS
X = solution()
print(X.LongestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))