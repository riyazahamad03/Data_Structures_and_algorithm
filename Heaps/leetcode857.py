import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        res = float("inf")
        pairs = []
        for i in range(len(quality)):
            pairs.append((wage[i] / quality[i], quality[i]))
        pairs.sort(key=lambda p: p[0])

        max_heap = []
        total = 0
        for r, q in pairs:
            heapq.heappush(max_heap, -q)
            total += q

            if len(max_heap) > k:
                total += heapq.heappop(max_heap)
            if len(max_heap) == k:
                res = min(res, total * r)
        return res


x = Solution()
print(x.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2))
