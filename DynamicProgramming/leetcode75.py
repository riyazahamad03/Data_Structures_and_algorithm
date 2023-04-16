class solution:
    def climbingStairs(self , n : int):
        dp = [-1] * n
        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if dp[i] != -1:
                return dp[i]
            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]
        return dfs(0)
    def climbingStairs2(self , n : int):
        oneStep , twoStep = 1 , 1
        for _ in range(n - 1):
            temp = oneStep
            oneStep = oneStep + twoStep
            twoStep = temp
        return oneStep

x = solution()
print(x.climbingStairs(5))
print(x.climbingStairs2(5))