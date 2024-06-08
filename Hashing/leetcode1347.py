class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mp = {}
        res = 0
        for i in s:
            mp[i] = 1 + mp.get(i, 0)
        for i in t:
            if i in mp and mp[i] > 0:
                mp[i] -= 1
            else:
                res += 1
        return res


x = Solution()
print(x.minSteps(s="leetcode", t="practice"))
