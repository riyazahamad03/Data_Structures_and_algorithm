from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for i in cnt:
            res += cnt[i]*(cnt[i] - 1)//2
        return res


x = Solution()
print(x.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
