class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if (m - 1 < 0 or nums[m] != nums[m - 1]) and (
                m + 1 == len(nums) or nums[m] != nums[m + 1]
            ):
                return nums[m]
            else:
                if m + 1 < len(nums) and nums[m] == nums[m + 1]:
                    leftOver = m
                else:
                    leftOver = m - 1

                if leftOver % 2 == 0:
                    l = m + 1
                else:
                    r = m


x = Solution()
print(x.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
