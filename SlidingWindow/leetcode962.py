class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        max_right = [0] * len(nums)
        i = len(nums) - 1
        prev_max = 0

        for n in reversed(nums):
            max_right[i] = max(n, prev_max)
            prev_max = max_right[i]
            i -= 1
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            res = max(res, r - l)
        return res


x = Solution()
print(x.maxWidthRamp([6, 0, 8, 2, 1, 5]))
