class solution:
    def longestArithmeticSeq(self, nums: list[int]):
        dp = {}
        for r in range(len(nums)):
            for l in range(0, r):
                dp[(l, nums[l] - nums[r])] = 1 + \
                    dp.get((r, nums[l] - nums[r]), 1)
        return max(dp.values())


x = solution()
print(x.longestArithmeticSeq([3, 6, 9, 12]))
