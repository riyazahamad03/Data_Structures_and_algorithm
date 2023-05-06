class solution:
    def numSubSeq(self, nums: list[int], target: int):
        mod = (10 ** 9) + 7
        nums.sort()
        r = len(nums) - 1
        res = 0
        for idex in range(len(nums)):
            left = nums[idex]
            while idex <= r and left + nums[r] > target:
                r -= 1
            if idex <= r:
                res += 2 ** (r - idex)
                res %= mod
        return res


x = solution()
print(x.numSubSeq([3, 5, 6, 7], 9))
