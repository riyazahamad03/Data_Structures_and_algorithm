import heapq


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        maxHeap = []
        d = {score[i]: i for i in range(len(score))}
        res = [""] * (len(score))
        for i in score:
            heapq.heappush(maxHeap, -1 * i)
        idx = 0
        while maxHeap:
            val = -1 * heapq.heappop(maxHeap)
            index = d[val]
            if idx == 0:
                res[index] = "Gold Medal"
            elif idx == 1:
                res[index] = "Silver Medal"
            elif idx == 2:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(idx + 1)
            idx += 1
        return res


x = Solution()
print(x.findRelativeRanks(score=[10, 3, 8, 9, 4]))
