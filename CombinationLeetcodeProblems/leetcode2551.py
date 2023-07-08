class solution:
    def putMarbles(self, weights: list[int], k: int):
        pairWeights = []
        for i in range(len(weights) - 1):
            pairWeights.append(weights[i] + weights[i + 1])
        pairWeights.sort()
        res = 0
        for i in range(k - 1):
            res += pairWeights[len(pairWeights)-i-1] - pairWeights[i]
        return res


x = solution()
print(x.putMarbles(weights=[1, 3, 5, 1], k=2))
