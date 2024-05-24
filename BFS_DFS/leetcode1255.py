from collections import Counter
class Solution:
    def maxScoreWords(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        letter_cnt = Counter(letters)

        def can_form(w, letter_cnt):
            word_cnt = Counter(w)
            for c in word_cnt:
                if word_cnt[c] > letter_cnt[c]:
                    return False
            return True

        def get_score(w):
            res = 0
            for c in w:
                res += score[ord(c) - ord("a")]
            return res

        def backtrack(i):
            if i == len(words):
                return 0
            res = backtrack(i + 1)
            if can_form(words[i], letter_cnt):
                for c in words[i]:
                    letter_cnt[c] -= 1
                res = max(res, get_score(words[i]) + backtrack(i + 1))
                for c in words[i]:
                    letter_cnt[c] += 1
            return res

        return backtrack(0)


x = Solution()
print(
    x.maxScoreWords(
        words=["dog", "cat", "dad", "good"],
        letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        score=[
            1,
            0,
            9,
            5,
            0,
            0,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )
)
