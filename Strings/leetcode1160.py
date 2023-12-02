class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        charMap = {}
        for i in chars:
            charMap[i] = 1 + charMap.get(i, 0)
        res = 0
        for word in words:
            wordCnt = {}
            fl = False
            for char in word:
                wordCnt[char] = 1 + wordCnt.get(char, 0)

                if char not in charMap or wordCnt[char] > charMap[char]:
                    fl = True
                    break

            res += len(word) if not fl else 0
        return res


x = Solution()
print(x.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
