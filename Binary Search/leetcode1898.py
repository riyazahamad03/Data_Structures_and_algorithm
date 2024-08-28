class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def isSub(s, p):
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i in removed or s[i] != p[j]:
                    i += 1
                    continue
                i, j = i + 1, j + 1
            return j == len(p)

        l, r = 0, len(removable) - 1
        res = 0
        while l <= r:
            m = (l + r) // 2
            removed = set(removable[: m + 1])
            if isSub(s, p):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1
        return res


x = Solution()
print(x.maximumRemovals("abcbddddd"))
