class solution:
    def combinationSum4(self, nums: list[int], target: int):
        nums.sort()
        dp = {}

        def dfs(n):
            if n in dp:
                return dp[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            res = 0
            for num in nums:
                if n - num < 0:
                    break
                res += dfs(n - num)
            dp[n] = res
            return res
        return dfs(target)


x = solution()
print(x.combinationSum4(nums=[1, 2, 3], target=4))
