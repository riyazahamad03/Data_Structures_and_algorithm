class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        flips = 0
        res = 0
        for i in range(len(nums)):
            if i - k >= 0 and nums[i - k] == 2:
                flips -= 1
            if (nums[i] + flips) % 2 == 0:
                if i + k > len(nums):
                    return -1
                res += 1
                flips += 1
                nums[i] = 2
        return res


x = Solution()
print(x.minKBitFlips(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3))
