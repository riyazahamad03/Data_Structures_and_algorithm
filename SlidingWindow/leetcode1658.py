class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tar = sum(nums) - x
        l, r = 0, 0
        res = float("inf")
        currSum = 0
        while r < len(nums):
            currSum += nums[r]
            while l <= r and currSum > tar:
                currSum -= nums[l]
                l += 1
            if currSum == tar:
                res = min(res, len(nums) - (r - l + 1))
            r += 1
        return res if res != float("inf") else -1


x = Solution()
print(x.minOperations(nums=[1, 1, 4, 2, 3], x=5))
