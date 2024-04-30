class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        pref = 0
        count = [0] * 1024
        count[0] = 1

        for c in word:
            pref ^= 1 << ord(c) - ord("a")

            ans += count[pref]

            ans += sum(count[pref ^ 1 << i] for i in range(10))
            count[pref] += 1

        return ans


x = Solution()
print(x.wonderfulSubstrings("aabb"))
