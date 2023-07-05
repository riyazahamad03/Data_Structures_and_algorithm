class solution:
    def longestSubArray(self, nums: list[int]):
        l, zeros, res = 0, 1, 0
        for r in range(len(nums)):
            if not nums[r]:
                zeros -= 1
            while zeros < 0 and l <= r:
                if not nums[l]:
                    zeros += 1
                l += 1
            res = max(res, r - l)
        return res


x = solution()
print(x.longestSubArray([1, 1, 0, 1]))
