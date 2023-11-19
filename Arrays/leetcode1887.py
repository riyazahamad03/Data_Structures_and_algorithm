import collections


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        res = 0
        count = collections.Counter(nums)
        keys = list(count.keys())
        keys.sort()
        for i in range(len(keys) - 1, 0, -1):
            res += i * (count[keys[i]])
        return res


x = Solution()
print(x.reductionOperations([1, 1, 2, 2, 3]))
