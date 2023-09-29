class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        def isInc(nums):
            l, r = 0, 1
            while r < len(nums):
                if nums[l] > nums[r]:
                    return False
                l, r = l + 1, r + 1
            return True

        def isDec(nums):
            l, r = 0, 1
            while r < len(nums):
                if nums[l] < nums[r]:
                    return False
                l, r = l + 1, r + 1
            return True

        return isInc(nums) or isDec(nums)


x = Solution()
print(x.isMonotonic(nums=[1, 2, 2, 3]))
