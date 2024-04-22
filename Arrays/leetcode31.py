class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # find the breakpoint index
        def getBreakPoint(nums):
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    return i
            return -1

        def revv(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        idx = getBreakPoint(nums)
        if idx == -1:
            revv(0, len(nums) - 1)
        else:
            # find the increasing part
            for j in range(len(nums) - 1, idx, -1):
                if nums[idx] < nums[j]:
                    nums[idx], nums[j] = nums[j], nums[idx]
                    break
            revv(idx + 1, len(nums) - 1)


x = Solution()
print(x.nextPermutation([3, 2, 1]))
