class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(1, n):
            prev, res = "", ""
            streak = 0
            for c in s:
                if c == prev or prev == "":
                    streak += 1
                else:
                    res += str(streak) + prev
                    streak = 1
                prev = c
            res += str(streak) + prev
            s = res
        return s


x = Solution()
print(x.countAndSay(30))
