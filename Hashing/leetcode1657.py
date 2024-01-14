from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq_a, freq_b = Counter(word1), Counter(word2)
        if (sorted(freq_a.values()) != sorted(freq_b.values())) or (
            set(word1) != set(word2)
        ):
            return False
        return True


x = Solution()
print(x.closeStrings("abc", "bca"))
