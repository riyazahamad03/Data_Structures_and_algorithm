class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lft = self.binSearch(nums, target, True)
        rgh = self.binSearch(nums, target, False)
        return [lft, rgh]

    def binSearch(self, nums, target, oneSided):
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            m = (l + r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                idx = m

                if oneSided:
                    r = m - 1
                else:
                    l = m + 1
        return idx


x = Solution()
print(x.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
