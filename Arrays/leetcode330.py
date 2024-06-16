class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        patch = 0
        curr_sum = 0
        idx = 0
        while curr_sum < n:
            if idx < len(nums) and nums[idx] <= curr_sum + 1:
                curr_sum += nums[idx]
                idx += 1
            else:
                curr_sum += curr_sum + 1
                patch += 1
        return patch


x = Solution()
print(x.minPatches(nums=[1, 5, 10], n=20))
