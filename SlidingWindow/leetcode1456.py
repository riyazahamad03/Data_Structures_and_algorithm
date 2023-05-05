class solution:
    def vow(self,  x):
        if x in 'aeiou':
            return 1
        return 0

    def maxVowels(self, s: str, k: int) -> int:
        l, r, count, res = 0, 0, 0, 0
        while r < len(s):
            count += self.vow(s[r])
            if r - l >= k:
                count -= self.vow(s[l])
                l += 1
            res = max(res, count)
            r += 1
        return res


x = solution()
print(x.maxVowels("abciiidef", 3))
