class Solution:
    def minOperations(self, s: str) -> int:
        s1 = s2 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    s2 += 1
                else:
                    s1 += 1
            else:
                if s[i] == "0":
                    s1 += 1
                else:
                    s2 += 1
        return min(s1, s2)


x = Solution()
print(x.minOperations("1101110101"))
