class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                if i < len(s) // 2:
                    count += 1
                else:
                    count -= 1
        return count == 0


x = Solution()
print(x.halvesAreAlike("book"))
