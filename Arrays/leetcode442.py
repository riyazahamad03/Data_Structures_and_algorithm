class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        n = len(nums)
        for i in range(n):
            v = abs(nums[i]) - 1
            if nums[v] < 0:
                res.append(v + 1)
            nums[v] *= -1
        return res


x = Solution()
print(x.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
