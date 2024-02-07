class Solution:
    def frequencySort(self, s: str) -> str:
        count = [[] for _ in range(len(s) + 1)]
        mp = {}
        for i in s:
            mp[i] = 1 + mp.get(i, 0)

        for i in mp:
            count[mp[i]].append(i)
        res = ""
        for i in range(len(s), -1, -1):
            for j in count[i]:
                cnt = mp[j]
                res += j * cnt
        return res


x = Solution()
print(x.frequencySort("cccaaa"))
