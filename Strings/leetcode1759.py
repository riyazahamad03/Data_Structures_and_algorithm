class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = ["", 0]
        cnt = 0
        mod = (10**9) + 7
        for i in range(len(s)):
            if s[i] != prev[0]:
                prev = [s[i], 0]
            prev[1] += 1

            cnt += prev[1]
            cnt = cnt % mod
        return cnt


x = Solution()
print(x.countHomogenous("abbcccaa"))
