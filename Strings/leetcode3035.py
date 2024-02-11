from collections import Counter


class Solution:
    def maxPalindromesAfterOperations(self, words: list[str]) -> int:
        char = Counter()
        for word in words:
            char.update(Counter(word))
        pair_count, ind_count = 0, 0
        for c in char:
            if char[c] % 2:
                ind_count += 1
            pair_count += (char[c] // 2) * 2
        words = sorted(words, key=lambda x: len(x))
        res = 0
        for word in words:
            word_count = len(word)
            if word_count % 2:
                cnt = (word_count // 2) * 2
                if ind_count > 0 and pair_count - cnt >= 0:

                    ind_count -= 1
                    pair_count -= cnt
                    res += 1
                elif pair_count - (cnt + 2) >= 0:
                    pair_count -= cnt + 2
                    ind_count += 1
                    res += 1
            else:
                if word_count <= pair_count:
                    pair_count -= word_count
                    res += 1

        return res


x = Solution()
print(x.maxPalindromesAfterOperations(["abbb", "ba", "aa"]))
