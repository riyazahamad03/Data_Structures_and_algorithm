class solution:
    def posFind(self, dp, tar):
        l, r = 0, len(dp) - 1
        while l <= r:
            mid = (l + r) // 2
            if dp[mid] <= tar:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def longestObstacleCourseAtEachPosition(self, nums: list[int]):
        dp = [float("inf")] * (len(nums) + 1)
        res = [1] * len(nums)
        for i, num in enumerate(nums):
            idex = self.posFind(dp, num)
            res[i] = idex + 1
            dp[idex] = num
        return res


x = solution()
print(x.longestObstacleCourseAtEachPosition([1, 2, 3, 2]))
print(x.longestObstacleCourseAtEachPosition([2, 2, 1]))
print(x.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]))
