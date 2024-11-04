class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        idx = 0

        while idx < len(word):
            cons = 0
            curr = word[idx]

            while idx < len(word) and cons < 9 and word[idx] == curr:
                cons += 1
                idx += 1

            res += str(cons)
            res += curr
        return res


x = Solution()
print(x.compressedString(word="abcde"))
