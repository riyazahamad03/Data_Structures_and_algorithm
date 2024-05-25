class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_dict = set(wordDict)

        def back_track(i):
            if i == len(s):
                res.append(" ".join(curr))
                return
            for j in range(i, len(s)):
                if s[i : j + 1] in word_dict:
                    curr.append(s[i : j + 1])
                    back_track(j + 1)
                    curr.pop()

        res, curr = [], []
        back_track(0)
        return res


x = Solution()
print(x.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
