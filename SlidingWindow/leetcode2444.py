class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        bad = left = right = -1
        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                bad = i
            if nums[i] == minK:
                left = i
            if nums[i] == maxK:
                right = i
            res += max(0 , min(left , right) - bad)
        return res
x = Solution()
print(x.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))