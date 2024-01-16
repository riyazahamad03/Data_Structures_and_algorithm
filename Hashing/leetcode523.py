class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefSum = {0: -1}
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]

            if curr % k in prefSum and i - prefSum[curr % k] > 1:
                return True

            if curr % k not in prefSum:
                prefSum[curr % k] = i
        return False


x = Solution()
print(x.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
