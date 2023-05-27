class solution:
    def stoneGameIII(self , stoneValue : list[int]):
        dp = {}
        def dfs(idex):
            if idex == len(stoneValue):
                return 0
            if idex in dp:
                return dp[idex]
            res = float("-inf")
            for j in range(idex , min(idex + 3 , len(stoneValue))):
                res = max(res , sum(stoneValue[idex : j + 1]) - dfs(j + 1))
            dp[idex] = res
            return res
        return "Alice" if dfs(0) > 0 else ("Bob" if dfs(0) < 0 else "Tie")
x = solution()
print(x.stoneGameIII([1,2,3,-9]))