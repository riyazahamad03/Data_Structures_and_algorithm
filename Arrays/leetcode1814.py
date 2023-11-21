import collections


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        def rev(x):
            res = 0
            while x:
                res = res * 10 + x % 10
                x //= 10
            return res

        arr = []

        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))

        dic = collections.defaultdict(int)
        ans = 0
        mod = 10**9 + 7

        for num in arr:
            ans = (ans + dic[num]) % mod
            dic[num] += 1

        return ans


x = Solution()
print(x.countNicePairs([42, 11, 1, 97]))
