class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        mp = {}
        mx = 0
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
            mx = max(mx, mp[i])
        res = 0
        for i in mp:
            if mp[i] == mx:
                res += mx
        return res


x = Solution()
print(x.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
