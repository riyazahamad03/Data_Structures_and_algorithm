class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        curr = 0
        res = -1
        for r in range(0, len(nums)):
            if curr > nums[r]:
                res = max(res, curr + nums[r])
            curr += nums[r]
        return res


x = Solution()
print(x.largestPerimeter([1, 12, 1, 2, 5, 50, 3]))
