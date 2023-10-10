class Solution:
    def minOperations(self, nums: list[int]) -> int:
        lgth = len(nums)
        nums = sorted(set(nums))
        res = lgth
        r = 0
        for l in range(len(nums)):
            while r < len(nums) and nums[r] < lgth + nums[l]:
                r += 1
            wdow = r - l
            res = min(res, lgth - wdow)
        return res


x = Solution()
print(x.minOperations([1, 10, 100, 1000]))
