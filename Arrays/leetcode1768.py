class solution:
    def mergeAlternately(self, word1: str, word2: str):
        res, idex = [], 0
        minLen = min(len(word1), len(word2))
        while idex < minLen:
            res.append(word1[idex])
            res.append(word2[idex])
            idex += 1
        while idex < len(word1):
            res.append(word1[idex])
            idex += 1
        while idex < len(word1):
            res.append(word2[idex])
            idex += 1
        return "".join(res)


x = solution()
print(x.mergeAlternately("abc", "pqr"))
