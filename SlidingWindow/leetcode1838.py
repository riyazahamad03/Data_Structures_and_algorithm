class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        curr = 0
        res = 0
        while r < len(nums):
            tar = nums[r]
            curr += nums[r]
            if ((r - l + 1) * tar) - curr > k:
                curr -= nums[l]
                l += 1
            res = max(res, (r - l + 1))

            r += 1
        return res


x = Solution()
print(x.maxFrequency(nums=[1, 2, 4], k=5))
