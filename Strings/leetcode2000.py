class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                return word[: i + 1][::-1] + word[i + 1 : :]
        return word


x = Solution()
print(x.reversePrefix(word="abcdefd", ch="d"))
