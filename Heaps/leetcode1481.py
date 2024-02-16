from collections import Counter
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        minHeap = []
        count = Counter(arr)
        for c in count:
            heapq.heappush(minHeap, [count[c], c])
        while k > 0:
            cnt, val = heapq.heappop(minHeap)
            k -= 1
            if cnt - 1 > 0:
                heapq.heappush(minHeap, [cnt - 1, val])
        return len(minHeap)


x = Solution()
print(x.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
