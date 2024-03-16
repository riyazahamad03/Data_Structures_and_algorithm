class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        zero, one = 0, 0
        res = 0
        diff = {}

        for i, n in enumerate(nums):
            if n == 1:
                one += 1
            else:
                zero += 1
            if one - zero not in diff:

                diff[one - zero] = i

            if one == zero:
                res = one + zero
            if one - zero in diff:
                idx = diff[one - zero]
                res = max(res, i - idx)

        return res


x = Solution()
print(x.findMaxLength(nums=[0, 1, 0]))
