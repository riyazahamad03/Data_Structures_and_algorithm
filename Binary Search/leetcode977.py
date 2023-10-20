class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        l, r = 0, len(nums) - 1
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
print(x.sortedSquares(nums=[-4, -1, 0, 3, 10]))
