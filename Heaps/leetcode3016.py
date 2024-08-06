from collections import Counter
import heapq


class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        mx = []

        for i in count:
            heapq.heappush(mx, -1 * (count[i]))
        res = 0
        idx = 0
        while mx:
            m = -1 * (heapq.heappop(mx))
            c = (idx // 8) + 1
            res += m * c
            idx += 1
        return res


x = Solution()

print(x.minimumPushes(word="xyzxyzxyzxyz"))
