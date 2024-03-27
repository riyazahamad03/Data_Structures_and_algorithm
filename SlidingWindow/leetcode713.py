class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k == 1:
            return 0
        l, r = 0, 0
        n = len(nums)
        res = 0
        currProd = nums[0]
        while l < n and r < n:

            if currProd < k:
                r += 1
                if r > l:
                    res += r - l
                if r < n:
                    currProd *= nums[r]

            else:
                currProd //= nums[l]
                l += 1
        return res


x = Solution()
print(x.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
