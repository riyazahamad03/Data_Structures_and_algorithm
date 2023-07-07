class solution:
    def maxConsecutiveAnswers(self, answerKey: list[str], k: int):
        res = k
        count = {'T': 0, 'F': 0}
        for i in range(k):
            count[answerKey[i]] += 1
        l = 0
        for r in range(k, len(answerKey)):
            count[answerKey[r]] += 1

            while min(count['T'], count['F']) > k:
                count[answerKey[r]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


X = solution()
print(X.maxConsecutiveAnswers(answerKey="TTFF", k=2))
