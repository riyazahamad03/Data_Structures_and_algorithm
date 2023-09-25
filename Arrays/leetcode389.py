class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1, s2 = 0, 0
        for i in t:
            s1 += ord(i)
        for i in s:
            s2 += ord(i)

        return chr(s1 - s2)


x = Solution()
print(x.findTheDifference(s="abcd", t="abcde"))
