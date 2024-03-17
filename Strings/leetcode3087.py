import heapq
from collections import Counter


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        count = Counter(s)
        minHeap = []
        for i in range(97, 123):
            heapq.heappush(minHeap, [count[chr(i)], chr(i)])
        res = []
        for c in s:
            if c == "?":
                cnt, val = heapq.heappop(minHeap)
                res.append(val)
                heapq.heappush(minHeap, [cnt + 1, val])
        res.sort()
        idx = 0
        ans = []

        for c in s:
            if c == "?":
                ans.append(res[idx])
                idx += 1
            else:
                ans.append(c)
        return "".join(ans)


x = Solution()
print(x.minimizeStringValue(s="a?a?"))
