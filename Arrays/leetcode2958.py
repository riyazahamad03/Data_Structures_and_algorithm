class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        Map = {}
        n = len(nums)
        res, l = 0, 0
        for r in range(n):
            val = nums[r]
            Map[val] = 1 + Map.get(val, 0)

            while l < r and Map[val] > k:
                Map[nums[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


x = Solution()
print(x.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
