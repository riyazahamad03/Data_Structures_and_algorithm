class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # res = ""
        # for i in range(len(s)):

        #     if s[i].isdigit():
        #         res += res * (int(s[i]) - 1)
        #     else:
        #         res += s[i]

        #     if len(res) >= k:
        #         return res[k - 1]

        length = 0

        for c in s:
            if c.isdigit():
                length = length * (int(c))
            else:
                length += 1

        for idx in range(len(s) - 1, - 1, - 1):
            k = k % length
            if s[idx].isdigit():
                length = length // int(s[idx])
            elif k == 0 or k == length:
                return s[idx]
            else:
                length -= 1


x = Solution()
print(x.decodeAtIndex(s="leet2code3", k=10))
