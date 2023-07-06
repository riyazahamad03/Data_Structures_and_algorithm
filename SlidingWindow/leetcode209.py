class solution:
    def minSubArrayLen(self, target: int, nums: list[int]):
        res, prefixSum, l = float("inf"), 0, 0
        for r in range(len(nums)):
            prefixSum += nums[r]
            while prefixSum >= target:
                res = min(res, r - l + 1)
                prefixSum -= nums[l]
                l += 1
        return res if res != float("inf") else 0


x = solution()
print(x.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))

print(x.minSubArrayLen(target=4, nums=[1, 4, 4]))

print(x.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
