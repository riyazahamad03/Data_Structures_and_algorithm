class solution:
    def mostPointsWithRecurrsion(self, questions: list[list[int]]):
        # time complexity O(2^n) might fail at some point
        def dfs(i, tot):
            if i >= len(questions):
                return tot
            return max(
                dfs(i + 1 + questions[i][1], questions[i][0] + tot),
                dfs(i + 1, tot)
            )
        return dfs(0 , 0)
    def mostPointsWithRecurrsionAndMemoization(self, questions: list[list[int]]):
        # timeComplexity O(m * n) with memoization somewhat efficient
        dp = {}
        def dfs(i , tot):
            if i >= len(questions):
                return tot
            if (i , tot) in dp:
                return dp[(i ,tot)]
            dp[(i ,tot)] = max(
                dfs(i + 1 + questions[i][1] ,questions[i][0] + tot),
                dfs(i + 1 , tot)
                
            )
            return dp[(i ,tot)]
        return dfs(0 , 0)
    def mostPointsWithTrueDp(self, questions: list[list[int]]):
        # time complexity O(N) best possible solution we can get 
        dp = [0] * (len(questions) + 1)
        for i in range(len(questions) - 1, -1 , -1):
            pts , idex = questions[i]
            if(i + 1 + idex < len(questions)):
                dp[i] = max(pts + dp[i + 1 + idex] , dp[i + 1])
            else:
                dp[i] = max(pts , dp[i + 1])
        return dp[0]
x = solution()
print(x.mostPointsWithRecurrsion([[3,2],[4,3],[4,4],[2,5]]))
print(x.mostPointsWithRecurrsionAndMemoization([[3,2],[4,3],[4,4],[2,5]]))
print(x.mostPointsWithTrueDp([[3,2],[4,3],[4,4],[2,5]]))