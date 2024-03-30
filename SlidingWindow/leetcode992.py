import collections


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        count = collections.defaultdict(int)
        res = 0
        lNear, lFar = 0, 0
        res = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while len(count) > k:
                count[nums[lNear]] -= 1
                if (count[nums[lNear]]) == 0:
                    count.pop(nums[lNear])
                lNear += 1
                lFar = lNear
            while count[nums[lNear]] > 1:
                count[nums[lNear]] -= 1
                lNear += 1
            if len(count) == k:
                res += lNear - lFar + 1
        return res


x = Solution()
print(x.subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
