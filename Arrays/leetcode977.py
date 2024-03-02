from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            lVal = abs(nums[l] * nums[l])
            rVal = abs(nums[r] * nums[r])

            if lVal > rVal:
                res.append(lVal)
                l += 1
            else:
                res.append(rVal)
                r -= 1
        return res[::-1]


x = Solution()
print(x.sortedSquares([-7, -3, 2, 3, 11]))
