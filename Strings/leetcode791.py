from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        count = Counter(s)
        for x in order:
            if x in s:

                res += count[x] * x
        for y in s:
            if y not in order:
                res += y
        return res


x = Solution()
print(x.customSortString(order="bcafg", s="abcd"))
